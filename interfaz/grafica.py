from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

import matplotlib.pyplot as plt

class PlotBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bar = uic.loadUi('interfaz/Plot.ui')
        self.bar.show()
        self.bar.btngraficar.clicked.connect(self.graficar)
        
    def graficar(self):
        fig, ax = plt.subplots()
        
        fruits = ['manzana', 'naranja', 'banano', 'fresa', 'pera']
        data = [50, 20, 45, 100, 60]
        bar_labels = ['manzana', 'naranja', 'banano', 'fresa', 'pera']
        bar_colors = ['#BF0B3B', '#D50DD9', '#238C2A', '#F2B90C', '#F27405']
        
        ax.bar(fruits, data, label=bar_labels, color=bar_colors)
        ax.set_ylabel('FRUTAS')
        ax.set_title('GRAFICA DE BARRAS DE LAS FRUTAS')
        ax.legend(title='COLOR DE FRUTAS')
        plt.show()