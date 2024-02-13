#!/usr/bin/node
let con = 0;

exports.logMe = function (item) {
  console.log(con + ': ' + item);
  con++;
};
