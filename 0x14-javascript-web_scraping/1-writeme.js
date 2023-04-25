#!/usr/bin/node

const fs = require('fs');

fs.writeFile(process.argv[2], String(process.argv[3]), function (err) {
  if (err) {
    console.log(err);
  }
});
