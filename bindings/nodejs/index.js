const {execSync} = require('child_process');
const packageJson = require('./package.json');
const version = packageJson.version;

class ExecutionContext {
    constructor(pythonPath) {
        this.python = pythonPath;
        // check if python path is correct and use absolute path
        this.python = this.getPythonPath();

        // check if the hvps package is available
        this.getPackageVersion();
    }

    getPythonVersion() {
        const command = `${this.python} -c "import sys; print(sys.version)"`;
        try {
            return execSync(command, {encoding: 'utf-8'}).trim();
        } catch (err) {
            console.error(`Error executing command (${command}): ${err}`);
            throw err;
        }
    }

    getPythonPath() {
        const command = `${this.python} -c "import sys; print(sys.executable)"`;
        try {
            return execSync(command, {encoding: 'utf-8'}).trim();
        } catch (err) {
            console.error(`Error executing command (${command}): ${err}`);
            throw err;
        }
    }

    getPackageVersion() {
        const command = `${this.python} -m hvps --version`;
        let pythonPackageVersion;
        try {
            pythonPackageVersion = execSync(command, {encoding: 'utf-8'}).trim();
        } catch (err) {
            throw new Error(`Error executing command (${command}). Please make sure the HVPS python package is installed. To install a specific version, run: '${this.python} -m pip install hvps==${version}'`);
        }

        if (pythonPackageVersion !== version) {
            throw new Error("Mismatch between the version of the HVPS python package and the version of the HVPS nodejs package.");
        }

        return pythonPackageVersion;
    }

    print() {
        console.log(`Python version: ${this.getPythonVersion()}`);
        console.log(`Python path: ${this.getPythonPath()}`);
        console.log(`Package version: ${this.getPackageVersion()}`);
    }

    // run method should call the python script with the arguments
    run(args) {
        const command = `${this.python} -m hvps ${args}`;
        try {
            return execSync(command, {encoding: 'utf-8'}).trim();
        } catch (err) {
            throw new Error(`Error executing command (${command}): ${err}`);
        }
    }
}

module.exports = {
    ExecutionContext,
};
