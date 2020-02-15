#!/usr/bin/node
/* Javascript using array of string and a loop */
let numbers = [];
let j = 2;

if ((process.argv.length === 2) || (process.argv.length === 3)) {
  console.log(0);
  return;
}

for (i = 0; i < (process.argv.length - 2); i++) {
  numbers[i] = Number(process.argv[j]);
  j++;
}

function lomutos_partition (arr, low, high)
{
  let buff;
  let pivot = arr[high];
  let i = (low - 1);

  for (let j = low; j <= high; j++) {
    if (arr[j] <= pivot) {
      i++;
      if (i != j)
      {
        buff = arr[i];
        arr[i] = arr[j];
        arr[j] = buff;
      }        
    }
  }
  return(i);
}

function quickSort(arr, low, high) {
  let pi;
  if (low < high)
  {
    pi = lomutos_partition(arr, low, high);
    
    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, high);
  }
    return(arr);
}

console.log(numbers.sort());
console.log(quickSort(numbers, numbers[0], numbers[numbers.lenght - 1]));
