

const { append } = require('gulp-insert')
const { request } = require('http')
var https =require('https')
const { Body } = require('node-fetch')
const { default: fetch } = require('node-fetch')
var red = require('./package.json')
var url="https://query1.finance.yahoo.com/v8/finance/chart/AAPL?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance"

const options = {
  "method": "GET",
  "hostname": "query1.finance.yahoo.com",
  "porct": null,
  "path": "/v8/finance/chart/AAPL?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance%22",
  "headers": {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)"
  }
};

var req=https.request(options,(res) => {
  console.log('statusCode:', res.statusCode);
  console.log('headers:', res.headers);

  res.on('data', (d) => {
    process.stdout.write(d);
  });
});
console.log(req)
req.end()
//'2ec0e15a0f074ba88d81d06785760a69'
//https://newsapi.org/v2/everything?q=bitcoin&language=en&from=2022-08-16&sortBy=publishedAt&apiKey=2ec0e15a0f074ba88d81d06785760a69