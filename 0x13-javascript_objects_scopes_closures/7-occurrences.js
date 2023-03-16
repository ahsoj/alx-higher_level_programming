#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((occ) => occ === searchElement).length;
};
