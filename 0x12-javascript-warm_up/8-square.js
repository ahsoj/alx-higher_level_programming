#!/usr/bin/node

const processArgv = process.argv.slice(2);
let x = 'X';
if (!processArgv[0] || isNaN(processArgv[0])) {
	console.log('Missing size');
} else {
	for (let i = 1; i <= processArgv[0]; i++) {	
		for (let j = 1; j <= processArgv[0]; j++) {
			process.stdout.write(x + '');
		}
		console.log('');
	}
}
