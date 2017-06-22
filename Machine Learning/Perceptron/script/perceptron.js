// Copyright 2017 by Adil Iqbal.
// All rights reserved.

function Perceptron() {

    // Primary attributes.
    this.bias = 1;
    this.learning_rate = 0.01;
    this.m = null;
    this.b = null;

    // Line end-points.
    this.x1 = -1;
    this.x2 = 1;
    this.y1 = null;
    this.y2 = null;

    this.weights = [];

    this.initialize = function() {
        this.m = random(-3, 3);
        this.b = random(-1, 1);
        for (var i = 0; i < 3; i++) {
            this.weights[i] = random(-1, 1);
        };
    }

    this.feedforward = function(x, y) {
        var sum = 1 * this.weights[0]; // bias
        sum += x * this.weights[1];
        sum += y * this.weights[2];
        return this.activate(sum);
    };

    this.activate = function(num) {
        if (num > 0) {
            return 1
        } else {
            return -1
        }
    };

    this.train = function(x, y, desired) {

        // Calculate guess point with respect to perceptron.
        var guess = this.feedforward(x, y)

        // Find error.
        var error = desired - guess;

        // Update weights.
        this.weights[0] += error * 1 * this.learning_rate; // bias.
        this.weights[1] += error * x * this.learning_rate;
        this.weights[2] += error * y * this.learning_rate;

        // Update attributes.
        this.m = this.weights[2] / this.weights[1];
        this.b = this.weights[0];

    };

    this.end_points = function() {
        var obj = {
            m: this.m,
            b: this.b
        }
        this.y1 = f(this.x1, obj);
        this.y2 = f(this.x2, obj);
        var x1 = pixelX(this.x1);
        var x2 = pixelX(this.x2);
        var y1 = pixelY(this.y1);
        var y2 = pixelY(this.y2);
        return [x1, y1, x2, y2];
    }
}
