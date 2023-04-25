const { spawn } = require('child_process');

// Source the config.sh file
const source = spawn('sh', ['-c', 'source /Users/danielhaycraft/Desktop/my_program/config.sh && env']);
let env = '';
source.stdout.on('data', (data) => {
  env += data;
});

source.on('close', (code) => {
  // Spawn the child process with the updated environment variables
  const process = spawn('python3', ['/Users/danielhaycraft/Desktop/my_program/alert.py'], {
    env: Object.assign({}, process.env, env),
  });

  process.on('exit', (code, signal) => {
    console.log(`Script exited with code ${code} and signal ${signal}`);
  });
});