// Copyright 2017 by Adil Iqbal.
// All rights reserved.

var target = {
    m: null,
    b: null,
    x1: -1,
    y1: null,
    x2: 1,
    y2: null,
    weight: 10,
    col: {
        r: 100,
        g: 100,
        b: 100
    }
}

var points = [];
var index = 0;

var w = 600;
var h = 480;

var perceptron = new Perceptron();

function setup() {
    createCanvas(w, h);
    // Calculate target line values.
    target.m = random(-3, 3);
    target.b = random(-1, 1);
    target.y1 = f(target.x1, target);
    target.y2 = f(target.x2, target);
    target.x1 = pixelX(target.x1)
    target.x2 = pixelX(target.x2)
    target.y1 = pixelY(target.y1)
    target.y2 = pixelY(target.y2)

    // Generate training data.
    for (var i = 0; i < 50; i++) {
        var x = random(-1, 1)
        var y = random(-1, 1)
        points.push(new Point(x, y));
    }

    // Initialize perceptron.
    perceptron.initialize();
};

function draw() {
    background(200);
    push();
    translate(w / 2, h / 2);
    if (index > points.length-1){
        index = 0;
    } else {
        index += 1;
    }

    console.log(index, points.length)

    // Draw training points.
    for (var i = 0; i < points.length; i++) {
        points[i].update();
        points[i].show();
    };

    // Draw target line.
    strokeWeight(4)
    line(target.x1, target.y1, target.x2, target.y2);

    // Train perceptron.
    var pt = points[index];
    perceptron.train(pt.x, pt.y, pt.target_y);

    // Draw perceptron line.
    strokeWeight(1)
    percline = perceptron.end_points()
    line(percline[0], percline[1], percline[2], percline[3]);
}

function f(x, line_object) {
    var m = line_object.m;
    var b = line_object.b;
    return -(m * x + b);
}

function pixelX(x) {
    return map(x, -1, 1, -w / 2, w / 2);
}

function pixelY(y) {
    return map(y, -1, 1, -h / 2, h / 2);
}
