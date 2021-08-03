#!/usr/bin/node
const Base = require('./5-square');

module.exports = class Square extends Base {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = this.height; i > 0; i--) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
