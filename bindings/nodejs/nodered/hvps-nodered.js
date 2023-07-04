import { ExecutionContext } from "hvps";

module.exports = function (RED) {
    function HVPS(config) {
        RED.nodes.createNode(this, config);
        const node = this;
        node.on('input', function (msg) {
            msg.payload = msg.payload.toLowerCase();
            node.send(msg);
        });
    }

    RED.nodes.registerType("hvps", HVPS);
}
