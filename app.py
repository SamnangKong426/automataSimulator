import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from controllers.automataSimulatorController import AutomataSimulatorController

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("interfaces/introduction.ui", self)
        self.w = None
        self.learnMoreBtn.clicked.connect(self.on_getStartedBtn_clicked)
        self.gettingStartBtn.clicked.connect(self.on_gettingStartBtn_clicked)

    def on_getStartedBtn_clicked(self):
        self.titleLable.setText("Learn More")

    def on_gettingStartBtn_clicked(self):
        print("Getting Started")
        self.hide()
        self.w = AutomataSimulatorController()
        self.w.show()
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()