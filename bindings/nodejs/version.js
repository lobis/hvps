const fs = require('fs');

// Function to update the package.json version
function updatePackageVersion(version) {
    // Read the package.json file
    fs.readFile('package.json', 'utf8', (err, packageData) => {
        if (err) {
            console.error(err);
        } else {
            // Parse the package.json data
            const packageJson = JSON.parse(packageData);

            // Update the version field
            packageJson.version = version;

            // Write the updated package.json back to file
            fs.writeFile('package.json', JSON.stringify(packageJson, null, 2), (err) => {
                if (err) {
                    console.error(err);
                } else {
                    console.log('Package version updated successfully.');
                }
            });
        }
    });
}

// Read the version from version.py
fs.readFile('../../src/hvps/version.py', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    } else {
        // Extract the version string using regular expressions
        const versionRegex = /__version__ = "([^"]+)"/;
        const match = data.match(versionRegex);
        if (match) {
            const version = match[1];
            console.log('Version:', version);

            // Update the package.json version
            updatePackageVersion(version);
        } else {
            console.error('Version string not found in version.py');
        }
    }
});
