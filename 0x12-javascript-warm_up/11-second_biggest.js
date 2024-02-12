#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arg = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[arg.length - 2]);
}
