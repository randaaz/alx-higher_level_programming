#!/usr/bin/node
//script that prints a message depending of the number of arguments
let arg = process.argv;
arg === 2 ? console.log("No argument") : arg === 3 ? console.log("Argument found") : console.log("Arguments found");
