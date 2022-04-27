from Gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import  pandas  as  pd
import random
import pyqtgraph as pg
import sys, os



class AppWindow(QtWidgets.QMainWindow,Ui_MainWindow): #Test    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_draw.clicked.connect(self.draw)
        self.pushButton_clear.clicked.connect(self.clear)




    def draw(self):
        chunks = []
        for chunk in pd.read_csv("emg - Copy.csv",chunksize = 50):
            i = chunk
            chunks.append(i)
        for j in range(len(chunks)):
            self.graphicsView.plot(chunks[j])
            plt.pause(0.3)

    def clear(self):
        self.graphicsView.clear()








app = QtCore.QCoreApplication.instance()
if app is None:
    app = QtWidgets.QApplication(sys.argv)
w = AppWindow()

w.show() # Create the widget and show it
sys.exit(app.exec_()) # Run the app