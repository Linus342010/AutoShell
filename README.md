# AutoShell

AutoShell is a Python program that implements a small, custom scripting language for automating tasks on Windows. The project is a work in progress and aims to become a lightweight shortcut-like app where users can write simple scripts (files) that AutoShell reads and executes line by line. Future plans include a drag-and-drop GUI and easier packaging for Windows.

Status: Work in progress

Short goals:
- Provide an easy-to-write scripting language for Windows automation
- Allow running scripts from files (current)
- Offer a GUI builder and app-style installer (planned)

Authors: Linus342010 and TheShadow1984

Badges

Place project badges here (status, license, build, coverage). Example placeholders:

[![build status](https://img.shields.io/badge/build-WIP-orange)](https://github.com/your/repo)
[![license](https://img.shields.io/badge/license-ADD--LICENSE-lightgrey)](./LICENSE)


Features

- Custom, minimal scripting language for Windows automation
- File-based scripts executed line-by-line (current)
- Intended: drag-and-drop GUI for non-coders (planned)
- Intended: packaging as a Windows shortcut/app for easy distribution (planned)


Installation

Prerequisites:
- Python 3.8+ installed on Windows

Quick start (example):

1. Clone the repository:

```bash
git clone https://github.com/Linus342010/AutoShell.git
cd AutoShell
```

2. Install dependencies (if any):

```bash
python -m pip install -r requirements.txt
```

If there is no requirements.txt, just run with Python directly.


Run Locally

To run a script file with AutoShell (example):

```bash
python AutoShell.py path/to/your_script.ashell
```

Replace `AutoShell.py` with the actual entrypoint filename in the repository if different.


Usage/Examples

Example script (example_script.ashell):

```ashell
# Open Notepad
open "notepad.exe"
# Wait 1 second
sleep 1
# Type some text
type "Hello from ashell"
# Save and exit (pseudo-commands; implement as available)
press "ctrl+s"
press "alt+f4"
```

Run it with:

```bash
python AutoShell.py example_script.ashell
```

Note: The exact commands and syntax depend on the current implementation. Add a documentation file with the language reference when available.


Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Make changes and add tests if appropriate.
4. Push to your fork and open a Pull Request describing your changes.

Please open an issue first if you plan a larger feature so maintainers can provide guidance. Add a CONTRIBUTORS or CONTRIBUTING file for more detailed rules (code style, tests, commit message format).


License

This project currently does not include a LICENSE file in the repo. Add a LICENSE (recommended: MIT) to make the project's license explicit.

Example: "MIT License — see LICENSE file"


Roadmap

Planned improvements:
- Implement more built-in commands (file ops, window management, scheduling)
- Add a drag-and-drop GUI builder for non-coders
- Create an installer or single-exe for Windows
- Provide full documentation and a language reference


Authors

- Linus342010
- TheShadow1984

Add contact links or GitHub profile links here.


Support
 
For support or to report bugs, open an issue in the project's GitHub repository or contact the authors via their GitHub profiles.
