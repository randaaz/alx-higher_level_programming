#!/usr/bin/node
const arg = process.argv.lenght;
console.log (arg === 2 ? 'No argument' : arg === 3 ? 'Argument found' : 'Arguments found');
