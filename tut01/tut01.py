import csv
import pandas as pd

def find_octant(a,b,c):
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


df=pd.read_csv('octant_input.csv')
u_avg=df['U'].mean()
v_avg=df['V'].mean()
w_avg=df['W'].mean()
df['U Avg']=u_avg
df['V Avg']=v_avg
df['W Avg']=w_avg

df[r"U'=U - U Avg"]=df['U']-df['U Avg']
df[r"V'=V - V Avg"]=df['V']-df['V Avg']
df[r"W'=W - W Avg"]=df['W']-df['W Avg']
octant=[]
for i in df.index:
    octant.append(find_octant(df[r"U'=U - U Avg"][i],df[r"V'=V - V Avg"][i],df[r"W'=W - W Avg"][i]))
df['Octant']=octant
count=[0]*8
for i in octant:
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

print('Octant ID\t1\t-1\t2\t-2\t3\t-3\t4\t-4')
print('Overall Count\t',end="")
for i in count:
    print(i,'\t',end="")
print("")
5
x=int(input("Enter mod value : "))
n=len(octant)

count=[0]*8
k=0
for i in octant:
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
    if(k%x==1):
        print(k,'-',end="")
    elif(k%x==0 or k==n):
        print(k,'\t',end="")
        for j in count:
            print(j,'\t',end="")
        print("")
        count=[0]*8


