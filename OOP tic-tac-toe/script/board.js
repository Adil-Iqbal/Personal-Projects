function Board(index, x, y, size) {
    // Parameter variables.
    this.index = index;
    this.x = x;
    this.y = y;
    this.size = size;

    // Rendering Variables.
    this.pad = this.size * 0.167; // Thickness of lines.
    this.w = this.size + this.pad;
    this.h = this.w;
    this.bounds = {
        posX: this.x + (this.w / 2),
        negX: this.x - (this.w / 2),
        posY: this.y + (this.h / 2),
        negY: this.y - (this.h / 2)
    };
    this.swapSymbols = false;
    this.col = {
        r: 0,
        g: 0,
        b: 0
    };
    // Tracking variables.
    this.board = [];
    this.turn = null;
    this.gameOn = false;
    this.gameOver = false;
    this.result = null;
    this.maxDepth = 15;
    this.blunder;


    this.initialize = function() {
        // Set turn by coin toss.
        if (random(1) > 0.5) {
            this.turn = human;
        } else {
            this.turn = computer;
        }
        // Choose symbols by coin toss.
        if (random(1) > 0.5) {
            this.swapSymbols = true;
        }
        // Set intelligence of computer AI.
        this.blunder = random(0.001, 0.15);
        // Create board.
        for (var i = 0; i < 9; i++) {
            // Find x in terms of i, this.w, and this.pad.
            var mx = i % 3;
            var x = ((this.w - this.pad) / 6 + mx * ((this.w - this.pad) / 3 + this.pad / 2)) + (this.x - this.w / 2);
            // Find y in terms of i, this.h, and this.pad
            var my1 = (i % 9) / 3;
            var my2 = my1 % 1;
            if (my2 == 0) {
                var my3 = my1 * ((this.h - this.pad) / 3 + this.pad / 2);
            }
            var y = ((this.h - this.pad) / 6 + my3) + (this.y - this.h / 2);
            // Initialize tiles.
            this.board[i] = new Tile(i, games[this.index], x, y);
            this.board[i].setSymbol();
        }
        // First computer move is random.
        if (this.turn == computer){
          this.randomMove(true);
        }
    };


    this.show = function() {
        // Setup
        this.col = this.setColor();
        noStroke();
        fill(this.col.r, this.col.g, this.col.b);
        // Show game board.
        rect(this.x, this.y, this.w, this.h);
        for (var i = 0; i < this.board.length; i++) {
            this.board[i].show(this.col);
        }
        // Computer's move.
        if (!this.gameOver && this.turn == computer) {
            if (random(1) > this.blunder) {
                this.minimax();
            } else {
                this.randomMove();
            }
        }
        // Show result of game.
        if (this.gameOver) {
            this.endGame();
        }
    };


    this.setColor = function() {
        // Game is waiting...
        if (this.gameOn == false) {
            this.col.r = 150;
            this.col.g = 150;
            this.col.b = 150;
        }
        // Game is in progress.
        if (this.gameOn == true && this.gameOver == false) {
            this.col.r = 0;
            this.col.g = 0;
            this.col.b = 0;
        }
        // Game is over.
        if (this.gameOver) {
            if (this.result == 'win') {
                this.col.r = 0;
                this.col.g = 120;
                this.col.b = 0;
            }
            if (this.result == 'loss') {
                this.col.r = 170;
                this.col.g = 0;
                this.col.b = 0;
            }
            if (this.result == 'draw') {
                this.col.r = 0;
                this.col.g = 0;
                this.col.b = 170;
            }
        }
        return this.col
    };


    // Invoke computer AI
    this.minimax = function() {
        this.board[this.compValue(this.board)].state = computer;
        this.switchTurn();
    };


    // Blundered Move.
    this.randomMove = function(first = false) {
        var emptyTiles = this.getEmptyTiles(this.board);
        var randomIndex = floor(random(0, emptyTiles.length));
        var randomTile = emptyTiles[randomIndex];
        this.board[randomTile].state = computer;
        if (!first) {
            this.switchTurn();
        } else {
            this.turn = human
        }
    };


    this.endGame = function() {
        var winIndex = this.checkForWin(this.board, false, returnIndex = true);
        stroke(this.col.r - 40, this.col.g - 40, this.col.b - 40);
        var lineThickness = map(this.size, 25, 200, 1, 5)
        strokeWeight(lineThickness); // WIP (map to padding)
        switch (winIndex) {
            case 0:
                line(this.bounds.negX, this.board[0].y, this.bounds.posX, this.board[2].y);
                break;
            case 1:
                line(this.bounds.negX, this.board[3].y, this.bounds.posX, this.board[5].y);
                break;
            case 2:
                line(this.bounds.negX, this.board[6].y, this.bounds.posX, this.board[8].y);
                break;
            case 3:
                line(this.board[0].x, this.bounds.negY, this.board[6].x, this.bounds.posY);
                break;
            case 4:
                line(this.board[1].x, this.bounds.negY, this.board[7].x, this.bounds.posY);
                break;
            case 5:
                line(this.board[2].x, this.bounds.negY, this.board[8].x, this.bounds.posY);
                break;
            case 6:
                line(this.bounds.negX, this.bounds.negY, this.bounds.posX, this.bounds.posY);
                break;
            case 7:
                line(this.bounds.posX, this.bounds.negY, this.bounds.negX, this.bounds.posY);
                break;
        }
    };


    this.compValue = function(node, depth = 0, a = -999, b = 999, first = true) {
        var emptyTiles = this.getEmptyTiles(node);
        var winner = this.checkForWin(node, returnPlayer = true);
        var terminal = this.isTerminalNode(depth, emptyTiles, winner);
        if (typeof terminal == 'number') {
            return terminal;
        }
        var maxValue = -999;
        var index = null
        for (var i = 0; i < emptyTiles.length; i++) {
            var childNode = this.createChildNode(node, emptyTiles[i], computer);
            var value = this.humanValue(childNode, depth++, a, b);
            if (value > maxValue) {
                maxValue = value;
                index = emptyTiles[i];
            }
            if (value > a) {
                a = value;
            }
            if (a >= b) {
                if (first) {
                    return index;
                } else {
                    return a;
                }
            }
        }
        if (first) {
            return index;
        } else {
            return maxValue;
        }
    };


    this.switchTurn = function() {
        var emptyTiles = this.getEmptyTiles(this.board);
        var winner = this.checkForWin(this.board, returnPlayer = true);
        if (typeof winner == 'number') {
            this.gameOver = true;
            if (winner == human) {
                this.result = 'win';
            }
            if (winner == computer) {
                this.result = 'loss';
            }
        } else if (emptyTiles.length == 0) {
            this.gameOver = true;
            this.result = 'draw';
        } else {
            this.turn *= -1;
        }
        redraw();
    };


    this.getEmptyTiles = function(onBoard) {
        var emptyTiles = [];
        for (var i = 0; i < onBoard.length; i++) {
            if (typeof onBoard[i] == 'number' && onBoard[i] == empty) {
                emptyTiles.push(i);
            } else if (typeof onBoard[i] == 'object' && onBoard[i].state == empty) {
                emptyTiles.push(onBoard[i].index);
            }
        }
        return emptyTiles;
    };


    this.checkForWin = function(onBoard = board, returnPlayer = false, returnIndex = false) {
        var space1, space2, space3;
        for (var i = 0; i < winConditions.length; i++) {
            if (typeof onBoard[i] == "object") {
                space1 = onBoard[winConditions[i][0]].state;
                space2 = onBoard[winConditions[i][1]].state;
                space3 = onBoard[winConditions[i][2]].state;
            } else if (typeof onBoard[i] == "number") {
                space1 = onBoard[winConditions[i][0]];
                space2 = onBoard[winConditions[i][1]];
                space3 = onBoard[winConditions[i][2]];
            }
            if (space1 == space2 && space2 == space3 && space3 != empty) {
                if (returnPlayer) {
                    return space1;
                } else if (returnIndex) {
                    return i;
                } else {
                    return true;
                }
            }
        }
        return false;
    };


    this.isTerminalNode = function(depth, emptyTiles, winner) {
        if (depth > this.maxDepth || emptyTiles.length == 0 || typeof winner == "number") {
            if (emptyTiles.length == 0 && typeof winner != "number") {
                return 0;
            }
            if (typeof winner == "number") {
                return (10 - depth) * winner;
            }
        }
        return false;
    };


    this.createChildNode = function(parentNode, emptyTileIndex, thisTurn) {
        var childNode = [];
        for (var i = 0; i < parentNode.length; i++) {
            if (typeof parentNode[i] == "object") {
                childNode.push(parentNode[i].state);
            } else if (typeof parentNode[i] == "number") {
                childNode.push(parentNode[i]);
            }
        }
        childNode[emptyTileIndex] = thisTurn;
        return childNode;
    };


    this.humanValue = function(node, depth = 0, a, b) {
        var emptyTiles = this.getEmptyTiles(node);
        var winner = this.checkForWin(node, returnPlayer = true);
        var terminal = this.isTerminalNode(depth, emptyTiles, winner);
        if (typeof terminal == 'number') {
            return terminal;
        }
        var minValue = 999;
        for (var i = 0; i < emptyTiles.length; i++) {
            var childNode = this.createChildNode(node, emptyTiles[i], human);
            var value = this.compValue(childNode, depth++, a, b, false);
            if (value < minValue) {
                minValue = value;
            }
            if (value < b) {
                b = value;
            }
            if (a >= b) {
                return b;
            }
        }
        return minValue;
    };


    this.clicked = function() {
        if (!this.gameOver) {
            if (mouseX < this.bounds.posX && mouseX > this.bounds.negX && mouseY < this.bounds.posY && mouseY > this.bounds.negY) {
                if (this.gameOn == false) {
                    this.gameOn = true;
                }
                for (var i = 0; i < this.board.length; i++) {
                    this.board[i].clicked();
                }
            }
        }
    };
}
