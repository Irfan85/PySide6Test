import sys

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QLineEdit, 
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signal and Slots")

        self.label = QLabel()
        
        self.input = QLineEdit()
        # Some of the widgets have bulit in slots. This eliminates the need for
        # writing python functions of our own.
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



