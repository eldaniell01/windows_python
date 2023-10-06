import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from datetime import datetime

class DateT(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dtime = uic.loadUi("interfaz/Fecha.ui")
        self.dtime.show()
        self.dtime.dtdate.setDate(datetime.now().date())
        self.dtime.btnfecha.clicked.connect(self.showDate)
        self.dtime.return1.clicked.connect(self.regreso)
    
    def showDate(self):
        self.fecha = self.dtime.dtdate.date()
        self.dtime.lbfecha.setText(self.fecha.toString("dd-MM-yyyy"))
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.dtime.close()