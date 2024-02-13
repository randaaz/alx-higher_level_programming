#!/usr/bin/node
const list = require('./100-data').list;
const nl = list.map(function (n, idx) {
  return n * idx;
});

console.log(list);
console.log(nl);
