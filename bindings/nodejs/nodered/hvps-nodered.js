hvps = require('hvps')

module.exports = function (RED) {
    function HVPS(config) {
        RED.nodes.createNode(this, config);
        const node = this;
        context = new hvps.ExecutionContext("/usr/bin/python");
        node.on('input', function (msg) {
            msg.payload = context.run(msg.payload);
            node.send(msg);
        });
    }

    RED.nodes.registerType("hvps", HVPS);
}
