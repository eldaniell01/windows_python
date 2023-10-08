import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from PyQt6.QtGui import QFont

class InsertTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tinsert = uic.loadUi("interfaz/TablaInsert.ui")
        self.tinsert.show()
        self.showTable()
        self.elementos=[]
        self.tinsert.btntable.clicked.connect(self.insert)
        
    def showTable(self):
        columns = ['NOMBRE', 'APELLIDO', 'DIRECCION']
        self.tinsert.table.setFont(QFont("Arial", 14))
        self.tinsert.table.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.tinsert.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))    
        self.tinsert.table.resizeColumnsToContents()
        
    def insert(self):
        self.name = self.tinsert.texname.text()
        self.last_name = self.tinsert.textlastname.text()
        self.direction = self.tinsert.textdirection.text()
        row_count = self.tinsert.table.rowCount()
        self.tinsert.table.insertRow(row_count)
        self.tinsert.table.setItem(row_count, 0, QTableWidgetItem(self.name))
        self.tinsert.table.setItem(row_count, 1, QTableWidgetItem(self.last_name))
        self.tinsert.table.setItem(row_count, 2, QTableWidgetItem(self.direction))