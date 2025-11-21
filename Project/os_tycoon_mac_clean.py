import sys, random
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QGraphicsOpacityEffect
)

class GlassPanel(QWidget):
    """Simple glass-like transparent panel (no blur, no QPainter conflict)."""
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 18px;
        """)


class GlassButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFont(QFont("Arial", 12))
        self.setFixedHeight(42)
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.18);
                color: #FFFFFF;
                border-radius: 12px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.28);
            }
        """)


class OSTycoonGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OS Tycoon — macOS Minimal Clean UI")
        self.resize(950, 600)

        # Background: macOS style gradient
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1A1A1A,
                    stop:1 #000000
                );
            }
        """)

        # Game State
        self.state = {
            "money": 1000,
            "users": 10,
            "reputation": 50,
            "kernel_level": 1,
            "devs": 1,
            "servers": 1,
            "day": 1,
        }

        root = QVBoxLayout()

        # Title
        title = QLabel("OS COMPANY TYCOON")
        title.setFont(QFont("Arial", 28, QFont.Bold))
        title.setStyleSheet("color: white; margin-top: 15px;")
        title.setAlignment(Qt.AlignCenter)
        root.addWidget(title)

        # Day
        self.day_label = QLabel(f"Day: {self.state['day']}")
        self.day_label.setFont(QFont("Arial", 16))
        self.day_label.setStyleSheet("color: #ccc; margin-bottom: 20px;")
        self.day_label.setAlignment(Qt.AlignCenter)
        root.addWidget(self.day_label)

        # Middle Layout
        middle = QHBoxLayout()

        # Stats Panel
        self.stats_panel = GlassPanel()
        stats_layout = QVBoxLayout()
        self.stats_labels = {}

        for stat in self.state:
            if stat != "day":
                lbl = QLabel(f"{stat.title()}: {self.state[stat]}")
                lbl.setFont(QFont("Arial", 14))
                lbl.setStyleSheet("color: #FFFFFF; margin: 6px;")
                stats_layout.addWidget(lbl)
                self.stats_labels[stat] = lbl

        self.stats_panel.setLayout(stats_layout)
        middle.addWidget(self.stats_panel, 2)

        # Action Buttons
        self.actions_panel = GlassPanel()
        actions_layout = QVBoxLayout()

        self.btn_kernel = GlassButton("Improve Kernel")
        self.btn_dev = GlassButton("Hire Developer")
        self.btn_server = GlassButton("Buy Server")
        self.btn_market = GlassButton("Market OS")
        self.btn_next = GlassButton("Next Day")

        for btn in [
            self.btn_kernel, self.btn_dev, self.btn_server,
            self.btn_market, self.btn_next
        ]:
            actions_layout.addWidget(btn)

        self.actions_panel.setLayout(actions_layout)
        middle.addWidget(self.actions_panel, 2)

        root.addLayout(middle)

        # Log Panel
        self.log_panel = GlassPanel()
        log_layout = QVBoxLayout()

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setStyleSheet("""
            QTextEdit {
                background: transparent;
                color: white;
                font-size: 13px;
                font-family: Consolas;
                padding: 6px;
            }
        """)

        log_layout.addWidget(self.log_box)
        self.log_panel.setLayout(log_layout)
        root.addWidget(self.log_panel, 3)

        # Button connections
        self.btn_kernel.clicked.connect(self.improve_kernel)
        self.btn_dev.clicked.connect(self.hire_dev)
        self.btn_server.clicked.connect(self.buy_server)
        self.btn_market.clicked.connect(self.market)
        self.btn_next.clicked.connect(self.next_day)

        self.setLayout(root)
        self.fade_in()

    # Fade in animation
    def fade_in(self):
        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)

        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(800)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.start()

    # Logging
    def log(self, msg):
        self.log_box.append(msg)

    # Updating Stats
    def update_stats(self):
        for stat in self.state:
            if stat != "day":
                self.stats_labels[stat].setText(f"{stat.title()}: {self.state[stat]}")
        self.day_label.setText(f"Day: {self.state['day']}")

    # Actions
    def improve_kernel(self):
        cost = 300 + self.state["kernel_level"] * 100
        if self.state["money"] >= cost:
            self.state["money"] -= cost
            self.state["kernel_level"] += 1
            self.log("🧠 Kernel upgraded!")
            self.update_stats()

    def hire_dev(self):
        if self.state["money"] >= 500:
            self.state["money"] -= 500
            self.state["devs"] += 1
            self.log("👨‍💻 Developer hired!")
            self.update_stats()

    def buy_server(self):
        if self.state["money"] >= 400:
            self.state["money"] -= 400
            self.state["servers"] += 1
            self.log("🖥️ Server upgraded!")
            self.update_stats()

    def market(self):
        if self.state["money"] >= 200:
            self.state["money"] -= 200
            gain = random.randint(5, 30)
            self.state["users"] += gain
            self.log(f"📢 Marketing boost: +{gain} users")
            self.update_stats()

    def next_day(self):
        growth = self.state["kernel_level"] * 2 + self.state["devs"] * 3
        cap = self.state["servers"] * 100 + 50
        self.state["users"] = min(self.state["users"] + growth, cap)

        roll = random.random()
        if roll < 0.1:
            loss = random.randint(5, 20)
            self.state["users"] -= loss
            self.log(f"🐞 Bug! Lost {loss} users")
        elif roll < 0.2:
            gain = random.randint(10, 40)
            self.state["users"] += gain
            self.log(f"🔥 Viral review! +{gain} users")

        income = self.state["users"] // 2
        self.state["money"] += income
        self.log(f"💵 Earned ₹{income}")

        self.state["day"] += 1
        self.update_stats()


# Run App
app = QApplication(sys.argv)
window = OSTycoonGUI()
window.show()
sys.exit(app.exec())
