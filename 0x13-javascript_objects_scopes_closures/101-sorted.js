#!/usr/bin/node
const dict = require('./101-data').dict;

const r1 = Object.entries(dict);
const v = Object.values(dict);
const vu = [...new Set(v)];
const nd = {};
for (const j in vu) {
  const list = [];
  for (const i in r1) {
    if (r1[i][1] === vu[j]) {
      list.unshift(r1[i][0]);
    }
  }
  nd[vu[j]] = list;
}
console.log(nd);
