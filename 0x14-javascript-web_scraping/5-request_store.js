#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, res, body) {
  if (err) console.error(err);
  if (res.statusCode === 200) {
    fs.writeFile(process.argv[3], String(body), function (err) {
      if (err !== null) console.error(err);
    });
  }
});
