import typing
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

class RouteFile(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ruta = uic.loadUi("interfaz/Rutas.ui")
        self.ruta.show()
        self.ruta.btnruta.clicked.connect(self.openRoute)
        self.ruta.return1.clicked.connect(self.regreso)
        
    def openRoute(self):
        self.archivo = QFileDialog()
        arch, arg = self.archivo.getOpenFileName(None,"archivo", "archivo")
        self.ruta.textruta.setText(arch)
        """folders:
        folder = self.archivo.getExistingDirectory(None, 'seleccionar carpeta', "")
        self.ruta.textruta.setText(folder)
        """
    
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.ruta.close()