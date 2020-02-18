#!/usr/bin/node
/// Recangle class
const DadSquare = require('./5-square');
class Square extends DadSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === 'C') {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('C');
        }
        console.log('');
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
