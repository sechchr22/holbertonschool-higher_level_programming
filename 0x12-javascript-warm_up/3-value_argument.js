#!/usr/bin/node
/* using process.arg */
if (!(process.argv[2])) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
