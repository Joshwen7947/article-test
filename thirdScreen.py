from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instructions import *


class Final(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.initUI()
        self.show()
        
        
    def initUI(self):
        self.workout_text = QLabel(txt_workheart)
        self.index = QLabel(txt_index)
        
        self.master = QVBoxLayout()
        
        self.master.addWidget(self.workout_text, alignment=Qt.AlignCenter)
        self.master.addWidget(self.index, alignment=Qt.AlignCenter)
        
        self.setLayout(self.master)
        
        
    def appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(600, 400)
    
        
    
        
    