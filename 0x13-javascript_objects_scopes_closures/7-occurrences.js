#!/usr/bin/node
/// function that returns the number of ocurrences in a list
function nbOccurences (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
}

exports.nbOccurences = nbOccurences;
