import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont

class DeleteTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.delT = uic.loadUi("interfaz/Delete.ui")
        self.delT.show()
        self.showData()
        self.delT.btndelete.clicked.connect(self.delete)
        self.delT.return1.clicked.connect(self.regreso)
    
    def showData(self):
        columns = ['NOMBRE', 'APELLIDO', 'DIRECCION']
        datos = [
                ["daniel", "montepque", "centro dos"],
                ["carlily", "escobar", "linea c12"] 
                 ]
        self.delT.table.setFont(QFont("Arial", 14))
        self.delT.table.setColumnCount(len(columns))
        self.delT.table.setRowCount(len(datos))
        for column, name in enumerate(columns):
            self.delT.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))
        for row, names in enumerate(datos):
            for col, value in enumerate(names):
                self.delT.table.setItem(row, col, QTableWidgetItem(value))
        self.delT.table.resizeColumnsToContents()
    
    def delete(self):
        self.id = int(self.delT.textid.text())
        self.delT.table.removeRow(self.id-1)
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.delT.close()