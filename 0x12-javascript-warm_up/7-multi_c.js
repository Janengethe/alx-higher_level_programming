#!/usr/bin/node
const myNum = parseInt(process.argv[2], 10);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  let i = myNum;
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
