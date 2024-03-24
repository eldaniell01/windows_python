from PyQt6 import QtCore, uic
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QFileDialog

import xml.etree.ElementTree as ET

class FileXML(QMainWindow):
    def __init__(self):
        super().__init__()
        self.xml = uic.loadUi("interfaz/filexml.ui")
        self.xml.show()
        self.xml.btncreate.clicked.connect(self.createXML)
        
    def createXML(self):
        root = ET.Element('libros')
        libros = [
            {"id": "1", "titulo": "El señor de los anillos", "autor": "J.R.R. Tolkien"},
            {"id": "2", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
            {"id": "3", "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"}
        ]
        for lib in libros:
            libro = ET.SubElement(root, 'libro')
            id_libro = ET.SubElement(libro, 'id')
            id_libro.text = lib['id']
            titulo = ET.SubElement(libro,'titulo')
            titulo.text = lib['titulo']
            autor = ET.SubElement(libro, 'autor')
            autor.text = lib['autor']
        
        tree = ET.ElementTree(root)
        tree.write('libroXML.xml')
            