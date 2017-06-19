var games = [];
var human = -1;
var empty = 0;
var computer = 1;
var winConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


function setup() {
    console.clear()
    createCanvas(830, 220);
    noLoop();
    rectMode(CENTER);
    for (var i = 0; i <= 3; i++) {
        var size = floor(random(25, 200));
        var x = ((size * 1.167) / 2) + 10
        if (i > 0) {
            x += games[i - 1].bounds.posX
        }
        games[i] = new Board(i, x, 110, size);
        games[i].initialize();
        console.log((i + 1) + '.) ' + games[i].blunder * 100)
    }
    redraw();
}


function draw() {
    for (var i = 0; i < games.length; i++) {
        games[i].show()
    }
}


function mousePressed() {
    for (var i = 0; i < games.length; i++) {
        games[i].clicked()
    }
}
