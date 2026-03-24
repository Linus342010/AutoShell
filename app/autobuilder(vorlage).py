import sys
import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QScrollArea, QPushButton, QFrame, QSizePolicy,
    QFileDialog, QMessageBox, QLineEdit, QSpinBox, QComboBox,
    QDialog, QFormLayout, QDialogButtonBox, QTextEdit, QSplitter,
    QToolBar, QStatusBar, QListWidget, QListWidgetItem, QGroupBox
)
from PySide6.QtCore import (
    Qt, QMimeData, QPoint, Signal, QSize, QTimer, QPropertyAnimation,
    QEasingCurve, QRect, QObject
)
from PySide6.QtGui import (
    QDrag, QPixmap, QPainter, QColor, QFont, QFontDatabase,
    QPen, QBrush, QLinearGradient, QAction, QKeySequence, QIcon,
    QCursor, QPalette
)

# ─── Color Palette ────────────────────────────────────────────────────────────
COLORS = {
    "bg":           "#0d0f14",
    "surface":      "#13161f",
    "surface2":     "#1a1e2b",
    "border":       "#252a3a",
    "accent":       "#4f8ef7",
    "accent_dim":   "#2a4a8a",
    "text":         "#c8d0e8",
    "text_dim":     "#5a6280",
    "text_bright":  "#eef2ff",
    "gui":          "#7c5cbf",
    "gui_dim":      "#3d2e60",
    "app":          "#2e8b6e",
    "app_dim":      "#174434",
    "logic":        "#c97a2e",
    "logic_dim":    "#5a3614",
    "sys":          "#b03a4e",
    "sys_dim":      "#521921",
    "success":      "#3dba7e",
    "warning":      "#e8a84a",
    "danger":       "#e05c6a",
}

# ─── Command Definitions ──────────────────────────────────────────────────────
COMMANDS = {
    "GUI-Aktionen": {
        "color": COLORS["gui"],
        "dim": COLORS["gui_dim"],
        "icon": "🖱",
        "commands": [
            {"name": "click", "label": "Mausklick", "params": [
                {"key": "x", "type": "int", "default": 0, "label": "X"},
                {"key": "y", "type": "int", "default": 0, "label": "Y"},
                {"key": "button", "type": "combo", "options": ["left","right","middle"], "default": "left", "label": "Taste"},
            ]},
            {"name": "type_text", "label": "Text tippen", "params": [
                {"key": "text", "type": "str", "default": "Hallo", "label": "Text"},
                {"key": "interval", "type": "float", "default": 0.05, "label": "Interval (s)"},
            ]},
            {"name": "hotkey", "label": "Tastenkürzel", "params": [
                {"key": "keys", "type": "str", "default": "ctrl+s", "label": "Keys (z.B. ctrl+s)"},
            ]},
            {"name": "screenshot", "label": "Screenshot", "params": [
                {"key": "path", "type": "str", "default": "screenshot.png", "label": "Pfad"},
            ]},
            {"name": "move_mouse", "label": "Maus bewegen", "params": [
                {"key": "x", "type": "int", "default": 100, "label": "X"},
                {"key": "y", "type": "int", "default": 100, "label": "Y"},
                {"key": "duration", "type": "float", "default": 0.3, "label": "Dauer (s)"},
            ]},
            {"name": "scroll", "label": "Scrollen", "params": [
                {"key": "clicks", "type": "int", "default": 3, "label": "Klicks"},
                {"key": "direction", "type": "combo", "options": ["up","down"], "default": "down", "label": "Richtung"},
            ]},
        ]
    },
    "App-Steuerung": {
        "color": COLORS["app"],
        "dim": COLORS["app_dim"],
        "icon": "⚙",
        "commands": [
            {"name": "open_app", "label": "App öffnen", "params": [
                {"key": "path", "type": "str", "default": "notepad.exe", "label": "Pfad/Name"},
            ]},
            {"name": "close_app", "label": "App schließen", "params": [
                {"key": "name", "type": "str", "default": "Notepad", "label": "Fenster-Titel"},
            ]},
            {"name": "focus_window", "label": "Fenster fokussieren", "params": [
                {"key": "title", "type": "str", "default": "Notepad", "label": "Titel"},
            ]},
            {"name": "wait_for_window", "label": "Warte auf Fenster", "params": [
                {"key": "title", "type": "str", "default": "Notepad", "label": "Titel"},
                {"key": "timeout", "type": "int", "default": 10, "label": "Timeout (s)"},
            ]},
        ]
    },
    "Logik & Ablauf": {
        "color": COLORS["logic"],
        "dim": COLORS["logic_dim"],
        "icon": "⟳",
        "commands": [
            {"name": "wait", "label": "Warten", "params": [
                {"key": "seconds", "type": "float", "default": 1.0, "label": "Sekunden"},
            ]},
            {"name": "repeat", "label": "Wiederholen", "params": [
                {"key": "count", "type": "int", "default": 3, "label": "Anzahl"},
            ]},
            {"name": "set_var", "label": "Variable setzen", "params": [
                {"key": "name", "type": "str", "default": "x", "label": "Name"},
                {"key": "value", "type": "str", "default": "0", "label": "Wert"},
            ]},
            {"name": "if_image", "label": "Wenn Bild sichtbar", "params": [
                {"key": "image", "type": "str", "default": "button.png", "label": "Bild-Datei"},
                {"key": "confidence", "type": "float", "default": 0.9, "label": "Sicherheit"},
            ]},
        ]
    },
    "System": {
        "color": COLORS["sys"],
        "dim": COLORS["sys_dim"],
        "icon": "💻",
        "commands": [
            {"name": "run_shell", "label": "Shell-Befehl", "params": [
                {"key": "command", "type": "str", "default": "echo hello", "label": "Befehl"},
            ]},
            {"name": "copy_file", "label": "Datei kopieren", "params": [
                {"key": "src", "type": "str", "default": "C:/src.txt", "label": "Quelle"},
                {"key": "dst", "type": "str", "default": "C:/dst.txt", "label": "Ziel"},
            ]},
            {"name": "write_file", "label": "Datei schreiben", "params": [
                {"key": "path", "type": "str", "default": "output.txt", "label": "Pfad"},
                {"key": "content", "type": "str", "default": "Inhalt", "label": "Inhalt"},
            ]},
            {"name": "read_clipboard", "label": "Zwischenablage lesen", "params": []},
            {"name": "set_clipboard", "label": "In Zwischenablage", "params": [
                {"key": "text", "type": "str", "default": "Text", "label": "Text"},
            ]},
        ]
    },
}


# ─── Block Data Class ─────────────────────────────────────────────────────────
class ScriptBlock:
    _counter = 0

    def __init__(self, cmd_def, category_name, category_info):
        ScriptBlock._counter += 1
        self.id = ScriptBlock._counter
        self.cmd_def = cmd_def
        self.category_name = category_name
        self.color = category_info["color"]
        self.dim = category_info["dim"]
        self.icon = category_info["icon"]
        self.params = {}
        for p in cmd_def.get("params", []):
            self.params[p["key"]] = p["default"]


# ─── Block Editor Dialog ──────────────────────────────────────────────────────
class BlockEditorDialog(QDialog):
    def __init__(self, block: ScriptBlock, parent=None):
        super().__init__(parent)
        self.block = block
        self.setWindowTitle(f"Block bearbeiten – {block.cmd_def['label']}")
        self.setMinimumWidth(380)
        self.setStyleSheet(f"""
            QDialog {{
                background: {COLORS['surface']};
                color: {COLORS['text']};
                font-family: 'Consolas', monospace;
            }}
            QLabel {{
                color: {COLORS['text_dim']};
                font-size: 11px;
                letter-spacing: 1px;
                text-transform: uppercase;
            }}
            QLineEdit, QSpinBox, QComboBox {{
                background: {COLORS['bg']};
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                color: {COLORS['text_bright']};
                padding: 6px 10px;
                font-size: 13px;
                font-family: 'Consolas', monospace;
            }}
            QLineEdit:focus, QSpinBox:focus, QComboBox:focus {{
                border-color: {block.color};
            }}
            QPushButton {{
                background: {block.color};
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 20px;
                font-weight: bold;
                font-size: 13px;
            }}
            QPushButton:hover {{ opacity: 0.85; }}
            QPushButton[flat=true] {{
                background: {COLORS['border']};
                color: {COLORS['text_dim']};
            }}
        """)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        # Header
        title = QLabel(f"{self.block.icon}  {self.block.cmd_def['label']}")
        title.setStyleSheet(f"color: {self.block.color}; font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        # Params
        self.inputs = {}
        form = QFormLayout()
        form.setSpacing(10)
        form.setLabelAlignment(Qt.AlignRight)

        for p in self.block.cmd_def.get("params", []):
            key = p["key"]
            val = self.block.params.get(key, p["default"])
            label = QLabel(p["label"])

            if p["type"] == "combo":
                widget = QComboBox()
                for opt in p["options"]:
                    widget.addItem(opt)
                widget.setCurrentText(str(val))
            elif p["type"] == "int":
                widget = QSpinBox()
                widget.setRange(-99999, 99999)
                widget.setValue(int(val))
            else:
                widget = QLineEdit(str(val))

            self.inputs[key] = widget
            form.addRow(label, widget)

        if not self.block.cmd_def.get("params"):
            form.addRow(QLabel("Keine Parameter erforderlich."))

        layout.addLayout(form)

        # Buttons
        btn_row = QHBoxLayout()
        cancel = QPushButton("Abbrechen")
        cancel.setProperty("flat", True)
        cancel.clicked.connect(self.reject)
        ok = QPushButton("Übernehmen")
        ok.clicked.connect(self.accept_changes)
        btn_row.addWidget(cancel)
        btn_row.addStretch()
        btn_row.addWidget(ok)
        layout.addLayout(btn_row)

    def accept_changes(self):
        for p in self.block.cmd_def.get("params", []):
            key = p["key"]
            widget = self.inputs[key]
            if isinstance(widget, QComboBox):
                self.block.params[key] = widget.currentText()
            elif isinstance(widget, QSpinBox):
                self.block.params[key] = widget.value()
            else:
                self.block.params[key] = widget.text()
        self.accept()


# ─── Script Block Widget ──────────────────────────────────────────────────────
class BlockWidget(QFrame):
    deleted = Signal(object)
    edited = Signal(object)
    move_up = Signal(object)
    move_down = Signal(object)

    def __init__(self, block: ScriptBlock, parent=None):
        super().__init__(parent)
        self.block = block
        self.setFixedHeight(70)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setCursor(Qt.OpenHandCursor)
        self._build_ui()
        self._apply_style()

    def _apply_style(self):
        c = self.block.color
        d = self.block.dim
        self.setStyleSheet(f"""
            BlockWidget {{
                background: {d};
                border: 1px solid {c};
                border-left: 4px solid {c};
                border-radius: 6px;
            }}
            BlockWidget:hover {{
                background: {c}22;
            }}
        """)

    def _build_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 8, 8)
        layout.setSpacing(10)

        # Drag handle
        handle = QLabel("⠿")
        handle.setStyleSheet(f"color: {self.block.color}; font-size: 18px;")
        handle.setFixedWidth(20)
        layout.addWidget(handle)

        # Icon + name
        left = QVBoxLayout()
        left.setSpacing(2)
        name_label = QLabel(f"{self.block.icon}  {self.block.cmd_def['label']}")
        name_label.setStyleSheet(f"color: {self.block.color}; font-weight: bold; font-size: 13px; font-family: 'Consolas', monospace;")
        left.addWidget(name_label)

        self.param_label = QLabel(self._param_summary())
        self.param_label.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 11px; font-family: 'Consolas', monospace;")
        left.addWidget(self.param_label)
        layout.addLayout(left)
        layout.addStretch()

        # Buttons
        for icon, tooltip, signal_name in [
            ("↑", "Nach oben", "move_up"),
            ("↓", "Nach unten", "move_down"),
            ("✎", "Bearbeiten", "edited"),
            ("✕", "Löschen", "deleted"),
        ]:
            btn = QPushButton(icon)
            btn.setToolTip(tooltip)
            btn.setFixedSize(28, 28)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {COLORS['surface2']};
                    color: {COLORS['text_dim']};
                    border: 1px solid {COLORS['border']};
                    border-radius: 4px;
                    font-size: 12px;
                }}
                QPushButton:hover {{
                    background: {self.block.color};
                    color: white;
                    border-color: {self.block.color};
                }}
            """)
            sig = getattr(self, signal_name)
            btn.clicked.connect(lambda _, s=sig: s.emit(self.block))
            layout.addWidget(btn)

    def _param_summary(self):
        params = self.block.params
        if not params:
            return self.block.cmd_def["name"] + "()"
        parts = [f"{k}={v}" for k, v in params.items()]
        summary = f"{self.block.cmd_def['name']}({', '.join(parts)})"
        if len(summary) > 55:
            summary = summary[:52] + "…"
        return summary

    def refresh(self):
        self.param_label.setText(self._param_summary())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            mime.setText(f"MOVE:{self.block.id}")
            drag.setMimeData(mime)

            # Pixmap preview
            pix = QPixmap(self.size())
            self.render(pix)
            drag.setPixmap(pix)
            drag.setHotSpot(event.position().toPoint())
            drag.exec(Qt.MoveAction)


# ─── Drop Zone (Canvas) ───────────────────────────────────────────────────────
class CanvasWidget(QWidget):
    blocks_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.blocks: list[ScriptBlock] = []
        self.block_widgets: list[BlockWidget] = []

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(16, 16, 16, 16)
        self.layout.setSpacing(8)
        self.layout.setAlignment(Qt.AlignTop)

        self._drop_indicator = QFrame()
        self._drop_indicator.setFixedHeight(3)
        self._drop_indicator.setStyleSheet(f"background: {COLORS['accent']}; border-radius: 2px;")
        self._drop_indicator.hide()

        self._empty_label = QLabel("Befehle hierher ziehen\num dein Script zu bauen")
        self._empty_label.setAlignment(Qt.AlignCenter)
        self._empty_label.setStyleSheet(f"""
            color: {COLORS['text_dim']};
            font-size: 15px;
            font-family: 'Consolas', monospace;
            border: 2px dashed {COLORS['border']};
            border-radius: 8px;
            padding: 60px;
        """)
        self.layout.addWidget(self._empty_label)

    def _update_empty(self):
        if self.blocks:
            self._empty_label.hide()
        else:
            self._empty_label.show()

    def add_block(self, block: ScriptBlock, index: int = -1):
        w = BlockWidget(block)
        w.deleted.connect(self._remove_block)
        w.edited.connect(self._edit_block)
        w.move_up.connect(self._move_up)
        w.move_down.connect(self._move_down)

        if index < 0 or index >= len(self.blocks):
            self.blocks.append(block)
            self.block_widgets.append(w)
            self.layout.insertWidget(self.layout.count() - 1, w)
        else:
            self.blocks.insert(index, block)
            self.block_widgets.insert(index, w)
            self.layout.insertWidget(index, w)

        self._update_empty()
        self.blocks_changed.emit()

    def _remove_block(self, block):
        idx = next((i for i, b in enumerate(self.blocks) if b.id == block.id), -1)
        if idx >= 0:
            w = self.block_widgets.pop(idx)
            self.blocks.pop(idx)
            self.layout.removeWidget(w)
            w.deleteLater()
            self._update_empty()
            self.blocks_changed.emit()

    def _edit_block(self, block):
        dlg = BlockEditorDialog(block, self)
        if dlg.exec():
            idx = next((i for i, b in enumerate(self.blocks) if b.id == block.id), -1)
            if idx >= 0:
                self.block_widgets[idx].refresh()
            self.blocks_changed.emit()

    def _move_up(self, block):
        idx = next((i for i, b in enumerate(self.blocks) if b.id == block.id), -1)
        if idx > 0:
            self._swap(idx, idx - 1)

    def _move_down(self, block):
        idx = next((i for i, b in enumerate(self.blocks) if b.id == block.id), -1)
        if idx >= 0 and idx < len(self.blocks) - 1:
            self._swap(idx, idx + 1)

    def _swap(self, i, j):
        self.blocks[i], self.blocks[j] = self.blocks[j], self.blocks[i]
        self.block_widgets[i], self.block_widgets[j] = self.block_widgets[j], self.block_widgets[i]
        # Re-insert widgets
        wi = self.block_widgets[i]
        wj = self.block_widgets[j]
        self.layout.removeWidget(wi)
        self.layout.removeWidget(wj)
        self.layout.insertWidget(min(i, j), self.block_widgets[min(i, j)])
        self.layout.insertWidget(max(i, j), self.block_widgets[max(i, j)])
        self.blocks_changed.emit()

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        text = event.mimeData().text()

        if text.startswith("NEW:"):
            # New block from sidebar
            _, cat, cmd_name = text.split(":", 2)
            cat_info = COMMANDS[cat]
            cmd_def = next((c for c in cat_info["commands"] if c["name"] == cmd_name), None)
            if cmd_def:
                block = ScriptBlock(cmd_def, cat, cat_info)
                drop_idx = self._drop_index(event.position().toPoint())
                self.add_block(block, drop_idx)

        elif text.startswith("MOVE:"):
            block_id = int(text.split(":")[1])
            idx = next((i for i, b in enumerate(self.blocks) if b.id == block_id), -1)
            if idx >= 0:
                block = self.blocks[idx]
                w = self.block_widgets[idx]
                self.blocks.pop(idx)
                self.block_widgets.pop(idx)
                self.layout.removeWidget(w)
                w.deleteLater()
                drop_idx = self._drop_index(event.position().toPoint())
                self.add_block(block, drop_idx)

        event.acceptProposedAction()

    def _drop_index(self, pos):
        for i, w in enumerate(self.block_widgets):
            if pos.y() < w.y() + w.height() // 2:
                return i
        return len(self.blocks)

    def clear_all(self):
        for w in self.block_widgets:
            w.deleteLater()
        self.blocks.clear()
        self.block_widgets.clear()
        self._update_empty()
        self.blocks_changed.emit()

    def generate_script(self, fmt="ashell") -> str:
        lines = []
        if fmt == "ashell":
            lines.append("# Generated by AutoShell Builder")
            lines.append("")
            for b in self.blocks:
                parts = []
                for k, v in b.params.items():
                    if isinstance(v, str):
                        parts.append(f'{k}="{v}"')
                    else:
                        parts.append(f"{k}={v}")
                if parts:
                    lines.append(f"{b.cmd_def['name']}({', '.join(parts)})")
                else:
                    lines.append(f"{b.cmd_def['name']}()")
        else:  # txt function call style
            lines.append("# AutoShell Script")
            lines.append("")
            for b in self.blocks:
                args = []
                for v in b.params.values():
                    if isinstance(v, str):
                        args.append(f'"{v}"')
                    else:
                        args.append(str(v))
                lines.append(f"{b.cmd_def['name']}({', '.join(args)})")
        return "\n".join(lines)

    def to_json(self) -> str:
        data = []
        for b in self.blocks:
            data.append({
                "cmd": b.cmd_def["name"],
                "category": b.category_name,
                "params": b.params,
            })
        return json.dumps(data, indent=2, ensure_ascii=False)

    def load_json(self, text: str):
        self.clear_all()
        data = json.loads(text)
        for item in data:
            cat_name = item["category"]
            cat_info = COMMANDS.get(cat_name)
            if not cat_info:
                continue
            cmd_def = next((c for c in cat_info["commands"] if c["name"] == item["cmd"]), None)
            if not cmd_def:
                continue
            block = ScriptBlock(cmd_def, cat_name, cat_info)
            block.params = item["params"]
            self.add_block(block)


# ─── Sidebar Command Item ─────────────────────────────────────────────────────
class SidebarItem(QLabel):
    def __init__(self, cmd_def, cat_name, color, dim, icon, parent=None):
        super().__init__(parent)
        self.cmd_def = cmd_def
        self.cat_name = cat_name
        self.color = color
        self.dim = dim
        self.icon = icon
        self.setText(f"  {icon}  {cmd_def['label']}")
        self.setFixedHeight(36)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setCursor(Qt.OpenHandCursor)
        self._apply_style(False)

    def _apply_style(self, hover):
        if hover:
            self.setStyleSheet(f"""
                background: {self.color}33;
                color: {self.color};
                border: 1px solid {self.color};
                border-radius: 4px;
                font-size: 12px;
                font-family: 'Consolas', monospace;
                font-weight: bold;
                padding-left: 4px;
            """)
        else:
            self.setStyleSheet(f"""
                background: transparent;
                color: {COLORS['text']};
                border: 1px solid transparent;
                border-radius: 4px;
                font-size: 12px;
                font-family: 'Consolas', monospace;
                padding-left: 4px;
            """)

    def enterEvent(self, e):
        self._apply_style(True)

    def leaveEvent(self, e):
        self._apply_style(False)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            mime.setText(f"NEW:{self.cat_name}:{self.cmd_def['name']}")
            drag.setMimeData(mime)
            drag.exec(Qt.CopyAction)


# ─── Main Window ──────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoShell Builder")
        self.resize(1200, 750)
        self.setMinimumSize(900, 600)
        self._setup_style()
        self._build_ui()
        self._build_menu()

    def _setup_style(self):
        self.setStyleSheet(f"""
            QMainWindow, QWidget {{
                background: {COLORS['bg']};
                color: {COLORS['text']};
                font-family: 'Consolas', monospace;
            }}
            QScrollArea {{ border: none; }}
            QScrollBar:vertical {{
                background: {COLORS['surface']};
                width: 6px;
                border-radius: 3px;
            }}
            QScrollBar::handle:vertical {{
                background: {COLORS['border']};
                border-radius: 3px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {COLORS['accent']};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
            QToolBar {{
                background: {COLORS['surface']};
                border-bottom: 1px solid {COLORS['border']};
                spacing: 4px;
                padding: 4px 8px;
            }}
            QStatusBar {{
                background: {COLORS['surface']};
                color: {COLORS['text_dim']};
                border-top: 1px solid {COLORS['border']};
                font-size: 11px;
            }}
            QMenuBar {{
                background: {COLORS['surface']};
                color: {COLORS['text']};
                border-bottom: 1px solid {COLORS['border']};
            }}
            QMenuBar::item:selected {{ background: {COLORS['accent_dim']}; }}
            QMenu {{
                background: {COLORS['surface2']};
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
            }}
            QMenu::item:selected {{ background: {COLORS['accent_dim']}; }}
            QSplitter::handle {{
                background: {COLORS['border']};
                width: 1px;
            }}
            QGroupBox {{
                border: 1px solid {COLORS['border']};
                border-radius: 6px;
                margin-top: 12px;
                padding-top: 8px;
                color: {COLORS['text_dim']};
                font-size: 10px;
                letter-spacing: 1px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
            }}
        """)

    def _build_ui(self):
        splitter = QSplitter(Qt.Horizontal)
        self.setCentralWidget(splitter)

        # ── Left: Sidebar ──────────────────────────────────────────
        sidebar_scroll = QScrollArea()
        sidebar_scroll.setWidgetResizable(True)
        sidebar_scroll.setFixedWidth(230)
        sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout(sidebar_widget)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(8)

        # Title
        title = QLabel("BEFEHLE")
        title.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 10px; letter-spacing: 2px; margin-bottom: 4px;")
        sidebar_layout.addWidget(title)

        for cat_name, cat_info in COMMANDS.items():
            group = QGroupBox(f"  {cat_info['icon']}  {cat_name}")
            group.setStyleSheet(f"""
                QGroupBox {{
                    border: 1px solid {cat_info['color']}44;
                    color: {cat_info['color']};
                    font-size: 10px;
                    letter-spacing: 1px;
                    font-weight: bold;
                }}
            """)
            glay = QVBoxLayout(group)
            glay.setContentsMargins(6, 8, 6, 6)
            glay.setSpacing(3)

            for cmd in cat_info["commands"]:
                item = SidebarItem(cmd, cat_name, cat_info["color"], cat_info["dim"], cat_info["icon"])
                glay.addWidget(item)

            sidebar_layout.addWidget(group)

        sidebar_layout.addStretch()
        sidebar_scroll.setWidget(sidebar_widget)
        sidebar_widget.setStyleSheet(f"background: {COLORS['surface']};")
        splitter.addWidget(sidebar_scroll)

        # ── Center: Canvas ─────────────────────────────────────────
        center = QWidget()
        center_layout = QVBoxLayout(center)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(0)

        canvas_header = QWidget()
        canvas_header.setFixedHeight(44)
        canvas_header.setStyleSheet(f"background: {COLORS['surface']}; border-bottom: 1px solid {COLORS['border']};")
        ch_layout = QHBoxLayout(canvas_header)
        ch_layout.setContentsMargins(16, 0, 16, 0)
        canvas_label = QLabel("SCRIPT CANVAS")
        canvas_label.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 10px; letter-spacing: 2px;")
        ch_layout.addWidget(canvas_label)
        ch_layout.addStretch()

        self.block_count_label = QLabel("0 Blöcke")
        self.block_count_label.setStyleSheet(f"color: {COLORS['accent']}; font-size: 11px;")
        ch_layout.addWidget(self.block_count_label)
        center_layout.addWidget(canvas_header)

        canvas_scroll = QScrollArea()
        canvas_scroll.setWidgetResizable(True)
        self.canvas = CanvasWidget()
        self.canvas.setStyleSheet(f"background: {COLORS['bg']};")
        self.canvas.blocks_changed.connect(self._on_blocks_changed)
        canvas_scroll.setWidget(self.canvas)
        center_layout.addWidget(canvas_scroll)
        splitter.addWidget(center)

        # ── Right: Preview ─────────────────────────────────────────
        right = QWidget()
        right.setFixedWidth(320)
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        preview_header = QWidget()
        preview_header.setFixedHeight(44)
        preview_header.setStyleSheet(f"background: {COLORS['surface']}; border-bottom: 1px solid {COLORS['border']};")
        ph_layout = QHBoxLayout(preview_header)
        ph_layout.setContentsMargins(16, 0, 16, 0)
        prev_label = QLabel("SCRIPT VORSCHAU")
        prev_label.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 10px; letter-spacing: 2px;")
        ph_layout.addWidget(prev_label)
        ph_layout.addStretch()

        self.fmt_combo = QComboBox()
        self.fmt_combo.addItems([".ashell", ".txt"])
        self.fmt_combo.setStyleSheet(f"""
            QComboBox {{
                background: {COLORS['surface2']};
                border: 1px solid {COLORS['border']};
                color: {COLORS['text']};
                padding: 3px 8px;
                border-radius: 3px;
                font-size: 11px;
            }}
            QComboBox::drop-down {{ border: none; width: 20px; }}
        """)
        self.fmt_combo.currentIndexChanged.connect(self._on_blocks_changed)
        ph_layout.addWidget(self.fmt_combo)
        right_layout.addWidget(preview_header)

        self.preview = QTextEdit()
        self.preview.setReadOnly(True)
        self.preview.setStyleSheet(f"""
            QTextEdit {{
                background: {COLORS['surface']};
                color: {COLORS['success']};
                border: none;
                font-family: 'Consolas', monospace;
                font-size: 12px;
                padding: 12px;
            }}
        """)
        right_layout.addWidget(self.preview)

        export_btn = QPushButton("  💾  Script exportieren")
        export_btn.setFixedHeight(44)
        export_btn.clicked.connect(self.export_script)
        export_btn.setStyleSheet(f"""
            QPushButton {{
                background: {COLORS['accent']};
                color: white;
                border: none;
                font-size: 13px;
                font-weight: bold;
                font-family: 'Consolas', monospace;
                border-radius: 0px;
            }}
            QPushButton:hover {{ background: #6fa0ff; }}
            QPushButton:pressed {{ background: {COLORS['accent_dim']}; }}
        """)
        right_layout.addWidget(export_btn)
        splitter.addWidget(right)

        splitter.setSizes([230, 650, 320])

        # Toolbar
        tb = self.addToolBar("Hauptleiste")
        tb.setMovable(False)
        tb.setIconSize(QSize(16, 16))

        def tb_btn(label, tooltip, slot):
            btn = QPushButton(label)
            btn.setToolTip(tooltip)
            btn.setFixedHeight(30)
            btn.clicked.connect(slot)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {COLORS['surface2']};
                    color: {COLORS['text']};
                    border: 1px solid {COLORS['border']};
                    border-radius: 4px;
                    padding: 0 14px;
                    font-size: 12px;
                    font-family: 'Consolas', monospace;
                }}
                QPushButton:hover {{
                    background: {COLORS['border']};
                    color: white;
                }}
            """)
            return btn

        tb.addWidget(tb_btn("  📂  Öffnen", "Projekt öffnen", self.open_project))
        tb.addWidget(tb_btn("  💾  Speichern", "Projekt speichern", self.save_project))
        tb.addSeparator()
        tb.addWidget(tb_btn("  🗑  Alle löschen", "Canvas leeren", self.clear_canvas))

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        tb.addWidget(spacer)

        self.status_lbl = QLabel("Bereit")
        tb.addWidget(self.status_lbl)

        self.setStatusBar(QStatusBar())

    def _build_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("Datei")
        file_menu.addAction("Öffnen", self.open_project, QKeySequence.Open)
        file_menu.addAction("Speichern", self.save_project, QKeySequence.Save)
        file_menu.addSeparator()
        file_menu.addAction("Script exportieren", self.export_script, "Ctrl+E")
        file_menu.addSeparator()
        file_menu.addAction("Beenden", self.close, QKeySequence.Quit)

        edit_menu = menu.addMenu("Bearbeiten")
        edit_menu.addAction("Alle löschen", self.clear_canvas)

    def _on_blocks_changed(self):
        n = len(self.canvas.blocks)
        self.block_count_label.setText(f"{n} Block{'e' if n != 1 else ''}")
        fmt = ".ashell" if self.fmt_combo.currentIndex() == 0 else ".txt"
        script = self.canvas.generate_script("ashell" if fmt == ".ashell" else "txt")
        self.preview.setPlainText(script)

    def clear_canvas(self):
        if self.canvas.blocks:
            reply = QMessageBox.question(self, "Löschen?", "Wirklich alle Blöcke löschen?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.canvas.clear_all()

    def save_project(self):
        path, _ = QFileDialog.getSaveFileName(self, "Projekt speichern", "", "AutoShell Projekt (*.ashproj)")
        if path:
            if not path.endswith(".ashproj"):
                path += ".ashproj"
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.canvas.to_json())
            self.statusBar().showMessage(f"Gespeichert: {path}", 3000)

    def open_project(self):
        path, _ = QFileDialog.getOpenFileName(self, "Projekt öffnen", "", "AutoShell Projekt (*.ashproj)")
        if path:
            with open(path, "r", encoding="utf-8") as f:
                self.canvas.load_json(f.read())
            self.statusBar().showMessage(f"Geöffnet: {path}", 3000)

    def export_script(self):
        fmt = ".ashell" if self.fmt_combo.currentIndex() == 0 else ".txt"
        ext = "ashell" if fmt == ".ashell" else "txt"
        path, _ = QFileDialog.getSaveFileName(
            self, "Script exportieren", f"script.{ext}",
            f"AutoShell Script (*.{ext})"
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.canvas.generate_script("ashell" if fmt == ".ashell" else "txt"))
            self.statusBar().showMessage(f"Exportiert: {path}", 3000)


# ─── Entry Point ──────────────────────────────────────────────────────────────
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("AutoShell Builder")

    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()