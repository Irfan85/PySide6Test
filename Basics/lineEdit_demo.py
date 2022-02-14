import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LineEdit Demo")

        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(10)
        self.line_edit.setPlaceholderText("Enter text")
      
        self.line_edit.returnPressed.connect(self.on_return_pressed)
        self.line_edit.selectionChanged.connect(self.on_selection_changed)
        # This is trigerred when the text is edited by either the user 
        # or the program
        self.line_edit.textChanged.connect(self.on_text_changed)
        # This is trigerred when text is edited by the user        
        self.line_edit.textEdited.connect(self.on_text_edited)

        # We can also set input masks for the lineEdit to only allow specific
        # format of inputs for instance, IP addresses. The following mask allows
        # a total of 6 digits with a dot separating groups of three. Also, '_'
        # is used a a placeholder for the digits
        # self.line_edit.setInputMask("000.000;_")

        self.setCentralWidget(self.line_edit)

    def on_return_pressed(self):
        print("Enter pressed")

    def on_selection_changed(self):
        print(self.line_edit.selectedText())

    def on_text_changed(self, s):
        print("Text has been changed")
        print(s)

    def on_text_edited(self, s):
        print("Text has been edited")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()