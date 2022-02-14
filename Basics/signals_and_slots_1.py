import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signal and slots")
        
        button = QPushButton("Click Me!")
        # This will keep it checked. Pressing again will un-check it
        button.setCheckable(True)
        
        button.clicked.connect(self.on_click_btn)
        # Some signal contain additional data with the event which can be
        # recieved by the slot as argument
        button.clicked.connect(self.on_toggle_btn)

        self.setCentralWidget(button)

    
    def on_click_btn(self):
        print("Clicked!")

    
    def on_toggle_btn(self, checked):
        print("Checked?: ", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


