#!/usr/bin/node

const argmnt = parseInt(process.argv[2], 10);
if (isNaN(argmnt)) {
  console.log('Missing size');
} else {
  for (let i = argmnt; i > 0; i--) {
      console.log('X'.repeat(argmnt));
  }
}
