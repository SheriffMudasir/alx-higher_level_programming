#!/usr/bin/node
const { argv } = require('node:process');

function factorial(n) { 
    if (n === NaN || n === 1 || n === 0) {
        return 1;
    } else { 
        return n * factorial(n - 1);
    }
}
fac = factorial(parseInt(argv[2]));
console.log(fac);
