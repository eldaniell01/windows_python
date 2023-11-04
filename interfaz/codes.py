import typing
import barcode
from barcode import Code128
from barcode.writer import ImageWriter
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from PIL import Image
from db.querys import Querys
from PyQt6 import QtCore, uic
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QFileDialog

class BarCode(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bcode = uic.loadUi("interfaz/Codigo_Barras.ui")
        self.bcode.show()
        self.bcode.btnlist.clicked.connect(self.languages)
        self.bcode.btnpdf.clicked.connect(self.get_bar_code)
        self.bcode.return1.clicked.connect(self.regreso)
        self.bcode.textlenguate.textChanged.connect(self.filterLanguages)
        self.showTable()
        
    def showTable(self):
        columns = ['ID', 'LENGUAJE ', 'FECHA Y HORA']
        self.bcode.table.setFont(QFont("Arial", 14))
        self.bcode.table.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.bcode.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))
    
    def languages(self):
        self.list = Querys()
        data = self.list.listLanguages()
        num_rows = len(data)
        self.bcode.table.setRowCount(num_rows)
        for fila, datos in enumerate(data):
            for columna, dato in enumerate(datos):
                self.bcode.table.setItem(fila, columna, QTableWidgetItem(str(dato)))
        self.bcode.table.resizeColumnsToContents()
        
    def get_data(self):
        select = self.bcode.table.selectionModel().selectedIndexes()
        if select:
            selected_data = [self.bcode.table.itemFromIndex(index).text() for index in select]
            return selected_data[0]
            
        else:
            print("No se ha seleccionado ningún dato.")
            
    def get_bar_code(self):
        data = self.get_data()
        bar_code = Code128(data, writer=ImageWriter())
        folder = QFileDialog()
        size = (188,140)
        path_save, __ = folder.getSaveFileName(None, 'GUARDAR IMAGEN', '', 'PNG (*.png)')
        bar_code.save(path_save)
        code = Image.open(f"{path_save}.png")
        code = code.resize(size)
        code.save(f"{path_save}.png")
        self.createpdf(path_save)
        
    def createpdf(self, path):
        template_dir = "views"
        pdf_file = f"{path}.pdf"
        img_path = f"{path}.png"
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template('barcode.html')
        html_content = template.render(img_paths=str(img_path))
        HTML(string=html_content).write_pdf(pdf_file)
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.bcode.close()
        
    def filterLanguages(self):
        texto = self.bcode.textlenguate.text().upper()
        for row in range(self.bcode.table.rowCount()):
            row_text=[self.bcode.table.item(row, col).text().upper() for col in range(self.bcode.table.columnCount())]
            if any(texto in text for text in row_text):
                self.bcode.table.setRowHidden(row, False)
            else:
                self.bcode.table.setRowHidden(row,True)
        
        
        