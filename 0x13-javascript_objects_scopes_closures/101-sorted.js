#!/usr/bin/node
const dict = require('./101-data').dict;

const tl = Object.entries(dict);
const v = Object.values(dict);
const vu = [...new Set(v)];
const nd = {};
for (const j in vu) {
  const list = [];
  for (const i in tl) {
    if (tl[i][1] === vu[j]) {
      list.unshift(tl[i][0]);
    }
  }
  nd[vu[j]] = list;
}
console.log(nd);
