#!/usr/bin/node

const processArgv = process.argv.slice(2);
if (!processArgv[0] || isNaN(processArgv[0])) {
	console.log('Not a number');
} else {
	console.log('My number:', Math.round(processArgv[0]))
}
