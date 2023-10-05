import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class TextLabels(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = uic.loadUi("interfaz/TextLabel.ui")
        self.text.show()
        self.text.message1.clicked.connect(self.showMessage1)
        self.text.message2.clicked.connect(self.showMessage2)
        self.text.return1.clicked.connect(self.regreso)
        
    def showMessage1(self):
        self.text.textLabel.setText("mensaje 1")
    
    def showMessage2(self):
        self.text.textLabel.setText("mensaje 2")
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.text.close()