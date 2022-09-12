import csv
import pandas as pd

def find_octant(a,b,c):             # Function to find the octant 
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


df=pd.read_csv('octant_input.csv')  # Reading the input file

u_avg=df['U'].mean()                # Finding average of u,v and w                 
v_avg=df['V'].mean()
w_avg=df['W'].mean()

df['U Avg']=u_avg                   # Creating a column of average of u,v and w
df['V Avg']=v_avg
df['W Avg']=w_avg

df[r"U'=U - U Avg"]=df['U']-df['U Avg']         # Subtracting mean u,v and w from original values and creating a column of it
df[r"V'=V - V Avg"]=df['V']-df['V Avg']
df[r"W'=W - W Avg"]=df['W']-df['W Avg']

octant=[]                           # List to store octants 

for i in df.index:                  # Finding octant of each row and appending in octant[]
    octant.append(find_octant(df[r"U'=U - U Avg"][i],df[r"V'=V - V Avg"][i],df[r"W'=W - W Avg"][i]))

df['Octant']=octant                 # Creating a column for storing corresponding octants
count=[0]*8                         # List for storing count of different octants

for i in octant:                    # Finding total count of values in different octants
    if(i==1):
        count[0]=count[0]+1
    elif(i==-1):
        count[1]=count[1]+1
    elif(i==2):
        count[2]=count[2]+1
    elif(i==-2):
        count[3]=count[3]+1
    elif(i==3):
        count[4]=count[4]+1
    elif(i==-3):
        count[5]=count[5]+1
    elif(i==4):
        count[6]=count[6]+1
    elif(i==-4):
        count[7]=count[7]+1

print('Octant ID\t1\t-1\t2\t-2\t3\t-3\t4\t-4')      # Printing the overall count of diiferent octants 
print('Overall Count\t',end="")
for i in count:
    print(i,'\t',end="")
print("")

x=int(input("Enter mod value : "))                  # Taking input of mod from user
n=len(octant)

count=[0]*8
k=0 
for i in octant:                                    # Counting number of values in different octants in mod range
    if(i==1):
        count[0]=count[0]+1
    elif(i==-1):
        count[1]=count[1]+1
    elif(i==2):
        count[2]=count[2]+1
    elif(i==-2):
        count[3]=count[3]+1
    elif(i==3):
        count[4]=count[4]+1
    elif(i==-3):
        count[5]=count[5]+1
    elif(i==4):
        count[6]=count[6]+1
    elif(i==-4):
        count[7]=count[7]+1
    k=k+1
    if(k%x==1):                                     # Printing the count of values in different octants
        print(k,'-',end="")
    elif(k%x==0 or k==n):
        print(k,'\t',end="")
        for j in count:
            print(j,'\t',end="")
        print("")
        count=[0]*8                                 # Resetting count of values in different octants


