import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QMessageBox

class Menssages(QMainWindow):
    def __init__(self):
        super().__init__()
        self.messages = uic.loadUi("interfaz/Messages.ui")
        self.messages.show()
        self.messages.info.clicked.connect(self.infoMessage)
        
    def infoMessage(self):
        self.mensaje = QMessageBox()
        self.mensaje.information(None,"informacion", "esto es un mensaje informativo")