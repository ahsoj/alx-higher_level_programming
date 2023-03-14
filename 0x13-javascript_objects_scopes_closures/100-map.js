#!/usr/bin/node

const list = require('./100-data').list;

const newList = [];
list.map((node, index) => newList.push(node * index));
console.log(list);
console.log(newList);
