import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
    "My Application",
    "Still My Application",
    "Again My Application"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title_index = 0

        self.setWindowTitle(window_titles[self.title_index])
        self.windowTitleChanged.connect(self.on_window_title_changed)

        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.on_click_button)

        self.setCentralWidget(self.button)

    def on_click_button(self):
        print("Clicked")
        
        self.title_index += 1
        self.title_index %= len(window_titles)
        new_window_title = window_titles[self.title_index]
        self.setWindowTitle(new_window_title)

    def on_window_title_changed(self):
        print("Window title changed: ", window_titles[self.title_index])


app = QApplication()

window = MainWindow()
window.show()

app.exec()