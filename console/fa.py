from automata.fa.dfa import DFA
import graphviz

# Functionalities -> python library (automaton-lib, graviz, pyqt5, json, pyinstaller)
# a. Design a finite automaton (FA)                         | Done
# b. Test if a FA is deterministic or non-deterministic     | Done
# c. Test if a string is accepted by a FA                   | Done
# d. Construct an equivalent DFA from an NFA                | Done
# e. Minimize a DFA

class FiniteAutomata():
    def __init__(self, dfa):
        self.dfa = dfa

    def is_deterministic(self):
        return self.dfa.is_deterministic()
