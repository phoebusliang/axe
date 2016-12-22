"use strict";
var http = require('http');
var process = require('child_process');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function cleanKeychain(uuid) {
  process.exec('/Users/twe/Documents/fbsimctl/fbsimctl ' + uuid + ' clear_keychain com.rea-group.reapa.internal',
    function(err, stdout, stderr) {
      if (err) {
        sleep(3000).then(() => {
          console.log("Take 3 seconds...")
        });
        console.log("\n" + stderr);
      } else {
        console.log(stdout);
        // console.log("Clean keychain successfully for " + uuid + ", " + bundleId);
      }
    });
}

function cleanAllKeychains() {
  process.exec('/Users/twe/Documents/fbsimctl/fbsimctl --state=booted clear_keychain com.rea-group.reapa.internal',
    function(err, stdout, stderr) {
      if (err) {
        sleep(3000).then(() => {
          console.log("Take 3 seconds...")
        });
        console.log("\n" + stderr);
      } else {
        console.log(stdout);
        // console.log("Clean keychains successfully for all simulators!");
      }
    });
}

function uninstallApp(uuid) {
  process.exec('/Users/twe/Documents/fbsimctl/fbsimctl ' + uuid + ' uninstall com.rea-group.reapa.internal', function(
    err, stdout, stderr) {
    if (err) {
      sleep(3000).then(() => {
        console.log("Take 3 seconds...")
      });
      console.log("\n" + stderr);
    } else {
      console.log(stdout);
      // console.log("Clean keychains successfully for all simulators!");
    }
  });
}

function installApp(uuid) {
  process.exec('/Users/twe/Documents/fbsimctl/fbsimctl ' + uuid + ' install /Users/twe/Downloads/RESI-Internal.app',
    function(err, stdout, stderr) {
      if (err) {
        sleep(3000).then(() => {
          console.log("Take 3 seconds...")
        });
        console.log("\n" + stderr);
      } else {
        console.log(stdout);
        // console.log("Clean keychains successfully for all simulators!");
      }
    });
}

const PORT = 8080;

function handleRequest(request, response) {
  // var uuid = request.url.split('/')[2];
  // var bundleId = request.url.split('/')[3];
  // if (request.url.split('/').length <= 2) {
  //     cleanAllKeychains();
  // } else {
  //     cleanKeychain(uuid, bundleId);
  // }
  if (request.url.indexOf("clean") > -1) {
    var uuid = request.url.split('/')[2];
    cleanKeychain(uuid);
  }

  if (request.url.indexOf("cleanall") > -1) {
    cleanAllKeychains();
  }

  if (request.url.indexOf("appinstall") > -1) {
    var uuid = request.url.split('/')[2];
    installApp(uuid);
  }

  if (request.url.indexOf("appuninstall") > -1) {
    var uuid = request.url.split('/')[2];
    uninstallApp(uuid);
  }

  console.log(request.url);
  response.end('Key chains ' + request.url);
}

var server = http.createServer(handleRequest);

server.listen(PORT, function() {
  console.log("Server listening on: http://localhost:%s", PORT);
});
