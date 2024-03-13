#!/usr/bin/node

// Class definition for Rectangle
class Rectangle {
    constructor(w, h) {
        // Checking if both width and height are greater than 0
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }
}

// Exporting the Rectangle class
module.exports = Rectangle;

