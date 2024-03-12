#!/usr/bin/env node

const args = process.argv.slice(2); // Extracting command line arguments (excluding node and script name)

if (process.argv.length === 0) {
  console.log("No argument");
} else if (process.argv.length === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}

