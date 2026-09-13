# Python Chess

A graphical two-player chess game built from scratch in Python using **Tkinter** and **Pillow**.

This project was created to practice Python programming, GUI development, event handling, and implementing chess movement rules without relying on an existing chess engine or chess library.

## Features

* Interactive 8×8 chessboard built with Tkinter
* Graphical chess pieces using image assets
* Alternating White and Black turns
* Piece selection using mouse clicks
* Legal movement validation for:

  * Pawns
  * Rooks
  * Knights
  * Bishops
  * Queens
  * Kings
* Piece capturing
* Collision detection to prevent sliding pieces from moving through other pieces
* Initial two-square pawn movement
* En passant support
* Internal tracking of each piece's type, color, and board position

## Technologies Used

* Python
* Tkinter
* Pillow (PIL)

## Requirements

Make sure Python is installed on your computer.

The project also requires Pillow:

```bash
pip install pillow
```

Tkinter is included with most standard Python installations.

## Required Image Files

The program uses PNG images for each chess piece. These files should be located in the same directory as `Chess.py`:

```text
white-pawn.png
white-rook.png
white-knight.png
white-bishop.png
white-queen.png
white-king.png

black-pawn.png
black-rook.png
black-knight.png
black-bishop.png
black-queen.png
black-king.png
```

## Running the Program

Clone or download the repository and navigate to the project directory.

Then run:

```bash
python Chess.py
```

A 640×640 chess window will open.

To move a piece:

1. Click the chess piece you want to move.
2. Click the square where you want to move it.
3. If the move is valid, the piece will move.
4. The turn will switch to the opposing player.

To capture an opposing piece, select your piece and then click the opponent's piece.

## How It Works

The game stores each chess piece in a dictionary containing information such as:

```python
"pawn1": {
    "type": "pawn",
    "position": "a2",
    "color": "White"
}
```

Board locations use standard chess notation such as `a1`, `e4`, and `h8`.

Each type of chess piece has its own movement-validation function. For example:

```python
valid_pawn_move()
valid_rook_move()
valid_bishop_move()
valid_knight_move()
valid_queen_move()
valid_king_move()
```

The program checks whether a requested move follows the movement rules for the selected piece before updating its position on the Tkinter canvas.

Rooks, bishops, and queens also check the squares between their starting and ending positions so that they cannot move through another piece.

Mouse input is handled through Tkinter's event system:

```python
chessboard.bind("<Button-1>", click)
```

The `click()` function handles piece selection, movement, captures, turn changes, and special pawn behavior.

## Current Limitations

The project is still a work in progress. Some complete chess rules are not currently implemented, including:

* Check detection
* Checkmate detection
* Stalemate
* Castling
* Pawn promotion
* Preventing a king from moving into check
* Game reset/restart
* Move history
* Chess notation
* Computer/AI opponent

Because check and checkmate detection are not yet implemented, the game currently focuses primarily on piece movement and board interaction rather than enforcing every rule required for a complete chess game.

## Possible Future Improvements

Future versions could include:

* Check and checkmate detection
* Castling
* Pawn promotion interface
* Highlighting legal moves
* Highlighting the currently selected piece
* Move history
* Algebraic chess notation
* Undo functionality
* Restart button
* Main menu
* Player clocks
* Improved GUI and board colors
* Object-oriented redesign of chess pieces
* AI/computer opponent

## Project Goal

The main goal of this project was to build the logic behind a chess game manually while improving my understanding of Python.

Instead of using an existing chess engine, movement rules, captures, board state, and user interaction were implemented directly in the program. This made the project an exercise in both programming logic and graphical application development.

## Author

Created as a personal Python programming project.
