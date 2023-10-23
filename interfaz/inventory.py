import typing
from db.querys import Querys
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt6.QtGui import QFont
class Inventory(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inventory = uic.loadUi("interfaz/Inventario.ui")
        self.inventory.show()
        self.inventory.btninventory.clicked.connect(self.showInventory)
        self.inventory.store1.toggled.connect(self.store1)
        self.inventory.store2.toggled.connect(self.store2)
        self.inventory.textsearch.textChanged.connect(self.filtertext)
        self.inventory.btnpdf.clicked.connect(self.pdfTemplate1)
        self.inventory.btnpdf_2.clicked.connect(self.pdfTemplate2)
        self.inventory.return1.clicked.connect(self.regreso)
        self.options =[]
        self.showTable()
        self.optionsInventory()
    
    def showTable(self):
        columns = ['PELICULA ', 'TIENDA', 'FECHA']
        self.inventory.table.setFont(QFont("Arial", 14))
        self.inventory.table.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.inventory.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))
    
    def showInventory(self):
        self.listinventory = Querys()
        data = self.listinventory.listInventory()
        num_row = len(data)
        self.inventory.table.setRowCount(num_row)
        for row, datos in enumerate(data):
            for column, dato in enumerate(datos):
                self.inventory.table.setItem(row, column, QTableWidgetItem(str(dato)))
                
        self.inventory.table.resizeColumnsToContents()
        
        
    def optionsInventory(self):
        self.listinventory = Querys()
        options = set(self.options)
        data = self.listinventory.listFilm()
        for row, datos in enumerate(data):
            options.add(str(datos[0]))
        lista = list(options)
        lista.sort()
        self.inventory.options.addItems(lista)
    
    def store1(self):
        if self.inventory.store1.isChecked():
            self.store = Querys()
            data = self.store.listStore1()
            num_row = len(data)
            self.inventory.table.setRowCount(num_row)
            for row, datos in enumerate(data):
                for column, dato in enumerate(datos):
                    self.inventory.table.setItem(row, column, QTableWidgetItem(str(dato)))
                    
            self.inventory.table.resizeColumnsToContents()
    
    def store2(self):
        if self.inventory.store2.isChecked():
            self.store = Querys()
            data = self.store.listStore2()
            num_row = len(data)
            self.inventory.table.setRowCount(num_row)
            for row, datos in enumerate(data):
                for column, dato in enumerate(datos):
                    self.inventory.table.setItem(row, column, QTableWidgetItem(str(dato)))
                    
            self.inventory.table.resizeColumnsToContents()
    
    def filtertext(self):
        texto = self.inventory.textsearch.text().upper()
        for row in range(self.inventory.table.rowCount()):
            row_text=[self.inventory.table.item(row, col).text().upper() for col in range(self.inventory.table.columnCount())]
            if any(texto in text for text in row_text):
                self.inventory.table.setRowHidden(row, False)
            else:
                self.inventory.table.setRowHidden(row,True)
    
    def pdfTemplate1(self):
        if self.inventory.table.rowCount()!=0:
            template_dir = "views"
            data = []
            num = 0
            for row in range(self.inventory.table.rowCount()):
                if not self.inventory.table.isRowHidden(row):
                    num = num +1
                    data_row ={
                        'id': str(num),
                        'film': self.inventory.table.item(row, 0).text(),
                        'store': self.inventory.table.item(row, 1).text(),
                        'date': self.inventory.table.item(row, 2).text()
                    }
                    data.append(data_row)
            folder = QFileDialog
            folder_path, _ = folder.getSaveFileName(None,'GUARDAR PDF', '', 'PDF (*.pdf)',)
            pdf_file = f"{folder_path}.pdf"
            context = {'films': data}
            
            env = Environment(loader=FileSystemLoader(template_dir))
            template = env.get_template('inventario.html')
            html_content = template.render(context)
            HTML(string=html_content).write_pdf(pdf_file)
        else:
            self.error = QMessageBox()
            self.error.critical(None, "Error", "no se esta mostrando datos en la tabla")
            
    def pdfTemplate2(self):
        self.summary = Querys()
        summary = self.summary.summary()                 
        template_dir = "views"
        data = []
        total1 = 0
        total2 = 0
        for row, datos in enumerate(summary):
            total1 += datos[2]
            total2 += datos[3]
            data_row ={
                'num': str(datos[0]),
                'film': str(datos[1]),
                'store1': str(datos[2]),
                'store2': str(datos[3])
            }
            data.append(data_row)
        folder = QFileDialog
        folder_path, _ = folder.getSaveFileName(None,'GUARDAR PDF', '', 'PDF (*.pdf)',)
        pdf_file = f"{folder_path}.pdf"
        context = {'films': data,
                    'total1': total1,
                    'total2': total2,       
            }
        
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template('resumen.html')
        html_content = template.render(context)
        HTML(string=html_content).write_pdf(pdf_file)
    
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.inventory.close()