import typing
from PIL import Image
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

class ImgConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.converter = uic.loadUi("interfaz/ConvertidorIMG.ui")
        self.converter.btnsearch.clicked.connect(self.searchIMG)
        self.converter.btnjpg.clicked.connect(self.imgJPEG)
        self.converter.btnpng.clicked.connect(self.imgPNG)
        self.converter.btnwebp.clicked.connect(self.imgWEBP)
        self.converter.btngif.clicked.connect(self.imgGIF)
        self.converter.return1.clicked.connect(self.regreso)
        self.converter.show()
        
    def searchIMG(self):
        folder = QFileDialog()
        folder_path, __= folder.getOpenFileName(None, 'ABRIR IMAGEN', '', 'Todos los archivos (*)',)
        self.converter.textimg.setText(folder_path)

    def imgJPEG(self):
        img = self.converter.textimg.text()
        path_img = Image.open(img)
        folder = QFileDialog()
        path, __ = folder.getSaveFileName(None, 'GUARDAR IMAGEN', '', 'JPEG (*.jpg)')
        path_img.save(f"{path}.jpg")
        
    def imgPNG(self):
        img = self.converter.textimg.text()
        path_img = Image.open(img)
        folder = QFileDialog()
        path, __ = folder.getSaveFileName(None, 'GUARDAR IMAGEN', '', 'PNG (*.png)')
        path_img.save(f"{path}.png")
        
    def imgWEBP(self):
        img = self.converter.textimg.text()
        path_img = Image.open(img)
        folder = QFileDialog()
        path, __ = folder.getSaveFileName(None, 'GUARDAR IMAGEN', '', 'WEBP (*.webp)')
        path_img.save(f"{path}.webp")
        
    def imgGIF(self):
        img = self.converter.textimg.text()
        path_img = Image.open(img)
        folder = QFileDialog()
        path, __ = folder.getSaveFileName(None, 'GUARDAR IMAGEN', '', 'GIF (*.gif)')
        path_img.save(f"{path}.gif")
        
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.converter.close()