#!/usr/bin/node

const request = require('request');

const arg = process.argv[2];
const API = `https://swapi-api.alx-tools.com/api/films/${arg}`;

request(API, function (err, res, body) {
  if (err) console.error(err);
  if (res.statusCode === 200) {
    const resData = JSON.parse(body).characters;
    resData.forEach((character) => {
      request(character, (err, resp, bod) => {
        if (err) console.error(err);
        if (resp.statusCode === 200) {
          console.log(JSON.parse(bod).name);
        }
      });
    });
  }
});
