## X O Game in Python

This project is implemented in Python using Object-Oriented Programming (OOP) principles. The game allows two players to compete against each other, taking turns to place their symbols (X or O) on a 3x3 grid. The game supports both human vs. human and human vs. computer modes.

### Features

- Object-Oriented Design: The game is structured using classes to represent different components such as the game board, players, and the game logic.
- Two-Player Mode: Play against another human player in turn-based gameplay.
- Single-Player Mode: Play against the computer, which makes random moves.
- Endgame Options: After a win or draw, players can choose to restart the game or quit.
- Input Validation: Ensures that players enter valid moves (numbers between 1 and 9).

### Classes

- Game: Manages the overall game flow, including turn-taking, checking for win/draw conditions, and handling endgame scenarios.
- Board: Represents the game board and includes methods to display the board, update cells, and reset the board for a new game.
- Player: Represents a player, storing their name and symbol (X or O).
- Menu: Handles the display of menus and user input for game settings and endgame options.

### How to Play

1. Start the Game: Run the game.start_game() method to begin.
2. Choose Mode: Select whether you want to play against another player or the computer.
3. Make Moves: Players take turns to enter their moves by choosing a cell number (1-9) corresponding to the positions on the board.
4. Win/Draw Check: The game checks for win or draw conditions after each move.
5. Endgame Menu: Choose to restart the game or quit after a game ends.
