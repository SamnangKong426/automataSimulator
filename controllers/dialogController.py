import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class AutomataSimulatorController(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("interfaces/dialog_input.ui", self)
        self.statesLine = self.findChild(QtWidgets.QLineEdit, 'statesLine')
        self.symbolsLine = self.findChild(QtWidgets.QLineEdit, 'symbolsLine')
        self.transitionsLine = self.findChild(QtWidgets.QLineEdit, 'transitionsLine')
        self.initialStateLine = self.findChild(QtWidgets.QLineEdit, 'initialStateLine')
        self.finalStatesLine = self.findChild(QtWidgets.QLineEdit, 'finalStatesLine')
        

    def button_clicked(self):
        # Action to take when the button is clicked
        text = self.lineEdit.text()
        print(f"LineEdit content: {text}")
        

# app = QtWidgets.QApplication(sys.argv)
# window = AutomataSimulatorController()
# window.show()
# app.exec_()






