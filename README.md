<div align="center">

```
 █████╗ ██╗   ██╗████████╗ ██████╗ ███████╗██╗  ██╗███████╗██╗     ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██║  ██║██╔════╝██║     ██║
███████║██║   ██║   ██║   ██║   ██║███████╗███████║█████╗  ██║     ██║
██╔══██║██║   ██║   ██║   ██║   ██║╚════██║██╔══██║██╔══╝  ██║     ██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝███████║██║  ██║███████╗███████╗███████╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
```

**Automate your Windows desktop with a simple, human-readable scripting language.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](https://github.com/Linus342010/AutoShell)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

</div>

---

## ✦ What is AutoShell?

AutoShell is a **lightweight GUI automation tool** for Windows that lets you write automation scripts in a clean, readable `.ashell` format — no complex Python knowledge required. Just write commands, run the script, done.

```ashell
# Launch the browser and search for something
open_app("chrome.exe")
wait(1500)
type_text("https://github.com")
key_press("enter")
screenshot("result.png")
```

---

## ✦ Features

| Feature | Description |
|--------|-------------|
| 🖱️ **Mouse Control** | Move, click, double-click, right-click at any screen position |
| ⌨️ **Keyboard Input** | Type text, press keys, trigger hotkey combos |
| 🔍 **Screen Reading** | Take screenshots, find images on screen |
| ⏱️ **Timing & Flow** | Wait, loop, and control script execution |
| 🪟 **App Launcher** | Open any application by executable name |
| 💬 **Comments** | Use `#` to document your scripts |

---

## ✦ Installation

**1. Clone the repository**
```bash
git clone https://github.com/Linus342010/AutoShell.git
cd AutoShell
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run your first script**
```bash
python main.py my_script.ashell
```

---

## ✦ Script Syntax

AutoShell uses a simple function-call syntax. Each line is one command:

```ashell
# ── Mouse ──────────────────────────────────────────
move_to(960, 540)          # Move mouse to coordinates
click(960, 540)            # Left click
right_click(200, 300)      # Right click
double_click(400, 400)     # Double click

# ── Keyboard ───────────────────────────────────────
type_text("Hello, World!") # Type a string
key_press("enter")         # Press a single key
hotkey("ctrl", "c")        # Trigger a key combo

# ── System ─────────────────────────────────────────
open_app("notepad.exe")    # Launch an application
wait(2000)                 # Wait 2 seconds
screenshot("snap.png")     # Save a screenshot
```

---

## ✦ Project Structure

```
AutoShell/
│
├── main.py            ← Entry point (CLI)
├── execute.py         ← Script executor / interpreter
├── commands.py        ← Command definitions & dispatch
├── log.py             ← Logging utilities
│
├── scripts/           ← Your .ashell scripts go here
│   └── example.ashell
│
└── requirements.txt
```

---

## ✦ Example Script

Save this as `scripts/open_notepad.ashell`:

```ashell
# Open Notepad and type a message
open_app("notepad.exe")
wait(1000)
type_text("AutoShell is running!")
key_press("enter")
type_text("Automation made simple.")
hotkey("ctrl", "s")
```

Run it:
```bash
python main.py scripts/open_notepad.ashell
```

---

## ✦ Roadmap

- [x] Basic mouse & keyboard commands
- [x] App launching
- [x] Screenshot support
- [x] Comment support (`#`)
- [x] CSV-based robust line parser
- [ ] `if` / `else` conditionals
- [ ] `loop` support
- [ ] Variable assignment
- [ ] GUI editor for `.ashell` scripts
- [ ] Packaged `.exe` release

---

## ✦ Requirements

- Python 3.8+
- Windows 10 / 11
- `pyautogui`
- `pygetwindow` *(optional, for window management)*

---

## ✦ Contributing

Pull requests are welcome! If you find a bug or have a feature idea, open an [issue](https://github.com/Linus342010/AutoShell/issues).

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push and open a PR

---

## ✦ License

MIT License — free to use, modify, and distribute.

---

<div align="center">

Made with ☕ and Python by [Linus342010](https://github.com/Linus342010)

</div>
