#!/usr/bin/node
/// reverse list
exports.esrever = function (list) {
  let j = list.length - 1;
  for (let i = 0; i < list.length - 1; i++) {
    if (i === j || i > j) {
      return list;
    }
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    j--;
  }
};
