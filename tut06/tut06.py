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
    
    del df
    df1=pd.read_csv('input_attendance.csv')                         # Reading input_attendace file 
    df = df1[df1['Attendance'].notnull()]                           # Removing the rows which have name as empty
    x=len(df)
    format="%d-%m-%Y"                                       # Formatting the date
    start=datetime.strptime(df['Timestamp'][0].split()[0],format)                 # Converting date string to date object supported by python
    end=datetime.strptime(df['Timestamp'][x-1].split()[0],format)
  
    datesRange = pd.date_range(start, end, freq='D')
    lectures=[]
    for i in range(len(datesRange)):
        if(datesRange[i].weekday()==0 or datesRange[i].weekday()==3):
            lectures.append(datesRange[i].strftime("%d-%m-%Y"))
    
    for i in range(len(lectures)):
        date_mapping[lectures[i]]=i

             
        
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