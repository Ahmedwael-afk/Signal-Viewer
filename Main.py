from Gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys, os



class AppWindow(QtWidgets.QMainWindow,Ui_MainWindow): #Test    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_draw.clicked.connect(self.draw)
        self.pushButton_clear.clicked.connect(self.clear)




    def draw(self):
        dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        dev_y = [38496, 42000, 46752, 49320, 53200,
                 56000, 62316, 64928, 67317, 68748, 73752]

        self.graphicsView.plot(dev_x,dev_y)

    def clear(self):
        self.graphicsView.clear()








app = QtCore.QCoreApplication.instance()
if app is None:
    app = QtWidgets.QApplication(sys.argv)
w = AppWindow()

w.show() # Create the widget and show it
sys.exit(app.exec_()) # Run the app