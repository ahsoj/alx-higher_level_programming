#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
        this.width = w;
	this.height = h;
    }
    print () {
        for (let i = 1; i <= this.height;i++) {
            for (let j = 1; j <= this.width; j++) {
                process.stdout.write('X'+'')
	    }
	    console.log();
        }
    }
    rotate () {
    	let ex = this.width;
	this.width = this.height;
	this.height = ex;
    }
    double () {
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;
