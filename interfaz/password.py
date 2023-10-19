import typing
import hashlib
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class PasswordSecurity(QMainWindow):
    def __init__(self):
        super().__init__()
        self.passw = uic.loadUi("interfaz/Password.ui")
        self.passw.show()
        self.passw.textpassword.textChanged.connect(self.write)
        self.passw.btncifrar.clicked.connect(self.encodeText)
        self.passw.btndecifrar.clicked.connect(self.decodeText)
        self.passw.return1.clicked.connect(self.regreso)
        
    def write(self):
        texto = self.passw.textpassword.text()
        print(texto)
        
    def encodeText(self):
        self.passw.lbpassword.setText(hashlib.sha256(self.passw.textpassword.text().encode()).hexdigest())
    
    def decodeText(self):
        password1 = self.passw.lbpassword.text()
        password2 = hashlib.sha256(self.passw.textpassword.text().encode()).hexdigest()
        
        if password1 == password2:
            self.passw.lbpassword.setText("es igual")
        else:
            self.passw.lbpassword.setText("no es igual")
    
    def regreso(self):
        from interfaz.principal import Windows
        self.regreso = Windows()
        self.passw.close()