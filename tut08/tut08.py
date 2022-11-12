
from datetime import datetime
start_time = datetime.now()
import textwrap as tr

#Help



def scorecard():
	
	players={}
	power_play1=0
	power_play2=0
	bat1=[]
	bowl1=[]
	bat2=[]
	bowl2=[]
	total1=[0]*3
	total2=[0]*3
	table1=[]
	table2=[]
	table3=[]
	table4=[]
	extra1=[0]*6
	extra2=[0]*6
	fall_of_wickets1=[]
	fall_of_wickets2=[]
	did_not_bat1=[]
	did_not_bat2=[]

	def find_indexof_bowler_batsman(bowler,batsman,x):
		temp=[]
		if(x==1):
			for i in range(len(bat1)):
				if(bat1[i]==batsman):
					temp.append(i)
					break
			for i in range(len(bowl1)):
				if(bowl1[i]==bowler):
					temp.append(i)
					break
		else:
			for i in range(len(bat2)):
				if(bat2[i]==batsman):
					temp.append(i)
					break
			for i in range(len(bowl2)):
				if(bowl2[i]==bowler):
					temp.append(i)
					break
		return temp
	def no_run(t1,t2,bowler,batsman,m):
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
	def runs(t1,t2,bowler,batsman,y,m):
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		t1[x[0]][1]+=y
		t2[x[1]][2]+=y
		
	def wide(t1,t2,bowler,batsman,m):
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t2[x[1]][5]+=1
		t2[x[1]][2]+=1
	def wides(t1,t2,bowler,batsman,z,m):
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t2[x[1]][5]+=z
		t2[x[1]][2]+=z
		
	def byes(t1,t2,bowler,batsman,z,m):
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		
	def caught_out(t1,t2,bowler,batsman,catcher,m):
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		t1[x[0]][0]='c '+catcher+' b '+bowler
		t2[x[1]][3]+=1
		
	def lbw(t1,t2,bowler,batsman,m):
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		t2[x[1]][3]+=1
		t1[x[0]][0]='lbw b '+bowler
		
	def bowled(t1,t2,bowler,batsman,m):
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		t2[x[1]][3]+=1
		t1[x[0]][0]='b '+bowler
		
	def bowls_to_overs(t):
		for i in t:
			res=str(i[0]//6)
			if(i[0]%6!=0):
				res+='.'+str(i[0]%6)
			i[0]=res
	def eco_calc(t):
		for i in t:
			temp=i[2]*6/i[0]
			i[6]='{0:.1f}'.format(temp)+'0'
	def SR_calc(t):
		for i in t:
			temp=i[1]*100/i[2]
			i[5]='{0:.2f}'.format(temp)
	def total_score_calc(t1,t2,total1):
		for i in t1:
			total1[2]+=i[2]
		res=str(total1[2]//6)
		if(total1[2]%6!=0):
			res+='.'+str(total1[2]%6)
		total1[2]=res


	file1=open('teams.txt','r')
	Lines=file1.readlines()
	pak_team=Lines[0].strip().split(':')[1].split(',')
	for i in range(len(pak_team)):
		pak_team[i]=pak_team[i].strip().split('(')[0]
		x=pak_team[i].split(' ')
		players[x[0]]=pak_team[i]
		players[x[1]]=pak_team[i]
		players[pak_team[i]]=pak_team[i]
		
	ind_team=Lines[2].strip().split(':')[1].split(',')
	for i in range(len(ind_team)):
		ind_team[i]=ind_team[i].strip().split('(')[0]
		x=ind_team[i].split(' ')
		players[x[0]]=ind_team[i]
		players[x[1]]=ind_team[i]
		players[ind_team[i]]=ind_team[i]
	file1.close()

	file1=open('pak_inns1.txt','r')
	Lines=file1.readlines()
	
	
	


	
###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

scorecard()


#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))