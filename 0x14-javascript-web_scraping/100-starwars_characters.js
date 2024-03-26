#!/usr/bin/node

const require = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
require.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const da = JSON.parse(body);
  const d = da.characters;
  for (const i of d) {
    require.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const da1 = JSON.parse(body1);
      console.log(da1.name);
    });
  }
});
