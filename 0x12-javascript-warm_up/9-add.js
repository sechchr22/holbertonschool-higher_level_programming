#!/usr/bin/node
/* Javascript using array of string and a loop */
const args = process.argv;
const num1 = Number(args[2]);
const num2 = Number(args[3]);

function add (a, b) {
  if (isNaN(num1) === true) {
    return NaN;
  }
  if (isNaN(num2) === true) {
    return NaN;
  }
  return (a + b);
}

console.log(add(num1, num2));
