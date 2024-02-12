#!/usr/bin/node
//script that prints x times “C is fun”
let x = Math.floor(Number(process.argv[2]));
let i;
if (isNaN(x)) {
    console.log("Missing number of occurrences");
}
else {
    for (i = 0; i < x; i++) {
        console.log("C is fun");
    }
}
