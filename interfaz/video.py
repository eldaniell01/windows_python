import typing
from pytube import YouTube
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox

class DownloadVideo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.video = uic.loadUi("interfaz/Download.ui")
        self.video.btndownload.clicked.connect(self.downloadVideo)
        self.video.show()
        
    def downloadVideo(self):
        link = self.video.texturl.text()
        download = YouTube(link)
        download = download.streams.get_by_itag(22)
        folder = QFileDialog()
        folder_path, _  = folder.getSaveFileName(None, "GUARDAR VIDEO", "", 'MP4 (*.mp4)')
        try: 
            download.download(folder_path)
            self.informativo = QMessageBox()
            self.informativo.information(None,"INFORMATIVO", "SE HA DESCARGADO EL VIDEO")
        except:
            self.error = QMessageBox()
            self.error.critical(None, "Error", "hay un error")
        