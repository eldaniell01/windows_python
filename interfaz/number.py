import typing
import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class LocationNumber(QMainWindow):
    def __init__(self):
        super().__init__()
        self.location = uic.loadUi("interfaz/Location.ui")
        self.location.btnlocation.clicked.connect(self.phoneLocation)
        self.location.show()
       
    def phoneLocation(self):
        key = 'cfa5a49db47748398dc9599a33bfe06f'
        code = OpenCageGeocode(key, 'http')
        number = phonenumbers.parse(self.location.textlocation.text())
        traking = geocoder.description_for_number(number, 'es',)
        query = str(traking)
        result = code.geocode(query)
        print(code)
        self.location.location.setText(f"{result[0]['geometry']['lat']},{result[0]['geometry']['lng']}")
        

