#!/usr/bin/node
const Square = require('./4-rectangle');

module.exports = class Rectangle extends Square {
  constructor (size) {
    super(size, size);
  }
};
