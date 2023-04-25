const { spawn } = require('child_process');

const process = spawn('python3', ['/Users/danielhaycraft/Desktop/my_program/alert.py']);

process.on('exit', (code, signal) => {
    console.log(`Script exited with code ${code} and signal ${signal}`);
});
