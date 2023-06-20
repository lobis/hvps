const { ExecutionContext } = require('./index');
const yargs = require('yargs');

const cli = yargs
    .scriptName('hvps')
    .usage('$0 <cmd> [args]')
    .option('python', {
        description: 'Specify the Python path to run HVPS.',
        alias: 'p',
        type: 'string',
        default: 'python', // Set a default string value
    })
    .help()
    .alias('h', 'help')
    .argv;

// check python is available
const context = new ExecutionContext(cli.python);
context.print();

// Get the remaining arguments as a string
const remainingArgs = cli._.join(' ');
// these should be passed to the python code. TODO: not working!

context.run(remainingArgs);
