#!/usr/bin/node
/* Javascript using array of string and a loop */
const args = process.argv;
const num = Number(args[2]);

if (isNaN(num) === true) {
  console.log('Missing size');
}

if (num > 0) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
