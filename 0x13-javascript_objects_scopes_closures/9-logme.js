#!/usr/bin/node

let node = 0;

exports.logMe = function (item) {
  console.log(`${node}: ${item}`);
  node++;
};
