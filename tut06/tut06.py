from ctypes import sizeof
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

def attendance_report():
    try:
        df=pd.read_csv('input_registered_students.csv')
    except:
        print('Input file error')

    attendence_count_actual={}
    attendence_count_fake={}
    rolls={}
    roll_numbers=[]
    name={}
    date_mapping={}
    lectures=set()
    
    for i in df.index:
        roll_no=df['Roll No'][i]
        roll_numbers.append(df['Roll No'][i])
        rolls[roll_no]=i
        name[roll_no]=df['Name'][i]
        attendence_count_actual[roll_no]=0
        attendence_count_fake[roll_no]=0
    
    n=len(rolls)
    dates_marked=[[] for _ in range(n)]

    del df
    df1=pd.read_csv('input_attendance.csv')
    df = df1[df1['Attendance'].notnull()]

    for i in df.index:
        try:
            date_and_time=df['Timestamp'][i].split()
            roll_no_and_name=df['Attendance'][i]
            roll_no=roll_no_and_name.split()[0]
            date=date_and_time[0]
            time=date_and_time[1].split(':')[0]
            format="%d/%m/%Y"
            date_obj=datetime.strptime(date,format)

            if(date_obj.weekday()==0 or date_obj.weekday()==3):
                lectures.add(date)
                if(time=='14'):
                    if(date not in dates_marked[rolls[roll_no]] and roll_no in roll_numbers):
                        attendence_count_actual[roll_no]+=1
                        dates_marked[rolls[roll_no]].append(date)
                elif(roll_no in roll_numbers):
                    attendence_count_fake[roll_no]+=1     
        except:
            continue
            
    total_lectures=len(lectures)
    lectures=list(lectures)
    for i in range(total_lectures):
        date_mapping[lectures[i]]=i
    roll_numbers_in_specific_date=[[] for _ in range(total_lectures)]

    for i in df.index:
        try:
            date_and_time=df['Timestamp'][i].split()
            roll_no_and_name=df['Attendance'][i]
            roll_no=roll_no_and_name.split()[0]
            date=date_and_time[0]
            time=date_and_time[1].split(':')[0]
            format="%d/%m/%Y"
            date_obj=datetime.strptime(date,format)

            if(roll_no in roll_numbers):
                roll_numbers_in_specific_date[date_mapping[date]].append(roll_no)     
        except:
            continue

    os.mkdir('output')
    for i in range(221):
        with open('output/%s.csv'%roll_numbers[i],'w',newline='') as f:         
            writer=csv.writer(f)
            header_list=['Roll','Name','total_lecture_taken','attendance_count_actual','attendance_count_fake','attendance_count_absent','Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal ']
            writer.writerow(header_list)
            absent=total_lectures-attendence_count_actual[roll_numbers[i]]-attendence_count_fake[roll_numbers[i]]
            percentage=round(attendence_count_actual[roll_numbers[i]]*100/total_lectures,2)
            writer.writerow([roll_numbers[i],name[roll_numbers[i]],total_lectures,attendence_count_actual[roll_numbers[i]],attendence_count_fake[roll_numbers[i]],absent,percentage])

    with open('output/%s.csv'%'attendance_report_consolidated','w',newline='') as f:         
        writer=csv.writer(f)
        header_list=['Roll','Name','total_lecture_taken','attendance_count_actual','attendance_count_fake','attendance_count_absent','Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal ']
        writer.writerow(header_list)
        for i in range(221):
            absent=total_lectures-attendence_count_actual[roll_numbers[i]]-attendence_count_fake[roll_numbers[i]]
            percentage=round(attendence_count_actual[roll_numbers[i]]*100/total_lectures,2)
            writer.writerow([roll_numbers[i],name[roll_numbers[i]],total_lectures,attendence_count_actual[roll_numbers[i]],attendence_count_fake[roll_numbers[i]],absent,percentage])  
    
    with open('output/%s.csv'%'attendance_report_duplicate','w',newline='') as f:         
        writer=csv.writer(f)
        header_list=['Timestamp','Roll','Name','Total count of attendance on that day']
        writer.writerow(header_list)
        for i in range(total_lectures):
            date_of_duplicate=lectures[i]
            roll_numbers_on_that_day=roll_numbers_in_specific_date[i]
            roll_numbers_on_that_day.sort()
            count_of_roll={}
            for j in range(221):
                count_of_roll[roll_numbers[j]]=0
            for j in range(len(roll_numbers_on_that_day)):
                count_of_roll[roll_numbers_on_that_day[j]]+=1
            for key,value in count_of_roll.items():
                if(value>1):
                    writer.writerow([date_of_duplicate,key,name[key],value])
    
    def send_email():
        try:
            subject = "Consolidated Attendace Report"
            body = "The report is attached with this mail."
            sender_email = input("Enter sender email : ")
            receiver_email = "cs3842022@gmail.com"
            password = input("Type your password and press enter:")

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

    ans=input("Do you want to email to cs3842022@gmail.com (Y/N) : ")
    if(ans=='Y'):
        send_email()

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
