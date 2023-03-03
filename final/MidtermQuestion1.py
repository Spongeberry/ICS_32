''' You are expected to comment your code. At a minimum if statements and for loops
 need at least 1 line of comment to explain what the loop does'''

#------------IMPORT ANY LIBRARIES YOU NEED HERE-----------
from pathlib import Path
import os
#---------- CREATE YOUR CUSTOM EXCEPTION HERE-------------
class NotAValidDirectory(Exception):
   print("Exception Found")

'''Write a function that reads all the text files (.txt extension)
located in the directory myPath and writes it to a new Combined
file created in the current directory. It returns the values
defined below. You will raise a custom exception called "NotAValidDirectory"if the directory provided
is not a directory.(Note you will need to create the custom exception called NotAValidDirectory yourself.
'''
def combineFiles(directoryName,combinedFilename):
   '''Use these provided variables and update them with the information described in the comment
   associated with each variable.'''
   totalFileCount = 0 #contains the total number of files in the directory provided
   textFileCount = 0 # provides the number of text files found in the directory
   combinedFileLineCount = 0 #provides the total number of lines in the final combined file

  #----------------YOUR FUNCTION CODE STARTS HERE--------------- 
   myPath = os.getcwd()
   p = Path(myPath)
   if os.path.isdir(directoryName):#check if the path is a directory and matches the name
      open(os.path.join(directoryName, combinedFilename), mode = "w")
      for file in p.iterdir():#iterate through files within that directory
         if file.endswith(".txt"):#filter for files ending within txt
            A = file.open("r")
            textFileCount += 1
            totalFileCount += 1
            while True:
               returned_string = A.readline()
               with open (combinedFilename, "w") as B:
                  B.write(returned_string)
            with open (combinedFilename, "r") as C:
               C_list = C.readlines()
               combinedFileLineCount = len(C_list)
         else:
            totalFileCount += 1    
   else:
      raise NotAValidDirectory

   #------------------- YOUR FUNCTION CODE ENDS HERE------------------   
   return totalFileCount, textFileCount,combinedFileLineCount


'''This will run your program. You should only add code to
handle exceptions that are raised. Any exceptions found will only
display "Exception Found" and end program execution. The program will
only run once.(Does not automatically restart)'''
if __name__ == "__main__":
   directoryName = input("Directory: ")
   combinedFilename = input ("Combined Filename: ")
   print(combineFiles(directoryName,combinedFilename))
