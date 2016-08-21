import random
from copy import deepcopy

class InterNode(object):
    def __init__(self,nextlayer,length, complexity):
        self.val = 0
        self.links=temparray=[0]*len(nextlayer)
        self.isOutputNode=0
        counter=0
        if nextlayer != None:	
        	while(counter<length):
        		if(random.randint(0,100)<=complexity):	
        			self.links[counter]=nextlayer[random.randint(0,length-1)]
        		else:
        			self.links[counter]=None
        		counter=counter+1

board =[1,1,1],[1,1,1],[1,1,1]
winner= 0
def printb(b):
	print(b[0][0], end="")
	print(' | ', end="")
	print(b[0][1], end="")
	print(' | ', end="")
	print(b[0][2])
	print('---------')
	print(b[1][0], end="")
	print(' | ', end="")
	print(b[1][1], end="")
	print(' | ', end="")
	print(b[1][2])
	print('---------')
	print(b[2][0], end="")
	print(' | ', end="")
	print(b[2][1], end="")
	print(' | ', end="")
	print(b[2][2])

def checkb(b):
	winner=0
	if(b[0][0]==1 and b[0][1]==1 and b[0][2]==1):
		winner = 1
		return winner
	if(b[1][0]==1 and b[1][1]==1 and b[1][2]==1):
		winner = 1
		return winner
	if(b[2][0]==1 and b[2][1]==1 and b[2][2]==1):
		winner = 1
		return winner
	if(b[0][0]==1 and b[1][0]==1 and b[2][0]==1):
		winner = 1
		return winner	
	if(b[0][1]==1 and b[1][1]==1 and b[2][1]==1):
		winner = 1
		return winner
	if(b[0][2]==1 and b[1][2]==1 and b[2][2]==1):
		winner = 1
		return winner
	if(b[0][0]==1 and b[1][1]==1 and b[2][2]==1):
		winner = 1
		return winner	
	if(b[0][2]==1 and b[1][1]==1 and b[2][0]==1):
		winner = 1
		return winner
	if(b[0][0]==-1 and b[0][1]==-1 and b[0][2]==-1):
		winner = -1
		return winner
	if(b[1][0]==-1 and b[1][1]==-1 and b[1][2]==-1):
		winner = -1
		return winner
	if(b[2][0]==-1 and b[2][1]==-1 and b[2][2]==-1):
		winner = -1
		return winner
	if(b[0][0]==-1 and b[1][0]==-1 and b[2][0]==-1):
		winner = -1
		return winner	
	if(b[0][1]==-1 and b[1][1]==-1 and b[2][1]==-1):
		winner = -1
		return winner
	if(b[0][2]==-1 and b[1][2]==-1 and b[2][2]==-1):
		winner = -1
		return winner
	if(b[0][0]==-1 and b[1][1]==-1 and b[2][2]==-1):
		winner = -1
		return winner	
	if(b[0][2]==-1 and b[1][1]==-1 and b[2][0]==-1):
		winner = -1
		return winner
	return winner

def pvp():
	b=[0,0,0],[0,0,0],[0,0,0]
	winner=0
	while(checkb(board)==0):
		attack=0
		attack=input("Player 1:")
		board[int(int(attack)/10)][int(int(attack)%10)]=1
		printb(board)
		if(checkb(board)==0):
			attack=0
			attack=input("Player 2:")
			board[int(int(attack)/10)][int(int(attack)%10)]=-1
			printb(board)

def buildlayer(s,nextlayer,conncections):
	layer=[0]*s
	z=0
	while(z<s):
		layer[z]=InterNode(nextlayer,len(nextlayer),conncections)
		q=random.randint(0,1)
		if(q==0):
			layer[z].val=1
		if(q==1):
			layer[z].val=0
		else:
			layer[z].val=-1
		z=z+1
	return layer

def buildOutput():
	lastlayer=[0]*9
	temparray=[0]*9
	z=0
	while(z<9):
		lastlayer[z]=InterNode(temparray,0,-1)
		lastlayer[z].isOutputNode=1
		z=z+1
	return lastlayer	

def buildinput(b,nextlayer,conncections):
	inputlayer=[0]*9
	z=0
	while(z<9):
		inputlayer[z]=InterNode(nextlayer,len(nextlayer),conncections)
		z=z+1
	inputlayer[0].val=b[0][0]
	inputlayer[1].val=b[0][1]
	inputlayer[2].val=b[0][2]
	inputlayer[3].val=b[1][0]
	inputlayer[4].val=b[1][1]
	inputlayer[5].val=b[1][2]
	inputlayer[6].val=b[2][0]
	inputlayer[7].val=b[2][1]
	inputlayer[8].val=b[2][2]

	return inputlayer	

def layerprinter(layer):
	x=0
	while(x<len(layer)):
		print(layer[x].val)
		print()
		x=x+1

def outputAction(outputlayer,b):
	tempboard=deepcopy(b)
	moveMade=0
	if(outputlayer[0].val==1):
		tempboard[0][0]=1
		moveMade=moveMade+1
	if(outputlayer[1].val==1):
		tempboard[0][1]=1
		moveMade=moveMade+1
	if(outputlayer[2].val==1):		
		tempboard[0][2]=1
		moveMade=moveMade+1
	if(outputlayer[3].val==1):
		tempboard[1][0]=1
		moveMade=moveMade+1
	if(outputlayer[4].val==1):
		tempboard[1][1]=1
		moveMade=moveMade+1
	if(outputlayer[5].val==1):
		tempboard[1][2]=1
		moveMade=moveMade+1
	if(outputlayer[6].val==1):
		tempboard[2][0]=1
		moveMade=moveMade+1
	if(outputlayer[7].val==1):
		tempboard[2][1]=1
		moveMade=moveMade+1
	if(outputlayer[8].val==1):
		tempboard[2][2]=1
		moveMade=moveMade+1
	if(moveMade==1):
		return tempboard
	else:
		return b


def transmit(start,tv):
	looper=0
	linklooper=0
	tempvalue=tv
	while(looper<=len(start)-1):
		if(start[looper]!=None):
			tempvalue=start[looper].val+tempvalue
			while(linklooper<=len(start[looper].links)-1):
				if(start[looper].links[linklooper]!=None):
					if(start[looper].links[linklooper].isOutputNode==1):
						start[looper].links[linklooper].val	= tempvalue
					else:
						transmit(start[looper].links,tempvalue)
				linklooper=linklooper+1
		looper=looper+1


#x=[1,2,3]
#test=InterNode(x,100)
#testar=[test]
#test2=InterNode(testar,100)
#print(test2.links[0].links)

output=buildOutput()
#layer1=buildlayer(9,output,10)
inputl=buildinput(board,output,10)



transmit(inputl,0)

layerprinter(output)

outputAction(output,board)
printb(board)
