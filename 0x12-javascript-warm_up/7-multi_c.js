#!/usr/bin/node
//script that prints x times “C is fun”
let a = Math.floor(Number(process.argv[2]));
let i;
if (isNaN(a)) {
    console.log("Missing number of occurrences");
}
else {
    for (i = 0; i < a; i++) {
        console.log("C is fun");
    }
}
