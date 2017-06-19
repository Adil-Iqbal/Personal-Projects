# Object Oriented Tic-Tac-Toe

### You can play it by [**clicking here!**](https://jsfiddle.net/mv1vr4yc/1/)

You can resize the panes of JSFiddle if the game boards are going off screen. You can also hit the "Run" button in the top-left corner to play again.

The game features:

* **Resizable board** - All tile objects are sized and positioned with respect to the game board. To demonstrate this, four boards will appear with random sizes.
* **Computer Player Intelligence** - The computer player
moves based on the [*minimax algorithm*](https://en.wikipedia.org/wiki/Minimax) with [*alpha-beta pruning*](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to keep the game running efficiently.
* **First-move Random** - The computer player has a 50% chance to go first. Since the minimax algorithm can be a bit predictable, the first move is always decided randomly. That increases the variety of how the games play out.
* **Chance to Blunder** - Since the algorithm used by the computer can determine the best move based on all possible outcomes of the game, each game board has a random chance (0.1% - 15%) to blunder a move. This gives the human player a fighting chance! (Check the browser console to see the blunder chance for each game board.)

### Copyright 2017 by **Adil Iqbal**.
