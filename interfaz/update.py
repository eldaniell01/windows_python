import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from PyQt6.QtGui import QFont

class UpdateTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.update = uic.loadUi("interfaz/Update.ui")
        self.update.show()
        self.showData()
        self.update.btnactualizar.clicked.connect(self.updateData)
        self.update.return1.clicked.connect(self.regreso)
        
    def showData(self):
        columns = ['NOMBRE', 'APELLIDO', 'DIRECCION']
        datos = [
                ["daniel", "montepque", "centro dos"],
                ["carlily", "escobar", "linea c12"] 
                 ]
        self.update.table.setFont(QFont("Arial", 14))
        self.update.table.setColumnCount(len(columns))
        self.update.table.setRowCount(len(datos))
        for column, name in enumerate(columns):
            self.update.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))
        for row, names in enumerate(datos):
            for col, value in enumerate(names):
                self.update.table.setItem(row, col, QTableWidgetItem(value))
        self.update.table.resizeColumnsToContents()
    
    def updateData(self):
        
        self.name = self.update.tetxname.text()
        self.last_name = self.update.textlastname.text()
        self.direction = self.update.textdirection.text()
        self.id = int(self.update.id.text())
        self.update.table.removeRow(self.id-1)
        row = self.update.table.rowCount()
        self.update.table.insertRow(row)
        self.update.table.setItem(row, 0, QTableWidgetItem(self.name))
        self.update.table.setItem(row, 1, QTableWidgetItem(self.last_name))
        self.update.table.setItem(row, 2, QTableWidgetItem(self.direction))
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.update.close()