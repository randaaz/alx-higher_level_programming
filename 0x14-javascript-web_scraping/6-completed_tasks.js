#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const comp = {};
    const tas = JSON.parse(body);
    for (const i in tas) {
      const task = tas[i];
      if (task.comp === true) {
        if (comp[task.userId] === undefined) {
          comp[task.userId] = 1;
        } else {
          comp[task.userId]++;
        }
      }
    }
    console.log(comp);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
