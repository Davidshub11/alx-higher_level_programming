#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // Convert arguments to integers

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a); // Sort arguments in descending order
  console.log(sortedArgs[1]);
}

