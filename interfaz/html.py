import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from bs4 import BeautifulSoup

class HTMLInsert(QMainWindow):
    def __init__(self):
        super().__init__()
        self.html = uic.loadUi("interfaz/HTML.ui")
        self.html.show()
        self.html.btnhtml.clicked.connect(self.insertHtml)
        self.html.return1.clicked.connect(self.regreso)
        
    def insertHtml(self):
        html_file = 'interfaz/plantilla.html'
        name = self.html.textname.text()
        lastname = self.html.textlastname.text()
        address = self.html.textaddress.text()
        data = [
            {"name": name, "lastname": lastname, "address": address}
        ]
        with open(html_file, 'r') as file:
            html = file.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        
        tbody = soup.find('tbody')
        for row in data:
            new_row = soup.new_tag('tr', style="height: 18px;")
            for key in ['name', 'lastname', 'address']:
                new_column = soup.new_tag('td', style="width: 33.3333%; text-align: center; height: 18px;")
                new_column.string = row[key]
                new_row.append(new_column)
            tbody.append(new_row)
        
        up = str(soup)
        with open(html_file, 'w') as updated_file:
            updated_file.write(up)
        print("archivo guardado")
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.html.close()