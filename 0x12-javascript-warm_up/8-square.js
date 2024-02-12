#!/usr/bin/node
let x = Math.floor(Number(process.argv[2]));
let j;

if (isNaN(x)) {
    console.log('Missing size');
}
else {
    for (i = 0; i < x; i++) {
        let a = "";
        for (j = 0; j < x; j++) {
            a += "X";
        }
        console.log(a);

    }
}
