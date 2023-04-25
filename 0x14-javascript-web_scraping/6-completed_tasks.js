#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) console.error(err);
  if (res.statusCode === 200) {
    const resData = JSON.parse(body);
    // console.log(typeof res_data)
    const _obj = {};
    const arr = [];
    resData.forEach((data) => {
      if (data.completed === true) {
        arr.push(data.userId);
      }
    });
    arr.forEach(function (x) { _obj[x] = (_obj[x] || 0) + 1; });
    console.log(_obj);
  }
});
