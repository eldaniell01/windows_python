import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class TextBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textbox = uic.loadUi("interfaz/Textbox.ui")
        self.textbox.show()
        self.textbox.btnshow.clicked.connect(self.showMessage)
        self.textbox.return1.clicked.connect(self.regreso)
        
        
    def showMessage(self):
        self.texto = self.textbox.lineEdit.text()
        self.textbox.lineEdit.setText("")
        self.textbox.lbshow.setText(self.texto)
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.textbox.close()
    