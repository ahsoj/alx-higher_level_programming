#!/usr/bin/node

exports.esrever = function (list) {
  const out = [];
  const len = list.length;
  for (let i = 0; i < len; i++) {
    out.push(list.pop());
  }
  return out;
};
