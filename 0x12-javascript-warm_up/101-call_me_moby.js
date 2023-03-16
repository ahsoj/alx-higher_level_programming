#!/usr/bin/node

exports.callMeMoby = function (n, func) {
  for (let i = 1; i <= n; i++) {
    func();
  }
};
