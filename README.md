⚡ Quick-Py

A lightweight, floating Python scratchpad that lets you quickly write, run, and test Python code in a minimal always-on-top UI.

🚀 Features
🧠 Instant Python execution (Ctrl/Cmd + Enter)
🪟 Floating always-on-top mini window
✍️ Multi-line code editor
🎨 Dark-themed editor (#707070)
⚡ Auto indentation support
🔗 Auto bracket/quote pairing
⌨ Tab-based autocomplete (Python keywords)
📜 Scrollable output console
🧵 Non-blocking execution (runs in background thread)
⏱ Execution timeout (prevents freezes)
🧹 Clear editor and output buttons


🖼️ UI Overview
Editor / Code section: Write Python code
Output section: Displays execution results and errors
Run / Clear buttons: Quick actions for execution control
🛠️ Installation
1. Clone the repository
git clone https://github.com/arrennbaral/quick-py.git
cd quick-py
2. Run the app
python quick_py.py
📦 Requirements

No external dependencies required.

Built using:

Python 3.x
Tkinter (standard library)
subprocess, threading (standard library)

▶️ Usage
Run Code
Press Ctrl + Enter (Windows/Linux)
Press Cmd + Enter (Mac)
Or click Run
Clear Editor
Click Clear


💡 Example
for i in range(5):
    print(i)
Output:
0
1
2
3
4
⚙️ Design Goals

Quick-Py is designed to be:

⚡ Fast (no setup, instant execution)
🪶 Lightweight (single-file tool)
🧪 Ideal for quick testing & debugging
🧑‍💻 Developer-friendly scratchpad
🔒 Safety Note

Code execution runs in a sandboxed subprocess with timeout limits to prevent freezing.
However, it is still intended for local development use only, not as a secure public code runner.

📌 Future Improvements
Syntax highlighting
Line numbers
Draggable floating widget
Save / load scripts
Theme switcher (dark/light)
Command palette (Ctrl+P style)
Stronger sandbox isolation (Docker-based execution)
🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

⭐ Show Support

If you like this project, consider giving it a ⭐ on GitHub!
