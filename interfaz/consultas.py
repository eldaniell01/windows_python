import typing
import os
from datetime import datetime
from db.querys import Querys
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from PyQt6 import QtCore, uic
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QFileDialog

class QuerysDataBase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.consulta = uic.loadUi("interfaz/Consultas.ui")
        self.consulta.show()
        self.consulta.datetime.setDateTime(datetime.now())
        self.consulta.btninsert.clicked.connect(self.insert)
        self.consulta.btnlist.clicked.connect(self.languages)
        self.consulta.textlanguage.textChanged.connect(self.filterLanguages)
        self.consulta.btnupdate.clicked.connect(self.updateLanguages)
        self.consulta.btnpdf.clicked.connect(self.createPDF)
        
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
        
    def filterLanguages(self):
        texto = self.consulta.textlanguage.text().upper()
        for row in range(self.consulta.table.rowCount()):
            row_text=[self.consulta.table.item(row, col).text().upper() for col in range(self.consulta.table.columnCount())]
            if any(texto in text for text in row_text):
                self.consulta.table.setRowHidden(row, False)
            else:
                self.consulta.table.setRowHidden(row,True)
    
    def updateLanguages(self):
        id = int(self.consulta.textid.text())
        language = self.consulta.textlanguage.text()
        self.upd = Querys()
        self.upd.updateLanguges(language, id)
        self.message = QMessageBox()
        self.message.information(None, "Actualizacion","se ha actualizado")
        self.consulta.textlanguage.setText("")
        self.consulta.textid.setText("")
        self.languages()
        
    def createPDF(self):
        template_dir = "views"
        data =[]
        for row in range(self.consulta.table.rowCount()):
            if not self.consulta.table.isRowHidden(row):
                data_row ={
                    'id': self.consulta.table.item(row, 0).text(),
                    'language': self.consulta.table.item(row, 1).text(),
                    'date':self.consulta.table.item(row, 2).text()
                }
                data.append(data_row)
        folder = QFileDialog()
        folder_path, __= folder.getSaveFileName(None, 'GUARDAR PDF', '', 'PDF (*.pdf)',)
        pdf_file = f"{folder_path}.pdf"
        context = {'languages': data}
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template('plantilla.html')
        html_content = template.render(context)
        HTML(string=html_content).write_pdf(pdf_file)
        
        