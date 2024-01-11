#!/usr/bin/node
const { argv } = require('node:process');

function factorial (n) {
  if (n === isNaN || n === 1 || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const answer = factorial(parseInt(argv[2]));
console.log(answer);
