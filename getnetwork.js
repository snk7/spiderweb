var page = require('webpage').create();
system = require('system');
var url = system.args[1];
page.onResourceRequested = function (request) {
    console.log('Request ' + JSON.stringify(request, undefined, 4));
    //phantom.exit();
};
page.open(url);
phantom.exit();