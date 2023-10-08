import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class RadioButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rbutton = uic.loadUi("interfaz/Radiobutton.ui")
        self.rbutton.show()
        self.rbutton.btnrbutton.clicked.connect(self.selection)
        self.rbutton.return1.clicked.connect(self.regreso)
    
    def selection(self):
        if self.rbutton.rbutton.isChecked():
            self.rbutton.lbrbutton.setText("seleccionado")
        else:
            self.rbutton.lbrbutton.setText("no seleccionado")

    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.rbutton.close()