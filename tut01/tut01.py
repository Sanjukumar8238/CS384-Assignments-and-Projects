import csv                                          
import pandas as pd
import os

mod=5000                                              # User input - Mod value

def find_octant(a,b,c):                             # Function to find the octant 
    if(a>0 and b>0 and c>0):    
        return 1
    elif(a>0 and b>0 and c<0):
        return -1
    elif(a<0 and b>0 and c>0):
        return 2
    elif(a<0 and b>0 and c<0):
        return -2
    elif(a<0 and b<0 and c>0):
        return 3
    elif(a<0 and b<0 and c<0):
        return -3
    elif(a>0 and b<0 and c>0):
        return 4
    elif(a>0 and b<0 and c<0):
        return -4


df=pd.read_csv('octant_input.csv')                  # Reading the input file

u_avg=df['U'].mean()                                # Finding average of u,v and w                 
v_avg=df['V'].mean()
w_avg=df['W'].mean()

with open('temp.csv','w',newline='') as f:          # Writing columns of average of u,v and w in a temp file
    writer=csv.writer(f)
    header_list=['U Avg','V Avg','W Avg']
    writer.writerow(header_list)
    writer.writerow([u_avg,v_avg,w_avg])

x=pd.read_csv('temp.csv')                           # Creating a dataframe 'x'

df['U Avg']=x['U Avg']                              # Creating a column of average of u,v and w in dataframe 'df' from dataframe 'x' so that the average columns of u,v and w are of one row
df['V Avg']=x['V Avg']
df['W Avg']=x['W Avg']

os.remove('temp.csv')                               # Deleting the temporary file

df[r"U'=U - U Avg"]=df['U']-u_avg                   # Subtracting mean of u,v and w from original values and creating a column of it
df[r"V'=V - V Avg"]=df['V']-v_avg
df[r"W'=W - W Avg"]=df['W']-w_avg

octant=[]                                           # List to store octants

for i in df.index:                                  # Finding octant and storing them in a list named 'Octant'
    octant.append(find_octant(df[r"U'=U - U Avg"][i],df[r"V'=V - V Avg"][i],df[r"W'=W - W Avg"][i]))

df['Octant']=octant                                 # Creating a column for storing corresponding octants in dataframe

matrix=[]                                           # 2-d matrix for storing octants within ranges
count=[0]*9                                         # Creating a list for storing elements of 9 columns

count[0]='Octant ID'                                # Storing header list in 'count' list
for i in range(0,4):
    count[2*i+1]=(i+1)
    count[2*(i+1)]=-(i+1)
matrix.append(count)                                # Appending header list in matrix

count=[0]*9                                         # Resetting values in list 'count'

for i in octant:                                    # Finding total count of values in different octants
    if(i==1):
        count[1]=count[1]+1
    elif(i==-1):
        count[2]=count[2]+1
    elif(i==2):
        count[3]=count[3]+1
    elif(i==-2):
        count[4]=count[4]+1
    elif(i==3):
        count[5]=count[5]+1
    elif(i==-3):
        count[6]=count[6]+1
    elif(i==4):
        count[7]=count[7]+1
    elif(i==-4):
        count[8]=count[8]+1

count[0]='Overall Count'                            
matrix.append(count)                                # Appending total count of values in different octants to the 2-d matrix

matrix.append(['User input','Mod '+str(mod)])         # Appending this value in the matrix

n=len(octant)                                       # Finding the number of points given in the input
count=[0]*9                                         # Resetting the values in the list 'count'
k=0                                                 # Variable to keep track of the index of data we are on
for i in octant:                                    # Counting number of values in different octants in mod range
    if(i==1):
        count[1]=count[1]+1
    elif(i==-1):
        count[2]=count[2]+1
    elif(i==2):
        count[3]=count[3]+1
    elif(i==-2):
        count[4]=count[4]+1
    elif(i==3):
        count[5]=count[5]+1
    elif(i==-3):
        count[6]=count[6]+1
    elif(i==4):
        count[7]=count[7]+1
    elif(i==-4):
        count[8]=count[8]+1
    k=k+1                                           # Incrementing the index tracking variable
    if(k%mod==1):                                     # Processing the mod values in the range and storing them in the list 'count'
        count[0]=str(k-1)+'-'                       
    elif(k%mod==0 or k==n):
        count[0]=count[0]+str(k-1)                  # Here count[0]-> represents the range and further elements of count represents the count in different octants
        matrix.append(count)                        # Appending the list in the matrix
        count=[0]*9                                 # Resetting count of values in different octants

with open('temp.csv', 'w', newline='') as file:     # Creating a temp file for storing the matrix which will be used to append values in the output file
    writer=csv.writer(file)
    writer.writerows(matrix)

x=pd.read_csv('temp.csv')                          # Reading the temp file and storing in new dataframe x
df['Octant ID']=x['Octant ID']                     # Adding the each column of 2-d matrix to the original dataframe
df['1']=x['1']
df['-1']=x['-1']
df['2']=x['2']
df['-2']=x['-2']
df['3']=x['3']
df['-3']=x['-3']
df['4']=x['4']
df['-4']=x['-4']

os.remove('temp.csv')                               # Deleting the temp file 

df.to_csv('octant_output.csv',index=False)          # Saving the output file

