const { execSync } = require('child_process');


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
            return execSync(command, { encoding: 'utf-8' }).trim();
        } catch (err) {
            console.error(`Error executing command (${command}): ${err}`);
            throw err;
        }
    }

    getPythonPath() {
        const command = `${this.python} -c "import sys; print(sys.executable)"`;
        try {
            return execSync(command, { encoding: 'utf-8' }).trim();
        } catch (err) {
            console.error(`Error executing command (${command}): ${err}`);
            throw err;
        }
    }

    getPackageVersion() {
        const command = `${this.python} -m hvps --version`;
        try {
            return execSync(command, { encoding: 'utf-8' }).trim();
        } catch (err) {
            throw new Error(`Error executing command (${command}). Please make sure the package is installed.`);
        }
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
            return execSync(command, { encoding: 'utf-8' }).trim();
        } catch (err) {
            throw new Error(`Error executing command (${command}): ${err}`);
        }
    }
}

module.exports = {
    ExecutionContext,
};
