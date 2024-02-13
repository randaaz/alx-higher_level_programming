#!/usr/bin/node
const files = require('files');

const fa = files.readFileSync(process.argv[2]).toString();
const sa = files.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], fa + sa);
