import typing
from datetime import datetime
from db.querys import Querys
from PyQt6 import QtCore, uic
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem

class QuerysDataBase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.consulta = uic.loadUi("interfaz/Consultas.ui")
        self.consulta.show()
        self.consulta.datetime.setDateTime(datetime.now())
        self.consulta.btninsert.clicked.connect(self.insert)
        self.consulta.btnlist.clicked.connect(self.languages)
        self.showTable()
        
    def showTable(self):
        columns = ['ID', 'LENGUAJE ', 'FECHA Y HORA']
        self.consulta.table.setFont(QFont("Arial", 14))
        self.consulta.table.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.consulta.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))    
        
    def insert(self):
        date = self.consulta.datetime.dateTime()
        language = self.consulta.textlanguage.text()
        self.insertdb= Querys()
        self.insertdb.insertLanguage(language,date.toPyDateTime())
        self.message = QMessageBox()
        self.message.information(None, "Guardado","se ha guardado")
        
    def languages(self):
        self.list = Querys()
        data = self.list.listLanguages()
        num_rows = len(data)
        self.consulta.table.setRowCount(num_rows)
        for fila, datos in enumerate(data):
            for columna, dato in enumerate(datos):
                self.consulta.table.setItem(fila, columna, QTableWidgetItem(str(dato)))
        
        self.consulta.table.resizeColumnsToContents()
        