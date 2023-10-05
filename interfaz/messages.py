import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QMessageBox, QFileDialog




class Menssages(QMainWindow):
    def __init__(self):
        super().__init__()
        self.messages = uic.loadUi("interfaz/Messages.ui")
        self.messages.show()
        self.messages.info.clicked.connect(self.infoMessage)
        self.messages.adve.clicked.connect(self.adveMessage)
        self.messages.error.clicked.connect(self.erroMessage)
        self.messages.file.clicked.connect(self.fileMessage)
        self.messages.return1.clicked.connect(self.regreso)
        
        
    def infoMessage(self):
        self.informativo = QMessageBox()
        self.informativo.information(None,"informacion", "esto es un mensaje informativo")
    
    def adveMessage(self):
        self.advertencia = QMessageBox()
        self.advertencia.warning(None, "peligro","esta es una advertencia")
    
    def erroMessage(self):
        self.error = QMessageBox()
        self.error.critical(None, "Error", "hay un error")
        
    def fileMessage(self):
        self.archivo = QFileDialog()
        self.archivo.getOpenFileName(None, "Abrir Archivo", "archivo")
    
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.messages.close()
  