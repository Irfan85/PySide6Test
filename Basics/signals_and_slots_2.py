import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_checked = True

        self.setWindowTitle("Signal and slots")

        button = QPushButton("Click me!")
        button.setCheckable(True)
        button.setChecked(self.button_checked)
        button.clicked.connect(self.on_button_toggle)

        self.setCentralWidget(button)

    def on_button_toggle(self, checked):
        self.button_checked = checked

        print(self.button_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()