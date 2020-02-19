#!/usr/bin/node
/// handling variable global scope

let count = 0;

exports.logMe = function (item) {
  console.log(count + ':', item);
  count++;
};
