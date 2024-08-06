class State:
    def __init__(self, name, output):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_char, next_state):
        self.transitions[input_char] = next_state

    def get_next_state(self, input_char):
        return self.transitions.get(input_char)

    def get_output(self):
        return self.output


class MooreMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def process_input(self, input_string):
        output = [self.current_state.get_output()]

        for char in input_string:
            next_state = self.current_state.get_next_state(char)
            if next_state is None:
                raise ValueError(f"Invalid input character: {char}")
            self.current_state = next_state
            output.append(self.current_state.get_output())

        return ''.join(output)


def main():
    # Define states with their associated outputs
    q0 = State("q0", "1")
    q1 = State("q1", "0")

    # Define transitions
    q0.add_transition('a', q0)
    q0.add_transition('b', q1)
    q1.add_transition('a', q0)
    q1.add_transition('b', q1)

    # Initialize Moore Machine
    machine = MooreMachine(q0)

    # Process input string
    input_string = input("Enter the input string: ")
    output = machine.process_input(input_string)

    # Count occurrences of '1' in the output
    count = output.count('1')

    print("Input: " + input_string)
    print("Output: " + output)
    print("a has occurred " + str(count - 1) + " times")


if __name__ == "__main__":
    main()
