#!/usr/bin/env node

const { stdin, stdout } = process;

stdout.write('Welcome to Holberton School, what is your name?\n');

stdin.on('readable', () => {
  const name = stdin.read();
  if (name) {
    stdout.write(`Your name is: ${name}`);
  }
});

stdin.on('end', () => {
  stdout.write('This important software is now closing\n');
});
