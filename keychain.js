"use strict";
var http = require('http');
var process = require('child_process');

function cleanKeychain(uuid, bundleId) {
  process.exec('/Users/twe/Documents/fbsimctl/fbsimctl ' + uuid + ' clear_keychain ' + bundleId, function(err, stdout,
    stderr) {
    if (err) {
      console.log("\n" + stderr);
    } else {
      console.log(stdout);
    }
  });
}

function cleanAllKeychains() {
  process.exec('/Users/twe/Documents/fbsimctl/fbsimctl --state=booted clear_keychain athome.lu.v3', function(err,
    stdout, stderr) {
    if (err) {
      console.log("\n" + stderr);
    } else {
      console.log(stdout);
    }
  });
}

const PORT = 8080;

function handleRequest(request, response) {
  var uuid = request.url.split('/')[2];
  var bundleId = request.url.split('/')[3];

  if (request.url.split('/').length <= 2) {
    cleanAllKeychains();
  } else {
    cleanKeychain(uuid, bundleId);
  }

  response.end('Key chains ' + request.url);
}

var server = http.createServer(handleRequest);

server.listen(PORT, function() {
  console.log("Server listening on: http://localhost:%s", PORT);
});
