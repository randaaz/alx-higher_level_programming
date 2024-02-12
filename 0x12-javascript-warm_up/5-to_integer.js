#!/usr/bin/node
// a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
console.log(isNaN(parseInt(process.argv[2])) ? 'Not a number': 'My number: ' + parseInt(process.argv[2]));
