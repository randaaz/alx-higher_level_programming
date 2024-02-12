#!/usr/bin/node
//script that searches the second biggest integer in the list of arguments.
if (process.argv.lenght <= 3) {
  console.log(0);
}
let arg = process.argv.map(Number)
.slice(2, process.argv.lenght)
.sort((a, b) => a - b);
console.log(arg[arg.lenght - 2]);
