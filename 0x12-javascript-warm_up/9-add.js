#!/usr/bin/node

const processArgv = process.argv.slice(2);
function add (a, b) {
  console.log(a + b);
}

if (!processArgv[0] || processArgv[0] && !processArgv[1]) {
  console.log('NaN');
} else {
  add(Number(processArgv[0]), Number(processArgv[1]));
}
