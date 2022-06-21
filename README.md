# Coding Challenge

Technical Asessment - DareData Engineering Interview

## Description

This project consist of three main tasks:
 1. Recursively lists all files and file sizes in an arbitrary directory and saves this output to a file in a format that can be read by a pandas dataframe (in a bash script)
 2. Loads the output file from the bash script into a pandas dataframe and calculates and print out the
   - average file size
   - the biggest file
   - the smallest file
   - histogram of file sizes
 3. Creates a HTTP python server that:
   - accepts a zip file that is a directory
   - uses the previously created bash and python scripts on the uploaded directory
   - returns the output in a json format

## Getting Started

### Prerequisites
* bash
* Linux

##### Python Libs
* Numpy
* Pandas
* Zipfile
* json
* sys
* os
* cgi
 
### Executing program

The first task (bash script: "script.sh") can be run either on Linux or Windows (For windows can be Git bash for example).

For the seconde task (python script: "pandas_script.py") in order to see the histogram plot it is necessary to run the code on a python interpreter.

The third task (HTTP python server: "server.py") needs to be run on Linux.

#### Step by Step
##### Bash script 
1. Open a terminal where you have saved the "script.sh" file and write "./script.sh path_of_the_directory" (Git bash on Windows) or "bash script.sh path_of_the_directory (Linux)"
2. An output file with the results called "directory_stats.txt" will be exported in the current folder where the terminal was initiated 

##### Python script
1. Open a python interpreter and run pandas_script.py. The python file "functions.py" needs to be in the same folder as pandas_script.
2. Results will be printed out. 

##### Python HTTP Server script (only runs with Linux)
1. Open a terminal and run python3 server.py. 
2. It will print out the link to the server.
3. Upload zipfile and write password "process".
4. Output in a JSON format will be printed. 

## Authors

Agustina Ravettino 
