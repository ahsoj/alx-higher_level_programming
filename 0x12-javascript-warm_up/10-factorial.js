#!/usr/bin/node

const processArgv = process.argv.slice(2);
function factorial (n) {
  let fac = 1;
  for (let i = 1; i <= n; i++) {
    fac *= i;
  }
  return fac;
}

if (!processArgv[0]) {
  console.log(1);
} else {
  console.log(factorial(processArgv[0]));
}
