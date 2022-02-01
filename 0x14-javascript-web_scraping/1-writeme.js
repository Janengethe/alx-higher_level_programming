#!/usr/bin/node

const filename = process.argv[2];
const cont = process.argv[3];
const fs = require('fs');
fs.writeFile(filename, cont, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
