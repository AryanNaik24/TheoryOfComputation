from collections import defaultdict

class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)

        while stack:
            state = stack.pop()
            if state in self.transition_function and '' in self.transition_function[state]:
                for next_state in self.transition_function[state]['']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)

        return closure

    def transition(self, states, symbol):
        next_states = set()
        for state in states:
            if state in self.transition_function and symbol in self.transition_function[state]:
                next_states.update(self.transition_function[state][symbol])
        return next_states

    def nfa_to_dfa(self):
        dfa_states = {}
        dfa_start_state = frozenset(self.epsilon_closure({self.start_state}))
        dfa_accept_states = set()
        dfa_transition_function = {}

        unprocessed_states = [dfa_start_state]
        dfa_states[dfa_start_state] = 'A'
        state_counter = 1

        while unprocessed_states:
            current_dfa_state = unprocessed_states.pop()
            dfa_transition_function[dfa_states[current_dfa_state]] = {}

            for symbol in self.alphabet:
                if symbol == '':
                    continue

                next_nfa_states = self.epsilon_closure(self.transition(current_dfa_state, symbol))
                if not next_nfa_states:
                    continue

                next_dfa_state = frozenset(next_nfa_states)

                if next_dfa_state not in dfa_states:
                    dfa_states[next_dfa_state] = chr(65 + state_counter)  # Use letters A, B, C, ...
                    state_counter += 1
                    unprocessed_states.append(next_dfa_state)

                dfa_transition_function[dfa_states[current_dfa_state]][symbol] = dfa_states[next_dfa_state]

                if next_dfa_state & self.accept_states:
                    dfa_accept_states.add(dfa_states[next_dfa_state])

        return DFA(set(dfa_states.values()), self.alphabet, dfa_transition_function, dfa_states[dfa_start_state], dfa_accept_states)


class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, string):
        current_state = self.start_state
        for symbol in string:
            if symbol in self.transition_function[current_state]:
                current_state = self.transition_function[current_state][symbol]
            else:
                return False
        return current_state in self.accept_states

    def print_transitions(self):
        print("DFA Transition Table:")
        for state in self.states:
            for symbol in self.alphabet:
                if symbol in self.transition_function[state]:
                    print(f"δ({state}, {symbol}) -> {self.transition_function[state][symbol]}")


# Take user input for NFA configuration
num_states = int(input("Enter the number of states: "))
states = set(input("Enter the states (space-separated): ").split())
alphabet = set(input("Enter the alphabet (space-separated): ").split())
start_state = input("Enter the start state: ")
accept_states = set(input("Enter the accept states (space-separated): ").split())

transition_function = {}
print("Enter the transition table (enter 'done' to finish):")
while True:
    state = input("State: ")
    if state == 'done':
        break
    transition_function[state] = defaultdict(set)
    while True:
        symbol = input(f"Symbol for state {state} (enter 'done' to finish): ")
        if symbol == 'done':
            break
        next_states = set(input(f"Next states for state {state} on symbol {symbol} (space-separated): ").split())
        transition_function[state][symbol] = next_states

# Create the NFA with user input
nfa = NFA(states, alphabet, transition_function, start_state, accept_states)

# Convert NFA to DFA
dfa = nfa.nfa_to_dfa()

# Print DFA transitions
dfa.print_transitions()

# Test the DFA with some strings
test_strings = input("Enter the test strings (space-separated): ").split()
dfa_results = {string: dfa.accepts(string) for string in test_strings}

for string, result in dfa_results.items():
    print(f"The string '{string}' is {'accepted' if result else 'rejected'} by the DFA.")
