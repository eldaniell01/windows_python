import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QFont

class FilterTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filter = uic.loadUi("interfaz/Filter.ui")
        self.filter.show()
        self.showData()
        self.filter.return1.clicked.connect(self.regreso)
        self.filter.textfilter.textChanged.connect(self.filterData)
        
    def showData(self):
        columns = ['NOMBRE', 'APELLIDO', 'DIRECCION']
        datos = [
                ["daniel", "montepque", "centro dos"],
                ["carlily", "escobar", "linea c12"] 
                 ]
        self.filter.table.setFont(QFont("Arial", 14))
        self.filter.table.setColumnCount(len(columns))
        self.filter.table.setRowCount(len(datos))
        for column, name in enumerate(columns):
            self.filter.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))
        for row, names in enumerate(datos):
            for col, value in enumerate(names):
                self.filter.table.setItem(row, col, QTableWidgetItem(value))
        self.filter.table.resizeColumnsToContents()
    
    def filterData(self):
        filtrar = self.filter.textfilter.text().upper()
        for row in range(self.filter.table.rowCount()):
            row_text=[self.filter.table.item(row, col).text().upper() for col in range(self.filter.table.columnCount())]
            print(row_text)
            if any(filtrar in text for text in row_text):
                self.filter.table.setRowHidden(row, False)
            else:
                self.filter.table.setRowHidden(row,True)
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.filter.close()