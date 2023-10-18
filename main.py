import sys
from interfaz.principal import Windows
from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Windows()
    
    sys.exit(app.exec()) 
    
    