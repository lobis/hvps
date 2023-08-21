hvps = require('hvps')

module.exports = function (RED) {
    function HVPS(config) {
        this.ports = config.ports
        this.port = config.port
        this.baudrate = config.baudrate
        this.hvps = config.hvps
        this.module = config.module
        this.channel_mode = config.channel_mode
        this.channel = config.channel
        this.test = config.test
        this.command = config.command

        RED.nodes.createNode(this, config);
        const node = this;
        let context = new hvps.ExecutionContext("/usr/bin/python");

        node.on('input', function (msg) {

            // Command building
            let command;
            if (config.ports) {
                command = "--ports";
            } else {
                command = `--port ${config.port} --baud ${config.baudrate}`;
                if (config.channel) {
                    command += ` --channel ${config.channel}`;
                }
                if (config.test) {
                    command += " --test";
                }
                command += ` ${config.hvps}`;
                if (config.hvps === "caen") {
                    command += ` --module ${config.module}`;
                }
                command += ` ${config.command}`;
            }

            this.warn(command)
            msg.payload = context.run(command);
            node.send(msg);
        });

    }

    RED.nodes.registerType("hvps", HVPS, {
        // Define the node properties and defaults here
        settings: {
            sampleNodeColour: {
                value: "red",
                exportable: true
            }
        }
    });
}
