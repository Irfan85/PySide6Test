import sys

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout,
    QWidget
)

from color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VboxLayout Demo")

        red_color = Color("red")
        green_color = Color("green")
        blue_color = Color("blue")

        layout = QVBoxLayout()
        layout.addWidget(red_color)
        layout.addWidget(green_color)
        layout.addWidget(blue_color)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
