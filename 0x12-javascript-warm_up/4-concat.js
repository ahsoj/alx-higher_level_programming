#!/usr/bin/node

const processArgv = process.argv.slice(2);
console.log(`${processArgv[0] || undefined} is ${processArgv[1] || undefined}`);
