from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instructions import *
from secondScreen import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        # Call all methods here
        self.initUI()
        self.connects()
        self.appear()
        self.show()
        
        
    def initUI(self):
        self.btn = QPushButton(txt_next)
        self.welcome = QLabel(txt_hello)
        self.instructions = QLabel(txt_instruction)
            
        self.master = QVBoxLayout()
        self.master.addWidget(self.welcome, alignment=Qt.AlignCenter)
        self.master.addWidget(self.instructions, alignment=Qt.AlignCenter)
        self.master.addWidget(self.btn, alignment=Qt.AlignCenter)
            
        self.setLayout(self.master)
            
        
    def next_click(self):
        self.second_window = SecondScreen()
        self.hide()
        
    def connects(self):
        self.btn.clicked.connect(self.next_click)
    
    def appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        
        
if __name__ in "__main__":
    app = QApplication([])
    main = Main()
    app.exec_()

    