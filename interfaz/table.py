import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont

class Table(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tab = uic.loadUi("interfaz/Table.ui")
        self.tab.show()
        self.tab.btntabla.clicked.connect(self.showTable)
        self.tab.return1.clicked.connect(self.regreso)
        
    def showTable(self):
        columns = ['NOMBRE', 'APELLIDO', 'DIRECCION']
        self.tab.table.setFont(QFont("Arial", 14))
        self.tab.table.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.tab.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))    
        self.tab.table.resizeColumnsToContents()
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.tab.close()