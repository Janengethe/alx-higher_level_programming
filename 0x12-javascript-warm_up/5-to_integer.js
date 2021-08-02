#!/usr/bin/node

const argmnt = parseInt(process.argv[2], 10);
if (isNaN(argmnt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argmnt);
}
