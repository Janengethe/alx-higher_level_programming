#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Error: ' + response.statusCode);
  }
});
