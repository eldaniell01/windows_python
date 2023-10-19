import sys
import typing
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from .messages import Menssages
from .labels import TextLabels
from .textbox import TextBox
from .calculadora import Calculadora
from .datet import DateT
from .opciones import OptionCombo
from .radiob import RadioButton
from .table import Table
from .tabla_insert import InsertTable
from .update import UpdateTable
from .delete import DeleteTable
from .filter import FilterTable
from .password import PasswordSecurity
from .rutas import RouteFile
from .html import HTMLInsert


class Windows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = uic.loadUi("interfaz/MainWindow.ui")
        self.main.show()
        self.main.btntextbox.clicked.connect(self.openTextbox)
        self.main.btncalculadora.clicked.connect(self.openCalculadora)
        self.main.btndate.clicked.connect(self.openCalendar)
        self.main.btnopciones.clicked.connect(self.openComboBox)
        self.main.btnrbutton.clicked.connect(self.openRadioButton)
        self.main.btntabla.clicked.connect(self.openTable)
        self.main.btntable2.clicked.connect(self.openInsertTable)
        self.main.btnupdate.clicked.connect(self.openUpdateTable)
        self.main.btndelete.clicked.connect(self.openDeleteTable)
        self.main.btnfilter.clicked.connect(self.openFilter)
        self.main.btnpassword.clicked.connect(self.openPassword)
        self.main.btnruta.clicked.connect(self.openRoutes)
        self.main.btnhtml.clicked.connect(self.openHTML)
    
    def openMessages(self):
        self.messages = Menssages()
        self.main.close()
    
    def openLabels(self):
        self.labels = TextLabels()
        self.main.close()
    
    def openTextbox(self):
        self.textbox = TextBox()
        self.main.close()
        
    def openCalculadora(self):
        self.calcu = Calculadora()
        self.main.close()
    
    def openCalendar(self):
        self.date = DateT()
        self.main.close()
        
    def openComboBox(self):
        self.option = OptionCombo()
        self.main.close()
    
    def openRadioButton(sefl):
        sefl.rbutton = RadioButton()
        sefl.main.close()
    
    def openTable(sefl):
        sefl.tab = Table()
        sefl.main.close()
        
    def openInsertTable(sefl):
        sefl.insert = InsertTable()
        sefl.main.close()
        
    def openUpdateTable(self):
        self.update = UpdateTable()
        self.main.close()
        
    def openDeleteTable(self):
        self.delete = DeleteTable()
        self.main.close()
        
    def openFilter(self):
        self.filter = FilterTable()
        self.main.close()
    
    def openPassword(self):
        self.password = PasswordSecurity()
        self.main.close()
        
    def openRoutes(self):
        self.ruta = RouteFile()
        self.main.close()
        
    def openHTML(self):
        self.html = HTMLInsert()
        self.main.close()