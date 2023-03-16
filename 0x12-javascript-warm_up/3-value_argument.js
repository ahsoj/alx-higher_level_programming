#!/usr/bin/node

const processArgv = process.argv.slice(2);

if (processArgv[0] === undefined) {
  console.log('No argument');
} else {
  for (const i of processArgv) {
    console.log(i);
  }
}
