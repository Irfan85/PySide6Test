import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)

from color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nesting Layouts Demo")

        
        vBoxLayout1 = QVBoxLayout()
        vBoxLayout1.addWidget(Color("red"))
        vBoxLayout1.addWidget(Color("green"))
        vBoxLayout1.addWidget(Color("blue"))

        vBoxLayout2 = QVBoxLayout()
        vBoxLayout2.addWidget(Color("yellow"))
        vBoxLayout2.addWidget(Color("purple"))

        hBoxLayout = QHBoxLayout()
        hBoxLayout.addLayout(vBoxLayout1)
        hBoxLayout.addWidget(Color("teal"))
        hBoxLayout.addLayout(vBoxLayout2)

        # This will put zero margin in every direction around the
        # layout components
        hBoxLayout.setContentsMargins(0, 0, 0, 0)

        # This will set the spacing between the elements to 20
        hBoxLayout.setSpacing(20)


        widget = QWidget()
        widget.setLayout(hBoxLayout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
