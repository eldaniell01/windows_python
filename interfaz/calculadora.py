import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculadora = uic.loadUi("interfaz/calculadora.ui")
        self.calculadora.show()
        self.calculadora.btnsumar.clicked.connect(self.sumar)
        self.calculadora.return1.clicked.connect(self.regreso)
        
    def sumar(self):
        self.calculadora.lbresul.setText(str(int(self.calculadora.num1.text())+int(self.calculadora.num2.text())))
        self.calculadora.num1.setText("")
        self.calculadora.num2.setText("")
    
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.calculadora.close()