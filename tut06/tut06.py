from ctypes import sizeof                                           # Importing libraries
import pandas as pd
import csv
import os
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime
start_time = datetime.now()

def attendance_report():                                            # Function to process input files
    try:
        df=pd.read_csv('input_registered_students.csv')             # Reading input_registered_students file
    except:
        print('Input file error')

    attendence_count_actual={}                                      # Dictionary to map actual count of attendance for each roll no.
    attendence_count_fake={}                                        # Dictionary to map fake count of attendance for each roll no.
    rolls={}                                                        # Mapping each roll no. with an integer
    roll_numbers=[]                                                 # List containing all registered roll numbers
    name={}                                                         # Dictionary for mapping roll numbers to names of students
    date_mapping={}                                                 # Dictionary for mapping each lecture falling on Monday and Thursday to an integer
    lectures=set()                                                  # Set containing dates of all lectures falling on Monday and Thursday
    
    for i in df.index:                                              # Iterating through the dataframe row-wise
        roll_no=df['Roll No'][i]                                    # Roll no. of student  
        roll_numbers.append(df['Roll No'][i])                       # Appending roll no. of student in the list 'roll_numbers'
        rolls[roll_no]=i                                            # Mapping roll numbers to integers
        name[roll_no]=df['Name'][i]                                 # Mapping roll numbers to names of students
        attendence_count_actual[roll_no]=0                          # Initializing actual attendance count of each student as zero
        attendence_count_fake[roll_no]=0                            # Initializing fake attendance count of each student as zero
    
    n=len(rolls)                                                    # Finding number of roll numbers
    dates_marked=[[] for _ in range(n)]                             # List of list for storing the dates marked by the each student

    del df
    df1=pd.read_csv('input_attendance.csv')                         # Reading input_attendace file 
    df = df1[df1['Attendance'].notnull()]                           # Removing the rows which have name as empty

    for i in df.index:                                              # Iterating through the dataframe of input_attendace file
        try:                                                
            date_and_time=df['Timestamp'][i].split()                # Storing date and time from the column 'Timestamp'
            roll_no_and_name=df['Attendance'][i]                    # Storing roll number and name from the column 'Attendance'
            roll_no=roll_no_and_name.split()[0]                     # Finding roll number by splitting the variable roll_no_and_name
            date=date_and_time[0]                                   # Finding date from date_and_time variable
            time=date_and_time[1].split(':')[0]                     # Finding hour of time from date and time variable by splitting
            format="%d/%m/%Y"                                       # Formatting the date
            date_obj=datetime.strptime(date,format)                 # Converting date string to date object supported by python

            if(date_obj.weekday()==0 or date_obj.weekday()==3):     # Checking if the date is on Monday or Thursday
                lectures.add(date)                                  # Adding the date to lectures if date is on Monday and Thursday
                if(time=='14' or date_and_time[1]=='15:00:00'):                                     # If time is from 2pm to 3pm proceed:
                    if(date not in dates_marked[rolls[roll_no]] and roll_no in roll_numbers):       # Checking if roll numbers are of registered students and if that date is already marked by the student
                        attendence_count_actual[roll_no]+=1                                         # Incrementing actual attendance count by 1
                        dates_marked[rolls[roll_no]].append(date)                                   # Appending the date corresponding to the roll number
                elif(roll_no in roll_numbers):                                          
                    attendence_count_fake[roll_no]+=1               # Incrementing fake attendance count by 1
            else:
                attendence_count_fake[roll_no]+=1                   # Incrementing fake attendance count by 1
        except:
            continue                                                # If any error occurs move to next row
            
    total_lectures=len(lectures)                                    # Counting total number of lectures
    lectures=list(lectures)                                         # Converting set to list
    for i in range(total_lectures):                                 # Mapping each leture to integer
        date_mapping[lectures[i]]=i
    roll_numbers_in_specific_date=[[] for _ in range(total_lectures)]   # Storing roll numbers in a particular day

    for i in df.index:
        try:
            date_and_time=df['Timestamp'][i].split()                # Storing date and time from the column 'Timestamp'
            roll_no_and_name=df['Attendance'][i]                    # Storing roll number and name from the column 'Attendance'
            roll_no=roll_no_and_name.split()[0]                     # Finding roll number by splitting the variable roll_no_and_name
            date=date_and_time[0]                                   # Finding date from date_and_time variable
            time=date_and_time[1].split(':')[0]                     # Finding hour of time from date and time variable by splitting
            format="%d/%m/%Y"                                       # Formatting the date
            date_obj=datetime.strptime(date,format)                 # Converting date string to date object supported by python

            if(date_obj.weekday()==0 or date_obj.weekday()==3):     # Checking if the date is on Monday or Thursday
                if(time=='14' or date_and_time[1]=='15:00:00'):                                     # If time is from 2pm to 3pm proceed:
                    if(roll_no in roll_numbers):       # Checking if roll numbers are of registered students and if that date is already marked by the student
                        roll_numbers_in_specific_date[date_mapping[date]].append(roll_no)       # Appending the roll number in the specific date     
        except:
            continue

    os.mkdir('output')                                              # Creating output directory

    for i in range(221):                                            # For creating individual ROLL_NO.csv file
        with open('output/%s.csv'%roll_numbers[i],'w',newline='') as f:         
            writer=csv.writer(f)
            header_list=['Roll','Name','total_lecture_taken','attendance_count_actual','attendance_count_fake','attendance_count_absent','Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal ']
            writer.writerow(header_list)                                                                                # Writing the header row
            absent=total_lectures-attendence_count_actual[roll_numbers[i]]                                              # Counting absent days
            percentage=round(attendence_count_actual[roll_numbers[i]]*100/total_lectures,2)                             # Counting percentage attendance
            writer.writerow([roll_numbers[i],name[roll_numbers[i]],total_lectures,attendence_count_actual[roll_numbers[i]],attendence_count_fake[roll_numbers[i]],absent,percentage])           # Writing the row

    with open('output/%s.csv'%'attendance_report_consolidated','w',newline='') as f:            # For creating consolidated attendance report    
        writer=csv.writer(f)
        header_list=['Roll','Name','total_lecture_taken','attendance_count_actual','attendance_count_fake','attendance_count_absent','Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal ']
        writer.writerow(header_list)                                                                                    # Writing the header row
        for i in range(221):
            absent=total_lectures-attendence_count_actual[roll_numbers[i]]                                              # Counting absent days
            percentage=round(attendence_count_actual[roll_numbers[i]]*100/total_lectures,2)                             # Counting percentage attendace
            writer.writerow([roll_numbers[i],name[roll_numbers[i]],total_lectures,attendence_count_actual[roll_numbers[i]],attendence_count_fake[roll_numbers[i]],absent,percentage])           # Writing the row
    
    with open('output/%s.csv'%'attendance_report_duplicate','w',newline='') as f:               # For attendance_report_duplicate.csv
        writer=csv.writer(f)
        header_list=['Timestamp','Roll','Name','Total count of attendance on that day']         
        writer.writerow(header_list)                                                            # Writing the header row
        for i in range(total_lectures):
            date_of_duplicate=lectures[i]
            roll_numbers_on_that_day=roll_numbers_in_specific_date[i]
            roll_numbers_on_that_day.sort() 
            count_of_roll={}
            for j in range(221):                                                                # Initializing the count of roll no. on particular lecture
                count_of_roll[roll_numbers[j]]=0
            for j in range(len(roll_numbers_on_that_day)):
                count_of_roll[roll_numbers_on_that_day[j]]+=1                                   # Incrementing the count of roll no.
            for key,value in count_of_roll.items():
                if(value>1):                                                                    # If attendance is more than 1 on particular day write it in the file
                    writer.writerow([date_of_duplicate,key,name[key],value])                    # Writing the duplicate information  
    
    def send_email():                                                                           # Function to send email to cs3842022@gmail.com
        try:
            subject = "Consolidated Attendace Report"                                           
            body = "The report is attached with this mail."
            sender_email = input("Enter sender email : ")                                       # Sender e-mail
            receiver_email = "cs3842022@gmail.com"                                        # Receiver e-mail => cs3842022@gmail.com
            password = input("Type your password and press enter:")                             # Password of sender e-mail

            # Create a multipart message and set headers
            message = MIMEMultipart()                                                       
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            filename = "output/attendance_report_consolidated.csv"  # In same directory as script

            # Open csv file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

            # Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
        except:
            print("Error in sending the file.")

    ans=input("Do you want to email to cs3842022@gmail.com (Y/N) : ")                                   # Asking if you want to email the file
    if(ans=='Y'):
        send_email()                                                                                    # If ans='Y' call send_email() function

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
