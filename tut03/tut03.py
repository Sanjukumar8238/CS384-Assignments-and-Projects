from distutils.log import error
from re import L
import pandas as pd
import os
import openpyxl
from openpyxl import workbook,load_workbook
from openpyxl.styles.borders import Border, Side

mod=5000                                                        # User input - Mod value

def find_octant(a,b,c):                                         # Function to find the octant 
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

df=pd.read_excel('input_octant_longest_subsequence.xlsx')       # Reading input file and storing in dataframe 'df'


n=len(df['U'])                                                  # Finding number of values

u_avg=df['U'].mean()                                            # Finding average of u,v and w                 
v_avg=df['V'].mean()
w_avg=df['W'].mean()

l1=[u_avg]                                                      # Storing values of average of u,v, and w in lists
l2=[v_avg]
l3=[w_avg]
for i in range(1,n):                                            # Appending empty string in all th remaining positions of list
    l1.append(" ")
    l2.append(" ")
    l3.append(" ")
df['U Avg']=l1                                                  # Adding the lists as column in dataframe
df['V Avg']=l2
df['W Avg']=l3

df[r"U'=U - U Avg"]=df['U']-u_avg                               # Subtracting mean of u,v and w from original values and creating a column of it
df[r"V'=V - V Avg"]=df['V']-v_avg
df[r"W'=W - W Avg"]=df['W']-w_avg

octant=[]                                                       # List to store octants

for i in df.index:                                              # Finding octant and storing them in a list named 'Octant'
    octant.append(find_octant(df[r"U'=U - U Avg"][i],df[r"V'=V - V Avg"][i],df[r"W'=W - W Avg"][i]))

df['Octant']=octant                                             # Creating a column for storing corresponding octants in dataframe
df.to_excel('output_octant_transition_identify.xlsx',index=False)                          # Saving the dataframe in file

wb=load_workbook('output_octant_transition_identify.xlsx')                                 # Loading the file in workbook
ws=wb.active


        

wb.save('output_octant_longest_subsequence.xlsx')                                          # Saving the file