#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body).results;
    let __count = 0;
    for (const index in responseJSON) {
      const res = responseJSON[index].characters;
      for (const _index in res) {
        //  console.log(res[_index])
        if (res[_index].includes('18')) {
          __count++;
        }
      }
    }
    console.log(__count);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
