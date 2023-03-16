#!/usr/bin/node

const Rectange = require('./4-rectangle');

class Square extends Rectange {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;
