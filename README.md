Connect4Game
Connect4Game is a Python implementation of the classic Connect Four game, allowing a human player to compete against a computer opponent. The project emphasizes object-oriented programming principles and layered architecture. It includes both a console-based user interface and an optional graphical user interface (GUI) for enhanced user experience.​

Features
Human vs. Computer Gameplay: Engage in a game against a computer opponent that employs basic strategic moves.

Input Validation: Robust handling of user inputs to prevent invalid moves and ensure smooth gameplay.

Layered Architecture: Separation of concerns through distinct modules for game logic, user interface, and testing.

Unit Testing: Comprehensive PyUnit test cases for non-UI modules to ensure code reliability.

Optional GUI: A graphical interface built with Tkinter, providing an alternative to the console-based UI.​

Requirements
Python 3.6 or higher

Tkinter (for GUI version)​

Gameplay Overview
Objective: Be the first to connect four of your discs in a row—vertically, horizontally, or diagonally.

Turns: Players alternate turns, dropping one disc into a column per turn.

Winning: The first player to align four discs wins the game.

Draw: If the board is full and no player has four aligned discs, the game ends in a draw.​
GitHub
+4
GitHub
+4
GitHub
+4

Computer Player Strategy
The computer opponent employs a basic strategy:​

Winning Move: If a winning move is available, the computer will take it.

Blocking: If the human player is one move away from winning, the computer will block that move.

Random Move: If no immediate win or block is necessary, the computer selects a random valid column.​

Note: The AI does not implement advanced algorithms like minimax; it focuses on immediate threats and opportunities.​
