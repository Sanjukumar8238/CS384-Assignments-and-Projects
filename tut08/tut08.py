from datetime import datetime							# Importing required header files
start_time = datetime.now()
import textwrap as tr

#Help

def scorecard():										# Function to generate scorecard
	
	players={}											# Dictionary to map players according to their first and last names
	power_play1=0										# Variable for Power-play runs -> team1
	power_play2=0										# Variable for Power-play runs -> team2
	bat1=[]												# List of batsman in team1
	bowl1=[]											# List of bowler in team1
	bat2=[]												# List of batsman in team2
	bowl2=[]											# List of bowler in team2
	total1=[0]*3										# Storing total values-> Runs, Wickets, Overs - team1
	total2=[0]*3										# Storing total values-> Runs, Wickets, Overs - team2
	table1=[]											# Batting stats of team1
	table2=[]											# Bowling stats of team2
	table3=[]											# Batting stats of team2
	table4=[]											# Bowling stats of team1
	extra1=[0]*6										# Extra runs - [sum of extra runs,b,lb,w,nb,p] - team1
	extra2=[0]*6										# Extra runs - [sum of extra runs,b,lb,w,nb,p] - team2
	fall_of_wickets1=[]									# List for containing fall of wickets - team1
	fall_of_wickets2=[]									# List for containing fall of wickets - team2
	did_not_bat1=[]										# Players that didn't bat in team1
	did_not_bat2=[]										# Players that didn't bat in team1

	def find_indexof_bowler_batsman(bowler,batsman,x):	# Function for finding index of bowler and batsman
		temp=[]											# []=[index of batsman, index of bowler]- for storing in tables
		if(x==1):										# For 1st innings
			for i in range(len(bat1)):
				if(bat1[i]==batsman):
					temp.append(i)
					break
			for i in range(len(bowl1)):
				if(bowl1[i]==bowler):
					temp.append(i)
					break
		else:											# For 2nd innings
			for i in range(len(bat2)):
				if(bat2[i]==batsman):
					temp.append(i)
					break
			for i in range(len(bowl2)):
				if(bowl2[i]==bowler):
					temp.append(i)
					break
		return temp
	def no_run(t1,t2,bowler,batsman,m):					# If no runs is scored in single ball
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
	def runs(t1,t2,bowler,batsman,y,m):					# If y runs is scored in single ball
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		t1[x[0]][1]+=y
		t2[x[1]][2]+=y
		
	def wide(t1,t2,bowler,batsman,m):					# If ball is wide
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t2[x[1]][5]+=1
		t2[x[1]][2]+=1
	def wides(t1,t2,bowler,batsman,z,m):				# If z balls are wide
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t2[x[1]][5]+=z
		t2[x[1]][2]+=z
		
	def byes(t1,t2,bowler,batsman,z,m):					# If 1 run is scored in byes
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		
	def caught_out(t1,t2,bowler,batsman,catcher,m):		# If batsman is caught out
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		t1[x[0]][0]='c '+catcher+' b '+bowler
		t2[x[1]][3]+=1
		
	def lbw(t1,t2,bowler,batsman,m):					# If batsman is out by lbw
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		t2[x[1]][3]+=1
		t1[x[0]][0]='lbw b '+bowler
		
	def bowled(t1,t2,bowler,batsman,m):					# If batsman is bowled
		x=find_indexof_bowler_batsman(bowler,batsman,m)
		t1[x[0]][2]+=1
		t2[x[1]][0]+=1
		t2[x[1]][3]+=1
		t1[x[0]][0]='b '+bowler
		
	def bowls_to_overs(t):								# Function to converting balls to overs
		for i in t:
			res=str(i[0]//6)
			if(i[0]%6!=0):
				res+='.'+str(i[0]%6)
			i[0]=res
	def eco_calc(t):									# Calculating economy of a bowler
		for i in t:
			temp=i[2]*6/i[0]
			i[6]='{0:.1f}'.format(temp)+'0'
	def SR_calc(t):										# Calculating strike rate of a batsman
		for i in t:
			temp=i[1]*100/i[2]
			i[5]='{0:.2f}'.format(temp)
	def total_score_calc(t1,t2,total1):					# Converting balls in total variable to overs
		for i in t1:
			total1[2]+=i[2]
		res=str(total1[2]//6)
		if(total1[2]%6!=0):
			res+='.'+str(total1[2]%6)
		total1[2]=res

	try:
		file1=open('teams.txt','r')							# Opening teams.txt file 
	except:
		print('Error in opening teams.txt file')
	Lines=file1.readlines()								

	pak_team=Lines[0].strip().split(':')[1].split(',')	# Storing names of team1 players and mapping according to their first and last names
	for i in range(len(pak_team)):
		pak_team[i]=pak_team[i].strip().split('(')[0]
		x=pak_team[i].split(' ')
		players[x[0]]=pak_team[i]
		players[x[1]]=pak_team[i]
		players[pak_team[i]]=pak_team[i]
		
	ind_team=Lines[2].strip().split(':')[1].split(',')	# Storing names of team2 players and mapping according to their first and last names
	for i in range(len(ind_team)):
		ind_team[i]=ind_team[i].strip().split('(')[0]
		x=ind_team[i].split(' ')
		players[x[0]]=ind_team[i]
		players[x[1]]=ind_team[i]
		players[ind_team[i]]=ind_team[i]
	file1.close()

	try:
		file1=open('pak_inns1.txt','r')						# Pakistan's innings file is opened
	except:
		print('Error in opening pak_inns1.txt')
	Lines=file1.readlines()
	for line in Lines:
		if(line=='\n'):
			continue
		line=line.strip().split(',')
		x=line[0].strip().split(' ')
		y=line[1].strip()
		
		if(x[2]=='to'):									# Figuring out bowler and batsman
			batsman=players[x[3]]
			bowler=players[x[1]]
		elif(x[3]=='to'):
			batsman=players[x[4]]
			bowler=players[x[1]]

		if(batsman not in bat1):						# If batsman or bowler is not in the bat1 or bowl1, then add a new row to table1 or table2 respectively
			bat1.append(batsman)
			temp=['not out',0,0,0,0,0]
			table1.append(temp)
		if(bowler not in bowl1):
			bowl1.append(bowler)
			temp=[0,0,0,0,0,0,0]
			table2.append(temp)

		# Functions are called according to the event happened in each ball
		if(y=='no run'):								
			no_run(table1,table2,bowler,batsman,1)
		elif(y=='byes'):
			z=int(line[2].strip().split(' ')[0])
			byes(table1,table2,bowler,batsman,z,1)
			extra1[1]+=z
			extra1[0]+=z
			total1[0]+=z
		elif(y=='1 run'):
			runs(table1,table2,bowler,batsman,1,1)
			total1[0]+=1
		elif(y=='FOUR'):
			x=find_indexof_bowler_batsman(bowler,batsman,1)
			table1[x[0]][3]+=1
			runs(table1,table2,bowler,batsman,4,1)
			total1[0]+=4
		elif(y=='wide'):
			wide(table1,table2,bowler,batsman,1)
			extra1[3]+=1
			extra1[0]+=1
			total1[0]+=1
		elif(y=='SIX'):
			x=find_indexof_bowler_batsman(bowler,batsman,1)
			table1[x[0]][4]+=1
			runs(table1,table2,bowler,batsman,6,1)
			total1[0]+=6
		elif(y.split(' ')[1]=='runs'):
			runs(table1,table2,bowler,batsman,int(y.split(' ')[0]),1)
			total1[0]+=int(y.split(' ')[0])
		elif(y.split(' ')[0]=='out' and y.split(' ')[1]=='Caught'):
			z=''
			flag=0
			for i in y:
				if(i=='y' and flag==0):
					flag=1
				elif(flag==1 and i==' '):
					flag=2
					continue
				elif(flag==2 and i!='!'):
					z+=i
				elif(i=='!'):
					break
			caught_out(table1,table2,bowler,batsman,players[z],1)
			total1[1]+=1
		elif(y.split(' ')[0]=='out' and y.split(' ')[1]=='Lbw!!'):
			lbw(table1,table2,bowler,batsman,1)
			total1[1]+=1
		elif(y.split(' ')[0]=='out' and y.split(' ')[1]=='Bowled!!'):
			bowled(table1,table2,bowler,batsman,1)
			total1[1]+=1

		if(y.split(' ')[0]=='out'):							# Storing fall of wickets
			fall_of_wickets1.append(str(total1[0])+'-'+str(total1[1])+' ('+batsman+', '+x[0]+')')
		if(x[0]=='5.6'):									# Powerplay over
			power_play1=total1[0]
	for i in pak_team:										# Players that did not bat
		if(i not in bat1):
			did_not_bat1.append(i)

	eco_calc(table2)										# Remaining functions are called
	bowls_to_overs(table2)
	SR_calc(table1)
	total_score_calc(table1,table2,total1=total1)
	
	
	file1.close()
	try:
		file1=open('india_inns2.txt','r')						# India's innings file is opened
	except:
		print('Error in opening india_inns2.txt')
	Lines=file1.readlines()
	for line in Lines:
		if(line=='\n'):
			continue
		line=line.strip().split(',')
		x=line[0].strip().split(' ')
		y=line[1].strip()
		
		if(x[2]=='to'):										# Figuring out bowler and batsman
			batsman=players[x[3]]
			bowler=players[x[1]]
		elif(x[3]=='to'):
			batsman=players[x[4]]
			bowler=players[x[1]]
	
		if(batsman not in bat2):							# If batsman or bowler is not in the bat1 or bowl1, then add a new row to table3 or table4 respectively
			bat2.append(batsman)
			temp=['not out',0,0,0,0,0]
			table3.append(temp)
		if(bowler not in bowl2):
			bowl2.append(bowler)
			temp=[0,0,0,0,0,0,0]
			table4.append(temp)

		# Functions are called according to the event happened in each ball
		if(y=='no run'):
			no_run(table3,table4,bowler,batsman,2)
		elif(y=='byes'):
			z=int(line[2].strip().split(' ')[0])
			byes(table3,table4,bowler,batsman,z,2)
			extra2[1]+=z
			extra2[0]+=z
			total2[0]+=z
		elif(y=='leg byes'):
			z=line[2].strip()
			x=0
			if(z=='FOUR'):
				x=4
			elif(z=='1 run'):
				x=1
			extra2[0]+=x
			total2[0]+=x
			extra2[2]+=x
			byes(table3,table4,bowler,batsman,x,2)
		elif(y=='1 run'):
			runs(table3,table4,bowler,batsman,1,2)
			total2[0]+=1
		elif(y=='FOUR'):
			x=find_indexof_bowler_batsman(bowler,batsman,2)
			table3[x[0]][3]+=1
			runs(table3,table4,bowler,batsman,4,2)
			total2[0]+=4
		elif(y=='wide'):
			wide(table3,table4,bowler,batsman,2)
			extra2[3]+=1
			extra2[0]+=1
			total2[0]+=1
		elif(y=='SIX'):
			x=find_indexof_bowler_batsman(bowler,batsman,2)
			table3[x[0]][4]+=1
			runs(table3,table4,bowler,batsman,6,2)
			total2[0]+=6
		elif(y.split(' ')[1]=='runs'):
			runs(table3,table4,bowler,batsman,int(y.split(' ')[0]),2)
			total2[0]+=int(y.split(' ')[0])
		elif(y.split(' ')[0]=='out' and y.split(' ')[1]=='Caught'):
			z=''
			flag=0
			for i in y:
				if(i=='y' and flag==0):
					flag=1
				elif(flag==1 and i==' '):
					flag=2
					continue
				elif(flag==2 and i!='!'):
					z+=i
				elif(i=='!'):
					break
			caught_out(table3,table4,bowler,batsman,players[z],2)
			total2[1]+=1
		elif(y.split(' ')[1]=='wides'):
			z=int(y.split(' ')[0])
			extra2[3]+=z
			extra2[0]+=z
			total2[0]+=z
			wides(table3,table4,bowler,batsman,z,2)
		elif(y.split(' ')[0]=='out' and y.split(' ')[1]=='Lbw!!'):
			lbw(table3,table4,bowler,batsman,2)
			total2[1]+=1
		elif(y.split(' ')[0]=='out' and y.split(' ')[1]=='Bowled!!'):
			bowled(table3,table4,bowler,batsman,2)
			total2[1]+=1
		else:
			print(line)

		if(y.split(' ')[0]=='out'):							# Storing fall of wickets
			fall_of_wickets2.append(str(total2[0])+'-'+str(total2[1])+' ('+batsman+', '+x[0]+')')
		if(line[0].strip().split(' ')[0]=='5.6'):			# Powerplay over
			power_play2=total2[0]
	for i in ind_team:										# Players that did not bat
		if(i not in bat2):
			did_not_bat2.append(i)
	
	eco_calc(table4)										# Remaining functions are called
	bowls_to_overs(table4)
	SR_calc(table3)
	total_score_calc(table3,table4,total1=total2)
	

	file1.close()
	try:
		file=open('Scorecard.txt','w')							# Opening Scorecard file for writing to it
	except:
		print('Error in opening Scorecard.txt file')
	# Pakistan's Scorecard written

	file.write("{: >0} {: >89}".format(*['Pakistan Innings',str(total1[0])+'-'+str(total1[1])+' ('+total1[2]+' Ov)\n']))
	file.write('\n')
	file.write("{: <20} {: ^45}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}".format(*['Batter','','R','B','4s','6s','SR\n']))
	for i in range(len(bat1)):
		file.write("{: <20} {: ^45}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}".format(*[bat1[i],table1[i][0],table1[i][1],table1[i][2],table1[i][3],table1[i][4],str(table1[i][5])+'\n']))
	file.write("{: <20} {: <48}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}".format(*['Extras','',str(extra1[0])+' (b '+str(extra1[1])+', lb '+str(extra1[2])+', w '+str(extra1[3])+', nb '+str(extra1[4])+', p '+str(extra1[5])+')','','','','\n']))
	file.write("{: <20} {: >71}".format(*['Total',str(total1[0])+' ('+str(total1[1])+' wkts, '+str(total1[2])+' Ov)\n']))
	file.write('\n')
	file.write("{: <20} {: >8}".format(*['Fall of Wickets','\n']))
	temp=''
	for i in range(len(fall_of_wickets1)):
		temp+=fall_of_wickets1[i]
		if(i!=len(fall_of_wickets1)-1):
			temp+=', '
	lines=tr.wrap(temp, width=106)
	for i in lines:
		file.write(i+'\n')
	file.write('\n')
	file.write("{: <49} {: ^8}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}{: >8}".format(*['Bowler','O','M','R','W','NB','WD','ECO\n']))
	for i in range(len(bowl1)):
		file.write("{: <49} {: ^8}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}{: >8}".format(*[bowl1[i],table2[i][0],table2[i][1],table2[i][2],table2[i][3],table2[i][4],table2[i][5],str(table2[i][6])+'\n']))
	file.write('\n')
	file.write("{: <35} {: ^35}{: >35}".format(*['Powerplays','Overs','Runs\n']))
	file.write("{: <35} {: ^35}{: >35}".format(*['Mandatory','0.1-6',str(power_play1)+'\n']))
	file.write('\n')
	file.write('\n')
	file.write('\n')


	# India's Scorecard written

	file.write("{: >0} {: >92}".format(*['India Innings',str(total2[0])+'-'+str(total2[1])+' ('+total2[2]+' Ov)\n']))
	file.write('\n')
	file.write("{: <20} {: ^45}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}".format(*['Batter','','R','B','4s','6s','SR\n']))
	for i in range(len(bat2)):
		file.write("{: <20} {: ^45}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}".format(*[bat2[i],table3[i][0],table3[i][1],table3[i][2],table3[i][3],table3[i][4],str(table3[i][5])+'\n']))
	file.write("{: <20} {: <48}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}".format(*['Extras','',str(extra2[0])+' (b '+str(extra2[1])+', lb '+str(extra2[2])+', w '+str(extra2[3])+', nb '+str(extra2[4])+', p '+str(extra2[5])+')','','','','\n']))
	file.write("{: <20} {: >71}".format(*['Total',str(total2[0])+' ('+str(total2[1])+' wkts, '+str(total2[2])+' Ov)\n']))
	temp=''
	for i in range(len(did_not_bat2)):
		temp+=did_not_bat2[i]
		if(i!=len(did_not_bat2)-1):
			temp+=', '
	file.write("{: <20} {: >71}".format(*['Did not bat',temp+'\n']))
	
	file.write('\n')
	file.write("{: <20} {: >8}".format(*['Fall of Wickets','\n']))
	temp=''
	for i in range(len(fall_of_wickets2)):
		temp+=fall_of_wickets2[i]
		if(i!=len(fall_of_wickets2)-1):
			temp+=', '
	lines=tr.wrap(temp, width=106)
	for i in lines:
		file.write(i+'\n')
	file.write('\n')
	file.write("{: <49} {: ^8}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}{: >8}".format(*['Bowler','O','M','R','W','NB','WD','ECO\n']))
	for i in range(len(bowl2)):
		file.write("{: <49} {: ^8}{: ^8}{: ^8}{: ^8}{: ^8}{: >8}{: >8}".format(*[bowl2[i],table4[i][0],table4[i][1],table4[i][2],table4[i][3],table4[i][4],table4[i][5],str(table4[i][6])+'\n']))
	file.write('\n')
	file.write("{: <35} {: ^35}{: >35}".format(*['Powerplays','Overs','Runs\n']))
	file.write("{: <35} {: ^35}{: >35}".format(*['Mandatory','0.1-6',str(power_play2)+'\n']))
	
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