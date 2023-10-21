import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from db.conexion_database import ConexionMysql

class DataBase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conexion = uic.loadUi("interfaz/DataBase.ui")
        self.conexion.show()
        self.con = ConexionMysql()
        self.conexion.btndatabase.clicked.connect(self.connec)
        self.conexion.btnclose.clicked.connect(self.closeDataBase)
        self.conexion.return1.clicked.connect(self.regreso)
        
    def connec(self):
        texto = self.con.connection()
        self.conexion.lbdatabase.setText(texto)
        
    def closeDataBase(self):
        texto = self.con.close_connection()
        self.conexion.lbdatabase.setText(texto)
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.conexion.close()