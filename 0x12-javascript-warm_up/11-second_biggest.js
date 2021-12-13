#!/usr/bin/node
const myArgs = process.argv.slice(2);
function secondMax (arr) {
  if (arr.length <= 1) {
    return (0);
  } else {
    arr.sort((a, b) => a - b);
    arr.pop();
    return (arr.pop());
  }
}
console.log(secondMax(myArgs));
