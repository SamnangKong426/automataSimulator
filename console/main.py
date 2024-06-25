from automata.fa.dfa import DFA
import graphviz
import os

def get_input_symbols():
    valid_symbols = set(map(chr, range(ord('a'), ord('z')+1))) | set(map(chr, range(ord('A'), ord('Z')+1))) | {'0', '1'}
    
    while True:
        input_symbols = input("Enter input symbols (comma-separated, alphanumeric): ").strip().split(',')
        input_symbols = [symbol.strip() for symbol in input_symbols]
        
        if all(symbol in valid_symbols for symbol in input_symbols):
            return input_symbols
        else:
            print("Invalid input. Please enter alphanumeric symbols (a-z, A-Z, 0-1).")

def get_states():
    while True:
        states = input("Enter states (comma-separated, alphanumeric): ").strip().split(',')
        if all(state.isalnum() for state in states):
            return states
        else:
            print("Invalid input. Please enter alphanumeric states.")

def get_final_states(states):
    while True:
        final_states = input("Enter final states (comma-separated): ").strip().split(',')
        if all(state in states for state in final_states):
            return final_states
        else:
            print("Invalid final state(s). Please enter states from the set of defined states.")

def draw_dfa(dfa, output_path):
    try:
        # Create a new directed graph
        dot = graphviz.Digraph(format='pdf')

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

        print(f"DFA diagram saved to {output_path}.pdf")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Get DFA details
    states = get_states()
    input_symbols = get_input_symbols()
    initial_state = input("Enter initial state: ").strip()
    final_states = get_final_states(states)

    transitions = {}
    for state in states:
        transitions[state] = {}
        for symbol in input_symbols:
            next_state = input(f"Transition from {state} with symbol '{symbol}': ").strip()
            transitions[state][symbol] = next_state

    # Define the DFA
    dfa = DFA(
        states=set(states),
        input_symbols=set(input_symbols),
        transitions=transitions,
        initial_state=initial_state,
        final_states=set(final_states)
    )

    # Print the transition table
    print("\nTransition Table:")
    for state, paths in dfa.transitions.items():
        for symbol, next_state in paths.items():
            print(f"{state} --{symbol}--> {next_state}")

    # View the DFA structure
    print("\nDFA Structure:")
    print("States:", dfa.states)
    print("Input Symbols:", dfa.input_symbols)
    print("Initial State:", dfa.initial_state)
    print("Final States:", dfa.final_states)

    # Path to save the image
    output_path = r'console/picsdfa_diagram'
    
    # Ensure the directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        print(f"Directory {output_dir} does not exist. Creating directory.")
        os.makedirs(output_dir)

    # Draw the DFA diagram and save to the specified path
    draw_dfa(dfa, output_path)
