import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Label Demo")

        # We already know labels contain text but they can also contain
        # images. Images are represented as QPixmap object in QT which is an
        # array of pixels 
        label = QLabel()
        label.setPixmap(QPixmap("owl.jpg"))
        # The Image maintains aspect ratio by default. Setting this to
        # true disables that and allows the image to stretch with the window
        label.setScaledContents(True)
        
        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()