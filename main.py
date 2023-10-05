import sys
from interfaz.principal import MainWindows
from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    
    sys.exit(app.exec()) 