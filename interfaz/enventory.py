import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class Inventory(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inventory = uic.loadUi("interfaz/Inventario.ui")
        self.inventory.show()