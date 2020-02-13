#!/usr/bin/node
/* Javascript using array of string and a loop */
const args = process.argv;
const num1 = Number(args[2]);

function factorial (a) {
  if (isNaN(a) === true || a === 0) {
    return 1;
  }

  return (factorial(a - 1) * a);
}

console.log(factorial(num1));
