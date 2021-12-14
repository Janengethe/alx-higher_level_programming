#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');// create fs module function through keyword require
const textA = fs.readFileSync(fileA, 'utf8');// read the original content in fileA
const textB = fs.readFileSync(fileB, 'utf8');// read the original content in fileB
fs.writeFileSync(fileC, textA + textB);// Write content
