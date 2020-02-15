#!/usr/bin/node
/* Javascript using array of string and a loop */
const numbers = [];
let j = 2;

function swap (items, leftIndex, rightIndex) {
  const temp = items[leftIndex];
  items[leftIndex] = items[rightIndex];
  items[rightIndex] = temp;
}

function partition (items, left, right) {
  const pivot = items[Math.floor((right + left) / 2)];
  let i = left;
  let j = right;

  while (i <= j) {
    while (items[i] < pivot) {
      i++;
    }
    while (items[j] > pivot) {
      j--;
    }
    if (i <= j) {
      swap(items, i, j);
      i++;
      j--;
    }
  }
  return i;
}

function quickSort (items, left, right) {
  let index;

  if (items.length > 1) {
    index = partition(items, left, right);
    if (left < index - 1) {
      quickSort(items, left, index - 1);
    }
    if (index < right) {
      quickSort(items, index, right);
    }
  }
  return items;
}

if ((process.argv.length === 2) || (process.argv.length === 3)) {
  console.log(0);
} else {
  for (let i = 0; i < (process.argv.length - 2); i++) {
    numbers[i] = Number(process.argv[j]);
    j++;
  }
  const result = quickSort(numbers, 0, numbers.length - 1);
  console.log(result[result.length - 2]);
}
