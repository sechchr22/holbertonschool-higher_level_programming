#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  let i;
  if (number < 0) {
    for (i = 0; i > number; i--) {
    }
    i++;
  } else {
    for (i = 0; i <= number; i++) {
    }
  }
  theFunction(i);
};
