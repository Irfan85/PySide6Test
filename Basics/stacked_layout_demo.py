import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QStackedLayout,
    QPushButton,
    QWidget
)

from color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stacked Layout Demo")

        button_layout = QHBoxLayout()
        
        button_red = QPushButton("Red")
        button_red.clicked.connect(self.show_tab_red)
        button_layout.addWidget(button_red)
        
        button_green = QPushButton("Green")
        button_green.clicked.connect(self.show_tab_green)
        button_layout.addWidget(button_green)

        button_blue = QPushButton("blue")
        button_blue.clicked.connect(self.show_tab_blue)
        button_layout.addWidget(button_blue)

        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(Color("red"))
        self.stack_layout.addWidget(Color("green"))
        self.stack_layout.addWidget(Color("blue"))
        self.stack_layout.setCurrentIndex(0)

        layout = QVBoxLayout()
        layout.addLayout(button_layout)
        layout.addLayout(self.stack_layout)

        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

    def show_tab_red(self):
        self.stack_layout.setCurrentIndex(0)

    def show_tab_green(self):
        self.stack_layout.setCurrentIndex(1)

    def show_tab_blue(self):
        self.stack_layout.setCurrentIndex(2)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
