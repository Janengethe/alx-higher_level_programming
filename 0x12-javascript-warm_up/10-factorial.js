#!/usr/bin/node
const myNum = parseInt(process.argv[2], 10);
function factorial (myNum) {
  if (isNaN(myNum) || myNum === 0) {
    return (1);
  }
  return (myNum * factorial(myNum - 1));
}
console.log(factorial(myNum));
