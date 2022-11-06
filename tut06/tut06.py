from ctypes import sizeof                                           # Importing libraries
import pandas as pd
import csv
import os
from datetime import datetime, timedelta
import openpyxl
from openpyxl import workbook,load_workbook

from datetime import datetime
start_time = datetime.now()

def attendance_report():                                            # Function to process input files
    try:
        df=pd.read_csv('input_registered_students.csv')             # Reading input_registered_students file
    except:
        print('Input file error')

    rolls={}                                                        # Mapping each roll no. with an integer
    roll_numbers=[]                                                 # List containing all registered roll numbers
    name={}                                                         # Dictionary for mapping roll numbers to names of students
    date_mapping={}                                                 # Dictionary for mapping each lecture falling on Monday and Thursday to an integer
    
    for i in df.index:                                              # Iterating through the dataframe row-wise
        roll_no=df['Roll No'][i]                                    # Roll no. of student  
        roll_numbers.append(df['Roll No'][i])                       # Appending roll no. of student in the list 'roll_numbers'
        rolls[roll_no]=i                                            # Mapping roll numbers to integers
        name[roll_no]=df['Name'][i]                                 # Mapping roll numbers to names of students
    n=len(rolls)                                                    # Finding number of roll numbers
    
            
        
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()                                                                                     # Calling the function to do the whole process




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))