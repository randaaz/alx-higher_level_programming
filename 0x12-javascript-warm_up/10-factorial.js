#!/usr/bin/node
// script that prints the addition of 2 integers
function factorial(a) {
  if (a === 1 || isNaN(a)) {
    return (1);
  }
  return a * factorial(a - 1);
}
