#!/usr/bin/node
// script that prints the addition of 2 integers
function add(a, b) {
  return (a + b);
}
console.log(add(Math.floor(Number(process.argv[2])), Math.floor(Number(process.argv[3]))));
