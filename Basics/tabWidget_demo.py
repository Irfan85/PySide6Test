import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget
)

from color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TabWidget Demo")

        tab_widget = QTabWidget()
        tab_widget.setTabPosition(QTabWidget.West)
        tab_widget.setMovable(True)
        # Only for macOS. This has no effect on other platforms
        tab_widget.setDocumentMode(True)

        for i, color in enumerate(["red", "green", "blue", "yellow"]):
            tab_widget.addTab(Color(color), color)

        self.setCentralWidget(tab_widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()