import sys
from PyQt6.QtWidgets import (QWidget, QMainWindow, QToolTip, QPushButton, QApplication, QMessageBox, QMenu, QTextEdit,
                             QHBoxLayout, QVBoxLayout, QLabel)

import morseCodeSolver as morse


def main():
    solver = morse.MorseCodeSolver("felicitare_Fane_morse.txt", "felicitare_Fane_RO.txt")
    solver.decode_morse_text([], "", 0)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        OK = QPushButton("OK")
        Cancel = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(OK)
        hbox.addWidget(Cancel)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(350, 350, 400, 200)
        self.setWindowTitle("Test")
        self.show()


def qt_sandbox():
    application = QApplication(sys.argv)
    widget = Example()
    sys.exit(application.exec())


if __name__ == "__main__":
    # main()
    qt_sandbox()
