#!/usr/bin/node
/* Javascript using array of string and a loop */
const numbers = [];
let j = 2;

if ((process.argv.length === 2) || (process.argv.length === 3)) {
  console.log(0);
} else {
  for (let i = 0; i < (process.argv.length - 2); i++) {
    numbers[i] = Number(process.argv[j]);
    j++;
  }
}

console.log(numbers.sort()[numbers.sort().length - 2]);
