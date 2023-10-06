import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class OptionCombo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.option = uic.loadUi("interfaz/ComboBox.ui")
        self.option.show()
        self.option.btnopciones.clicked.connect(self.options)
        
    def options(self):
        elementos = ["opcion 1", "opcion 2", "opcion 3"]
        self.option.cbopciones.addItems(elementos)
