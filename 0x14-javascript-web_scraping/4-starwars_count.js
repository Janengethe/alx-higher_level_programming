#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const result = JSON.parse(body).results;
    let count = 0;
    for (const i in result) {
      const chars = result[i].characters;
      for (const c in chars) {
        if (chars[c].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Erorr: ' + response.statusCode);
  }
});
