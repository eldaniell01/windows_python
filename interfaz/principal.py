import sys
import typing
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from interfaz.messages import Menssages
class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = uic.loadUi("interfaz/MainWindow.ui")
        self.main.show()
        self.main.mensaje.clicked.connect(self.openMessages)
    
    def openMessages(self):
        self.messages = Menssages()
        self.main.close()
        
    