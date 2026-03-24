import tkinter as tk
import subprocess
import sys
import threading
import re
import keyword

# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("Quick-Py")

# middle-right positioning
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 450
window_height = 520

x = screen_width - window_width - 20
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.attributes("-topmost", True)


# ---------------- RUN SANDBOX ----------------
def run_code_sandboxed():
    code = entry.get("1.0", tk.END)

    def worker():
        try:
            result = subprocess.run(
                [sys.executable, "-c", code],
                capture_output=True,
                text=True,
                timeout=3
            )

            output_box.config(state="normal")
            output_box.delete("1.0", tk.END)

            if result.stdout:
                output_box.insert(tk.END, result.stdout)
            if result.stderr:
                output_box.insert(tk.END, result.stderr)

            if not result.stdout and not result.stderr:
                output_box.insert(tk.END, "✔ executed")

            output_box.config(state="disabled")

        except subprocess.TimeoutExpired:
            output_box.config(state="normal")
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, "⚠ Execution timed out (3s limit)")
            output_box.config(state="disabled")

    threading.Thread(target=worker, daemon=True).start()


# ---------------- AUTO INDENT ----------------
def handle_enter(event):
    line = entry.get("insert linestart", "insert")
    indent = re.match(r"^\s*", line).group()

    if line.strip().endswith(":"):
        indent += "    "

    entry.insert("insert", "\n" + indent)
    return "break"


# ---------------- AUTO PAIRS ----------------
def auto_pair(event):
    pairs = {"(": "()", "[": "[]", "{": "{}", "\"": "\"\"", "'": "''"}
    ch = event.char
    if ch in pairs:
        entry.insert("insert", pairs[ch])
        entry.mark_set("insert", "insert-1c")
        return "break"


# ---------------- AUTOCOMPLETE (TAB) ----------------
def autocomplete(event):
    if event.keysym != "Tab":
        return

    if event.state & 0x1:
        return

    line = entry.get("insert linestart", "insert")
    match = re.search(r"(\w+)$", line)

    if not match:
        return "break"

    prefix = match.group(1)

    suggestions = list(keyword.kwlist)
    matches = [s for s in suggestions if s.startswith(prefix)]

    if not matches:
        return "break"

    completion = matches[0][len(prefix):]
    entry.insert("insert", completion)
    return "break"


# ---------------- UI ELEMENTS ----------------

# Title
title = tk.Label(root, text="Quick-Py", font=("Arial", 16, "bold"))
title.pack(pady=8)

# Editor label
tk.Label(root, text="Editor / Code", font=("Arial", 11, "bold")).pack(anchor="w", padx=10)

# Editor (production styling)
entry = tk.Text(
    root,
    height=10,
    font=("Consolas", 12),
    bg="#707070",
    fg="white",
    insertbackground="white",
    wrap="word"
)
entry.pack(fill="both", expand=True, padx=10, pady=5)

entry.bind("<Return>", handle_enter)
entry.bind("<Key>", auto_pair)
entry.bind("<Tab>", autocomplete)
entry.bind("<Shift-Tab>", lambda e: "break")

# Output label
tk.Label(root, text="Output", font=("Arial", 11, "bold")).pack(anchor="w", padx=10)

# Output box (read-only + scrollable)
output_frame = tk.Frame(root)
output_frame.pack(fill="both", expand=True, padx=10, pady=5)

output_box = tk.Text(
    output_frame,
    height=8,
    font=("Consolas", 11),
    wrap="word",
    state="disabled"
)
output_box.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(output_frame, command=output_box.yview)
output_box.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")


# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(root)
btn_frame.pack(pady=8)

tk.Button(btn_frame, text="Run (Ctrl/Cmd+Enter)", command=run_code_sandboxed).pack(side="left", padx=5)

def clear_all():
    entry.delete("1.0", tk.END)
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.config(state="disabled")

tk.Button(btn_frame, text="Clear", command=clear_all).pack(side="left", padx=5)


# hotkeys
root.bind("<Control-Return>", lambda e: run_code_sandboxed())
root.bind("<Command-Return>", lambda e: run_code_sandboxed())


root.mainloop()