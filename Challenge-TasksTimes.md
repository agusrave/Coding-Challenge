# Time taken for each task


### Create a bash script that

- recursively lists all files and file sizes in an arbitrary directory
- saves this output to a file in a format that can be read by a pandas dataframe

#### Solution:
 - I have generated a bash script "script.sh" that can be run specifying the directory path and will recursively go through the folder getting information about files names and file sizes in bytes. All that information is exported into a "txt" file wherever the terminal was opened. 
 -  - The script can read also file names and folder names that have spaces (It will replace those spaces with an underscore).

   ##### Time of each task
    1. Investigating and refreshing memory on how to code with bash and navigate through files and directories: 2 hours.
    2. Generating the base code: 1 hour.
    3. Debugging, cleaning and making some improvement details: 1 hour.
    4. Testing for different directories with different file names combinations: 1 hour.

### Write a python script that:
- load this file into a pandas dataframe and calcualte and print out the
   - average file size
   - the biggest file
   - the smallest file
   - histogram of file sizes
#### Solution:
- I generated a python function with file name argument that creates a pandas data frame and prints the different results requested.
   ##### Time of each task
   - Coding: 20 min
   - Debugging, cleaning and improving: 15 min
   

### Create an HTTP server in python that
   - accepts a zip file that is a directory
   - uses the previously created bash and python scripts on the uploaded directory
   - returns the output in a json format

#### Solution:
   ##### Time of each task
   - Investigating on how to do this task and work with python http server. (No experience before): whole day
   - Generating python code and gathering together the bash and pandas code: whole day 
   - Adapting bash and python code to work properly: 4 hours
   - Debugging, cleaning and improving: half day
  
### As part of the submission, identify any architectural or security issues as well as improvements that you would like to make in the future.
#### *Answer:

I could definitely improve security of the server: for example I could request the user to generate an user with account and password, check if the user is allowed to enter the server and send a token to allow access. 

Now the user needs only a password to acces the server. 

I could improve the visual interface of the web. I focused on getting the solution for the task so I did not spend time improving the web design.

Since this is my first time developing an http python server I believe there is lot more improvements I could make, not only to improve visuals 
but also to the architecture. 

I have no experience in http servers so I need to investigate more and find more ways to make this more efficient.

During the investigation on how to generate a server I noticed that I could use more professional tools such as flask.

Another improvement that I can think of is to give the user the option to download the JSON output.
Also I could improve the histogram chart from the python script. It is pretty simple. 
It would be great to be able to upload more directories, not only one. 


