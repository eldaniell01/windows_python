import typing
from PIL import Image
from rembg import remove
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

class RemoveBG(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rembg = uic.loadUi("interfaz/Remove.ui")
        self.rembg.show()
        self.rembg.btnimg.clicked.connect(self.searchimg)
        self.rembg.btnremove.clicked.connect(self.removeBG)
        self.rembg.return1.clicked.connect(self.regreso)
        
    def searchimg(self):
        folder = QFileDialog()
        folder_path, __= folder.getOpenFileName(None, 'ABRIR IMAGEN', '', 'Todos los archivos (*)',)
        self.rembg.textimg.setText(folder_path)
        
        
    def removeBG(self):
        path = self.rembg.textimg.text()
        rem = Image.open(path)
        bg = remove(rem)
        folder = QFileDialog()
        path_save, __ = folder.getSaveFileName(None, 'GUARDAR IMAGEN', '', 'PNG (*.png)')
        bg.save(f"{path_save}.png")
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.rembg.close()