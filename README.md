[![CI](https://github.com/nogibjj/skye-assignment-8/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/skye-assignment-8/actions/workflows/cicd.yml)
# Performance Comparison of Rust and Python Scripts
 This project is designed to compare the runtime and memory usage of Python and Rust implementations of a task. The project includes: 
 1. A Python script (src) for the task.
 2. A Rust executable (mylib). 
 3. A comparison script (compare.sh) that runs both implementations, measuring and reporting runtime and memory usage.
 
-----------------------------------------
# Perfomance Report for python_script
Max memory usage by python_script:   1120 KB
Processing time for python_script:0.24
-----------------------------------------
 
 
-----------------------------------------
# Perfomance Report for rust_executable
Max memory usage by rust_executable:   1120 KB
Processing time for rust_executable:1.28
-----------------------------------------
 
# Getting Started
Clone the repository and navigate into the project directory.
Ensure all dependencies are installed (see Requirements).

# Requirements
## System Requirements
- UNIX-like operating system (Linux, macOS)
- Bash shell for running compare.sh
- Rust (installed via Rustup)
- Python 3 and any required libraries for your_script.py
## Required Scripts
- Rust Script: This script should be compiled as your_rust_executable.
- Python Script: Place your Python script as your_script.py.
- Comparison Script: compare.sh is provided for comparing the resource usage.

# Project Structure
```{bash}
project/
├── compare.sh             # Bash script to compare performance and resource usage
├── your_rust_executable   # Compiled Rust executable
├── your_script.py         # Python script
└── README.md              # Documentation
```
Usage
1. Compile the Rust Script
Before running compare.sh, compile the Rust program if it hasn't already been compiled:
```{bash}
# In the project directory
make rust-run
```
2. Run the Comparison Script
```{bash}
chmod +x compare.sh
./compare.sh "python3 your_script.py" "Python Script"
./compare.sh "./your_rust_executable" "Rust Executable"
```
3. Capture Output to a File
To save the results in a file (e.g., results.md):
```{bash}
./compare.sh "python3 your_script.py" "Python Script" > results.md
./compare.sh "./your_rust_executable" "Rust Executable" >> results.md
```