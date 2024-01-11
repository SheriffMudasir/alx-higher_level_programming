#!/usr/bin/node
const { argv } = require('node:process');
function secondBiggest (num) {
  if (argv.length <= 2) {
    return 0;
  }

  const sortedNumbers = argv.slice(2).map(Number).sort((a, b) => b - a);

  return sortedNumbers[1];
}
const secondNum = secondBiggest(argv);
console.log(secondNum);
