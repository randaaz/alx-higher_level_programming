#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length -1;
  let i = 0;
  while ((l - 1) > 0) {
    let temp = list[l];
    list[l] = list[i];
    list[i] = temp;
    i++;
    l--;
  }
  return list;
};
