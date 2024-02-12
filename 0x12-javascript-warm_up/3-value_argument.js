#!/usr/bin/node
//script that prints the first argument
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
