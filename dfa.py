class MealyMachine:
    def __init__(self):
        # Define the states
        self.states = ['S0', 'S1']
        
        # Define the initial state
        self.current_state = 'S0'
        
        # Define the transitions and outputs
        self.transitions = {
            'S0': {'0': ('S1', 'A'), '1': ('S0', 'B')},
            'S1': {'0': ('S0', 'B'), '1': ('S1', 'A')}
        }
    
    def transition(self, input_char):
        if input_char in self.transitions[self.current_state]:
            next_state, output = self.transitions[self.current_state][input_char]
            self.current_state = next_state
            return output
        else:
            raise ValueError(f"Invalid input: {input_char}")
    
    def process_input(self, input_string):
        output_string = ""
        for char in input_string:
            output_string += self.transition(char)
        return output_string

# Example usage
if __name__ == "__main__":
    mealy_machine = MealyMachine()
    
    input_string = "010110"
    output_string = mealy_machine.process_input(input_string)
    
    print(f"Input: {input_string}")
    print(f"Output: {output_string}")
