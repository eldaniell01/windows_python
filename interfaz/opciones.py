import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class OptionCombo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.option = uic.loadUi("interfaz/ComboBox.ui")
        self.option.show()
        self.option.btnopciones.clicked.connect(self.options)
        self.elementos = []
        self.option.return1.clicked.connect(self.regreso)
        
    def options(self):
        lista = set(self.elementos)
        lista.add(str(self.option.textopciones.text()))
        self.option.cbopciones.addItems(list(lista))

    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.option.close()