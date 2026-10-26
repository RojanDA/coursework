
The program solves the 8-Puzzle problem using the A* Search Algorithm with
Manhattan Distance heuristic. The 8-Puzzle is a 3x3 sliding tile puzzle with
eight numbered tiles and one blank space. In this program, the blank space is
represented by 0.

The goal state used in this project is:

1 2 3
4 5 6
7 8 0

The program includes a graphical user interface (GUI) using Tkinter. The GUI
allows the user to select sample puzzles, enter custom puzzle states, solve the
puzzle, check whether a puzzle is solvable, animate the solution, and view
statistics such as total moves, nodes expanded, time taken, and path cost.


SYSTEM REQUIREMENTS
------------------------------------------------------------

- Python 3.10 or newer recommended
- Tkinter GUI support

No extra external packages are required.

The program uses only Python standard libraries:
- tkinter
- heapq
- time
- copy
- typing

Because these are standard Python libraries, the user does not need to install
extra packages using pip.

HOW TO INSTALL PYTHON 
------------------------------------------------------------


https://www.python.org/downloads/

Add python.exe to PATH

This step is important because it allows Python to run from Command Prompt.


HOW TO USE THE PROGRAM
------------------------------------------------------------

When the program opens, the user will see:
- 3x3 puzzle board
- input boxes for numbers 0 to 8
- Easy, Medium, Hard, and Unsolvable sample buttons
- Solve button
- Animate Solution button
- Step Forward button
- Reset button
- Clear button
- results/statistics panel

Option 1: Use a sample puzzle

Step 1:
Click Easy, Medium, Hard, or Unsolvable.

Step 2:
Click Solve.

Step 3:
If the puzzle is solvable, the result panel will show:
- Algorithm
- Heuristic
- Initial state
- Goal state
- Solution found
- Total moves
- Nodes expanded
- Time taken
- Path cost

Step 4:
Click Animate Solution to watch the solution step by step.

Step 5:
Click Step Forward if you want to manually move through the solution path.

Option 2: Enter a custom puzzle

Step 1:
Enter numbers 0 to 8 into the 9 input boxes.

Important:
- Use each number from 0 to 8 exactly once.
- 0 represents the blank tile.
- Do not repeat numbers.
- Do not leave boxes empty.

Example custom puzzle:

1 2 3
4 0 6
7 5 8

Step 2:
Click Solve.

Step 3:
If the puzzle is solvable, the program will solve it using A* Search.

Step 4:
Click Animate Solution to view the movement of the tiles.


SAMPLE PUZZLES USED IN THE PROGRAM
------------------------------------------------------------

Easy:

1 2 3
4 5 6
7 0 8

Medium:

1 2 3
4 0 6
7 5 8

Hard:

8 6 7
2 5 4
3 0 1

Unsolvable:

1 2 3
4 5 6
8 7 0

