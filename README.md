# Introduction

Hi. I'm Benjamin Chen, author of this Tic Tac Toe game. There can be 1 player or 2 players, depending on what the user wants. Libraries used: random

## Gameplay

Here is an example of gameplay.

```
How many players, 1 or 2? 1
|---|---|---|
| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
|---|---|---|
| 7 | 8 | 9 |
|---|---|---|
Enter the coordinate to place a marker.
Do you want to be X or O?
```
The player can choose how many people play the game (1 or 2), and the first person to go can choose to be X or O.

To place a marker, the current player inputs an eligible number to substitute their marker with that number (if that number doesn't exist, then the player will be prompted again). Then, their turn ends and gameplay switches to the other player (or the computer in 1 player mode).

The game ends when:
- one player places 3 markers in a row
- there are no more available markers left on the board

## Computer Algorithm

The computer works by:
1. seeing if the computer can win in one move
2. seeing if the computer can block the player from winning
3. choosing a corner, if available
4. choosing the center, if available
5. choosing an edge, if available

Stopping if there are no more spaces left on the board ensures that there will never be an error when the computer decides its move.
