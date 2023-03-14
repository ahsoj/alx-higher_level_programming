#!/usr/bin/node

const SQ = require('./5-square');

class Square extends SQ {
    constructor (size) {
        super(size)
	this.size = size;
    }
    charPrint(c) {
        let pr = c === undefined ? 'X' : 'C';
	for (let i = 1;i <= this.size;i++) {
            for (let j = 1; j <= this.size;j++) {
	        process.stdout.write(pr+'');
	    }
	console.log();
	}
    }
}
