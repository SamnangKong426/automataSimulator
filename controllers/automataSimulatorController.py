import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from automata.fa.dfa import DFA
import json
import graphviz

class AutomataSimulatorController(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("interfaces/automataSimulator.ui", self)
        self.statesLine = self.findChild(QtWidgets.QLineEdit, 'statesLineEdit')
        self.symbolsLine = self.findChild(QtWidgets.QLineEdit, 'symbolsLineEdit')
        self.transitionsLine = self.findChild(QtWidgets.QLineEdit, 'transitionsLineEdit')
        self.startStateLine = self.findChild(QtWidgets.QLineEdit, 'startStatesLineEdit')
        self.finalStatesLine = self.findChild(QtWidgets.QLineEdit, 'finalStates')
        self.submitBtn = self.findChild(QtWidgets.QPushButton, 'submitBtn')
        self.submitBtn.clicked.connect(self.okBtn_clicked)
        self.clearTextBtn = self.findChild(QtWidgets.QPushButton, 'clearTextBtn')
        self.clearTextBtn.clicked.connect(self.clearBtn_clicked)
        self.gravizImg = self.findChild(QtWidgets.QLabel, 'graphvizImg')
        self.imageCounter = 0
        
        # Fill the text fields with the json data
        self.fillJson()

    def okBtn_clicked(self):
        # Action to take when the button is clicked
        states = self.statesLine.text()
        symbols = self.symbolsLine.text()
        transitions = self.transitionsLine.text()
        startState = self.startStateLine.text()
        finalStates = self.finalStatesLine.text()

        # Create a DFA object with the input data
        dfa = DFA(
            states=eval(states),
            input_symbols=eval(symbols),
            transitions=eval(transitions),
            initial_state=eval(startState),
            final_states=eval(finalStates)
        )
        # Path to save the image
        output_path = r'assets/{}'.format(self.imageCounter)
        # Ensure the directory exists
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            print(f"Directory {output_dir} does not exist. Creating directory.")
            os.makedirs(output_dir)

        # Draw the DFA diagram and save to the specified path
        self.draw_dfa(dfa, output_path)
        self.changeGraviz()

    def draw_dfa(self, dfa, output_path):
        try:
            # Create a new directed graph
            dot = graphviz.Digraph(format='jpg')
            # Set rank direction to top to bottom
            dot.attr(rankdir='TB')
            # Add states (nodes)
            for state in dfa.states:
                shape = 'doublecircle' if state in dfa.final_states else 'circle'
                dot.node(state, shape=shape)
            # Add transitions (edges)
            for state, paths in dfa.transitions.items():
                for symbol, next_state in paths.items():
                    dot.edge(state, next_state, label=symbol)
            # Render the graph to file
            dot.render(output_path)
            print(f"DFA diagram saved to {output_path}.jpg")
        except Exception as e:
            print(f"An error occurred: {e}")
        self.imageCounter += 1
        
    def clearBtn_clicked(self):
        self.statesLine.clear()
        self.symbolsLine.clear()
        self.transitionsLine.clear()
        self.startStateLine.clear()
        self.finalStatesLine.clear()

    def fillJson(self):
        with open('db\\dfa.json', 'r') as f:
            data = json.load(f)
            # For lists, replace '[' and ']' with '{' and '}' respectively
            self.statesLine.setText(str(data['states']).replace('[', '{').replace(']', '}'))
            self.symbolsLine.setText(str(data['input_symbols']).replace('[', '{').replace(']', '}'))
            self.transitionsLine.setText(str(data['transitions']))
            self.startStateLine.setText(str(data['initial_state']))
            self.finalStatesLine.setText(str(data['final_states']).replace('[', '{').replace(']', '}'))

    def changeGraviz(self):
        self.gravizImg.setPixmap(QtGui.QPixmap(('assets/{}.jpg').format(self.imageCounter-1)))

        







