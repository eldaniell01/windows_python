from PyQt6 import QtCore, uic
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QFileDialog
import xml.etree.ElementTree as ET
class Txml(QMainWindow):
    def __init__(self):
        super().__init__()
        self.txml = uic.loadUi('interfaz/Txml.ui')
        self.txml.show()
        self.showTable()
        self.txml.btninsert.clicked.connect(self.insert)
        self.txml.btncreate.clicked.connect(self.createXML)
    
    def showTable(self):
        columns = ['NOMBRE', 'APELLIDO', 'DIRECCION']
        self.txml.table.setFont(QFont("Arial", 14))
        self.txml.table.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.txml.table.setHorizontalHeaderItem(column, QTableWidgetItem(name))    
        self.txml.table.resizeColumnsToContents()
    
    def insert(self):
        self.name = self.txml.txtname.text()
        self.last_name = self.txml.txtlastname.text()
        self.address = self.txml.txtaddress.text()
        row_count = self.txml.table.rowCount()
        self.txml.table.insertRow(row_count)
        self.txml.table.setItem(row_count, 0, QTableWidgetItem(self.name))
        self.txml.table.setItem(row_count, 1, QTableWidgetItem(self.last_name))
        self.txml.table.setItem(row_count, 2, QTableWidgetItem(self.address))
    
    def createXML(self):
        if self.txml.table.rowCount()!=0:
            num = 0
            data = []
            for row in range(self.txml.table.rowCount()):
                if not self.txml.table.isRowHidden(row):
                    num = num+1
                    data_row ={
                        'id': str(num),
                        'name': self.txml.table.item(row, 0).text(),
                        'lastname': self.txml.table.item(row,1).text(),
                        'address': self.txml.table.item(row,2).text()
                    }
                    data.append(data_row)
            
            root = ET.Element('personas')
            for people in data:
                person = ET.SubElement(root,'persona')
                id_person = ET.SubElement(person, 'id')
                id_person.text = people['id']
                name = ET.SubElement(person,'name')
                name.text = people['name']
                lastname = ET.SubElement(person, 'lastname')
                lastname.text = people['lastname']
                address = ET.SubElement(person, 'address')
                address.text = people['address']
                
            tree = ET.ElementTree(root)
            tree.write('personaXML.xml')