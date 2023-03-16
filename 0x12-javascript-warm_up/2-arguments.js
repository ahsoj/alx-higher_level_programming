#!/usr/bin/node

const processArgv = process.argv.slice(2);

if (processArgv.length === 0) {
  console.log('No argument');
} else if (processArgv.length === 1) {
  console.log('Argument found');
} else if (processArgv.length > 1) {
  console.log('Arguments found');
}
