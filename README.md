# Project2_Morales
Project 2 Readme Team Morales
Version 1 9/11/24
A single copy of this template should be filled out and submitted with each project submission, regardless of the number of students on the team. It should have the name readme_”teamname”
Also change the title of this template to “Project x Readme Team xxx”
1
Team Name: Morales
2
Team members names and netids: Nicolas Morales: nmorale2
3
Overall project attempted, with sub-projects: Project 1: Tracing NTM Behavior
4
Overall success of the project: Great! Everything worked out fine
5
Approximately total time (in hours) to complete: 4-5 hours
6
Link to github repository: https://github.com/nmorale2/Project2_Morales 
7
List of included files (if you have many files of a certain type, such as test files of different sizes, list just the folder): (Add more rows as necessary). Add more rows as necessary.

File/folder Name
File Contents and Use
Code Files
NTM_Morales.py
Is the code file containing the algorithm using a deque to trace the behavior of a Turing Machine.
Test Files
ntm_test_cases.txt
input_Morales.csv
Contains hundreds of test cases, and ntm_test_cases.txt contains the 7-tuple implementation of the turing machine given at the top of the file.
Output Files
output_Morales.txt
Contains the output from the above input files when passed through the program.
Discussion of Program Correctness
In order to ensure the program was correct, I did several things. First, I verified the implementation against Turing Machine specifications to manage edge cases. Second, I manually traced out several inputs to check if they matched the program output. These strings were both long and short, with different input cases such as: short strings (“1”, “10”); inputs with blanks (“1_0”, “110_”); and long strings of 100 characters to test if nondeterminism branches correctly.





8
Programming languages used, and associated libraries: I used python, and used the libraries ‘sys’, ‘collections’, and ‘csv’.
9
Key data structures (for each sub-project): I used a deque to perform BFS traversal for the turing machine’s nondeterminism.
10
General operation of code (for each subproject): This program simulates a Non-Deterministic Turing Machine by reading its description from a file and running it on a series of input strings provided in a CSV file. It explores all possible computational paths the NTM can take and determines whether the input string is accepted or rejected. The program is an implementation of theoretical computation that deals with non-deterministic behavior in Turing machines.
11
What test cases you used/added, why you used them, what did they tell you about the correctness of your code. I used several test cases with varying lengths and with varying amounts of non determinism. I was able to map them out on a program online and by hand and then checked them against the program that I coded to make sure the project was correct.
12
How you managed the code development: I developed the program by first defining the NonDeterministicTuringMachine class with attributes for states, alphabets, and transitions. I implemented the parse_file() method to read the NTM’s description and the simulate() method to run the machine on input strings using breadth-first search to handle non-determinism. The simulation tracks the machine’s execution, printing step-by-step tape and head positions. The program processes input from a CSV file and handles command-line arguments for flexibility. I tested and debugged components like file parsing and BFS to ensure correctness and efficient handling of non-deterministic behavior.
13
Detailed discussion of results: The results of running the Non-Deterministic Turing Machine (NTM) simulator show whether each input string is accepted or rejected based on the machine's transitions. The program uses breadth-first search (BFS) to explore all possible configurations, allowing the NTM to handle non-determinism by branching into multiple paths. For each input, the simulator prints a step-by-step trace of the tape, state, and head position, offering insights into the machine’s execution. Performance can vary depending on the complexity of the NTM and the input size, with non-determinism potentially leading to longer execution times. The program helps visualize the machine’s behavior and can be debugged through the detailed execution log.
14
How team was organized: I worked alone
15
What you might do differently if you did the project again: If I had to do the project again, I might want to use a different data structure instead of using a deque. Maybe use a graph traversal algorithm to find the most optimal path or something of that nature.
16
