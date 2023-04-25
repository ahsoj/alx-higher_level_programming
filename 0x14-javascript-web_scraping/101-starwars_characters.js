#!/usr/bin/node

const request = require('request');

const arg = process.argv[2];
const API = `https://swapi-api.alx-tools.com/api/films/${arg}`;

request(API, function (err, res, body) {
  if (err) console.error(err);
  if (res.statusCode === 200) {
    const resData = JSON.parse(body).characters;
    sortAsc(resData, 0);
  }
});

function sortAsc (wName, i) {
  request(wName[i], (err, resp, bod) => {
    if (err) console.error(err);
    if (resp.statusCode === 200) {
      console.log(JSON.parse(bod).name);
      if (i + 1 < wName.length) {
        sortAsc(wName, i + 1);
      }
    }
  });
}
