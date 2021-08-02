#!/usr/bin/node

const argmnt = parseInt(process.argv[2], 10);
if (isNaN(argmnt)) {
  console.log('Missing number of occurrences');
} else {
  let i = argmnt;
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
