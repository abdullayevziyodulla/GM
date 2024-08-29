from PyQt5.QtWidgets import *
from test2 import Oyna2  # Importing the Oyna2 class

class Oyna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.move(1200, 100)
        self.btn = QPushButton("Click me", self)
        self.btn.move(100, 50)
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        self.hide()  # Hide the current window
        self.new_window = Oyna2()  # Create the Oyna2 window
        self.new_window.show()  # Show the new window

app = QApplication([])
win = Oyna()
win.show()
app.exec_()
