import sys
import typing
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from .messages import Menssages
from .labels import TextLabels
from .textbox import TextBox
from .calculadora import Calculadora

class Windows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = uic.loadUi("interfaz/MainWindow.ui")
        self.main.show()
        self.main.mensaje.clicked.connect(self.openMessages)
        self.main.btnlabels.clicked.connect(self.openLabels)
        self.main.btntextbox.clicked.connect(self.openTextbox)
        self.main.btncalculadora.clicked.connect(self.openCalculadora)
    
    def openMessages(self):
        self.messages = Menssages()
        self.main.close()
    
    def openLabels(self):
        self.labels = TextLabels()
        self.main.close()
    
    def openTextbox(self):
        self.textbox = TextBox()
        self.main.close()
        
    def openCalculadora(self):
        self.calcu = Calculadora()
        self.main.close()