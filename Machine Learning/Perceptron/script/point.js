// Copyright 2017 by Adil Iqbal.
// All rights reserved.

function Point(x, y) {

    // Normalized coordinates.
    this.x = x;
    this.y = -y;

    // Pixel coordinates.
    this.px = pixelX(this.x);
    this.py = pixelY(this.y);

    // This point's relationship to target line.
    this.target_y = f(this.x, target)
    if (this.y < this.target_y) {
        this.point_to_target = 1;
    } else {
        this.point_to_target = -1;
    }

    // Accuracy of the perceptron's evaluation of this point.
    this.status = false;

    this.show = function() {
        if (this.status) {
            fill(0, 255, 0, 180)
        } else {
            fill(255, 0, 0, 180)
        }
        strokeWeight(1)
        stroke(0, 0, 0)
        ellipse(this.px, this.py, 10, 10)
        point(this.px, this.py)
    };

    this.update = function() {

        // This point's relationship to the perceptron line.
        if (this.y > f(this.x, perceptron)) {
            var point_to_perceptron = 1;
        } else {
            var point_to_perceptron = -1;
        }

        // Does the perceptron evaluate this point correctly?
        if (this.point_to_target == point_to_perceptron) {
            this.status = true;
        } else {
            this.status = false;
        }
    }
}
