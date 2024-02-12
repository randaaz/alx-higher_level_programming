#!/usr/bin/node
const arg = process.argv.lenght;
arg === 2 ? console.log("No argument") : arg === 3 ? console.log("Argument found") : console.log("Arguments found");
