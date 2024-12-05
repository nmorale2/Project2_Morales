import sys
from collections import defaultdict, deque
import csv

class NonDeterministicTuringMachine:
    def __init__(self, file_name):
        self.transitions = defaultdict(list)  # Transition rules
        self.name = ""
        self.states = set()
        self.input_alphabet = set()
        self.tape_alphabet = set()
        self.start_state = None
        self.accept_state = None
        self.reject_state = "qreject"  # Implicit reject state
        self.parse_file(file_name)
    
    def parse_file(self, file_name):
        """Parse the automata file."""
        with open(file_name, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            
        # Header parsing
        self.name = lines[0]
        self.states = set(lines[1].split(','))  # Line 2
        self.input_alphabet = set(lines[2].split(','))  # Line 3
        self.tape_alphabet = set(lines[3].split(','))  # Line 4
        self.start_state = lines[4]  # Line 5
        self.accept_state = lines[5]  # Line 6

        # Transition parsing
        for line in lines[7:]:
            if line.strip():
                parts = line.split(',')
                state, input_char, next_state, write_char, move_dir = parts
                self.transitions[(state, input_char)].append((next_state, write_char, move_dir))
    
    def simulate(self, input_string, max_steps=1000):
        """Simulate the NTM on the given input string."""
        tape = list(input_string) + ['_']  # Initialize tape with input and blanks
        initial_config = (self.start_state, 0, tape[:], 0, [])  # (state, head, tape, steps, history)
        queue = deque([initial_config])  # Use BFS for non-determinism
        steps = 0

        while queue and steps < max_steps:
            state, head, tape, current_steps, history = queue.popleft()
            steps += 1

            # Halt conditions
            if state == self.accept_state:
                print(f"Input: {input_string} - String accepted in {current_steps} steps!")
                self.print_path(history + [(tape, state, head)])
                return True
            if state == self.reject_state:
                continue
            
            # Read current tape character
            current_char = tape[head] if head < len(tape) else '_'
            transitions = self.transitions.get((state, current_char), [])
            
            # Apply transitions
            if not transitions:
                continue  # Implicitly move to reject state
            
            for next_state, write_char, move_dir in transitions:
                new_tape = tape[:]
                if head < len(new_tape):
                    new_tape[head] = write_char
                else:
                    new_tape.append(write_char)

                new_head = head + (1 if move_dir == 'R' else -1)
                if new_head < 0:  # Extend the tape to the left if needed
                    new_tape.insert(0, '_')
                    new_head = 0
                
                # Add the new configuration to the queue
                queue.append((next_state, new_head, new_tape, current_steps + 1, history + [(tape, state, head)]))
        
        print(f"Input: {input_string} - Execution stopped after {steps} steps. String rejected.")
        return False
    
    def print_path(self, history):
        """Print the step-by-step path."""
        for step, (tape, state, head) in enumerate(history):
            left_of_head = ''.join(tape[:head])
            head_char = tape[head] if head < len(tape) else '_'
            right_of_head = ''.join(tape[head + 1:])
            print(f"Step {step}: {left_of_head}({state}){head_char}{right_of_head}")

# Main Function
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 ntm_simulator.py <file_name> <csv_file> [<max_steps>]")
        sys.exit(1)
    
    file_name = sys.argv[1]
    csv_file = sys.argv[2]
    max_steps = int(sys.argv[3]) if len(sys.argv) > 3 else 1000

    ntm = NonDeterministicTuringMachine(file_name)
    print(f"Simulating machine: {ntm.name}")

    # Process CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip empty rows
                input_string = row[0]
                ntm.simulate(input_string, max_steps)
                print("-" * 40)