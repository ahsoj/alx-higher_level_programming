#!/usr/bin/node

const processArgv = process.argv.slice(2)

if (!processArgv[0] || processArgv.length === 1) {
	console.log(0);
} else {
	console.log(Number(processArgv.sort().slice(-2,-1)));
}
