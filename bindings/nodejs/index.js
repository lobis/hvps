const {PythonShell} = require('python-shell');
const {execSync} = require('child_process');

function getPythonVersion() {
    const command = 'python --version';
    try {
        return execSync(command).toString().trim();
    } catch (err) {
        console.error(`Error executing command (${command}): ${err}`);
        throw err;
    }
}

function getPythonPath() {
    const command = 'python -c "import sys; print(sys.executable)"';
    try {
        return execSync(command).toString().trim();
    } catch (err) {
        console.error(`Error executing command (${command}): ${err}`);
        throw err;
    }
}

function getPackageVersion() {
    const command = 'python -m hvps --version';
    try {
        return execSync(command).toString().trim();
    } catch (err) {
        throw new Error(`Error executing command (${command}). Please make sure the package is installed.`);
    }
}


function run(args, callback) {
    const pythonVersion = getPythonVersion();
    console.log('Python version:', pythonVersion);

    const pythonPath = getPythonPath();
    console.log('Python path:', pythonPath);

    // print package version
    const packageVersion = getPackageVersion();
    console.log('Package version:', packageVersion);
}

module.exports = run;
