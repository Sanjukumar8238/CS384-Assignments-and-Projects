import csv
import os
import pandas as pd
os.chdir(r"C:\Users\Sanju Phogat\Documents\GitHub\2001EE62_2022\tut01")

df=pd.read_csv('octant_input.csv')
u_avg=df['U'].mean()
v_avg=df['V'].mean()
w_avg=df['W'].mean()
df['U Avg']=u_avg
df['V Avg']=v_avg
df['W Avg']=w_avg

df[r"U'=U-U Avg"]=df['U']-df['U Avg']
df[r"V'=V-V Avg"]=df['V']-df['V Avg']
df[r"W'=W-W Avg"]=df['W']-df['W Avg']

df.to_csv('output.csv')
#def octact_identification(mod=5000):
###Code


#mod=5000
#octact_identification(mod)

