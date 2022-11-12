
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