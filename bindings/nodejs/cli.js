const {ExecutionContext} = require('./index');
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

// print all arguments, options, etc.
const userInput = process.argv.slice(2).join(' ');
console.log(`User Input: ${userInput}`);

// define an array of flags to exclude
const excludedFlags = ['--python', '-p']; // Add any other flags to exclude here

// remove the excluded flags and their values from the arguments
const excludedFlagsPattern = excludedFlags.map((flag) => `(?:${flag}(?:=[^\\s]+|\\s+[^-\\s]+)?)`).join('|');
const remainingArgs = userInput.replace(new RegExp(excludedFlagsPattern, 'g'), '').trim();

console.log(`Remaining Args: ${remainingArgs}`);

context.run(remainingArgs);
