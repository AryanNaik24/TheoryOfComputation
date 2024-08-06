class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_char, next_state, output):
        self.transitions[input_char] = (next_state, output)

    def get_next_state_and_output(self, input_char):
        return self.transitions.get(input_char)


class MealyMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def process_input(self, input_string):
        output = []

        for char in input_string:
            transition = self.current_state.get_next_state_and_output(char)
            if transition is None:
                raise ValueError(f"Invalid input character: {char}")
            next_state, out = transition
            output.append(out)
            self.current_state = next_state

        return ''.join(output)


def main():
    # Define states
    q0 = State("q0")
    q1 = State("q1")

    # Define transitions
    q0.add_transition('a', q0, '1')
    q0.add_transition('b', q1, '0')
    q1.add_transition('a', q0, '1')
    q1.add_transition('b', q1, '0')

    # Initialize Mealy Machine
    machine = MealyMachine(q0)

    # Process input string
    input_string = input("Enter the input string: ")
    output = machine.process_input(input_string)

    # Count occurrences of '1' in the output
    count = output.count('1')

    print("Input: " + input_string)
    print("Output: " + output)
    print("a has occurred " + str(count) + " times")


if __name__ == "__main__":
    main()
