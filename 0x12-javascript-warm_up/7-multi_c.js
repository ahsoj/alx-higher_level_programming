#!/usr/bin/node

const processArgv = process.argv.slice(2);

if (!processArgv[0]) {
	console.log('Missing number of occurrences');
} else if (processArgv[0] > 0) {
	for (let i = 1; i <= processArgv; i++) {
		console.log('C is fun');
	}
}
