#!/usr/bin/node

let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
const fs = require('fs');// create fs module function through keyword require
let textA = fs.readFileSync(fileA, 'utf8');//read the original content in fileA
let textB = fs.readFileSync(fileB, 'utf8');//read the original content in fileB
fs.writeFileSync(fileC, textA + textB);//Write content
