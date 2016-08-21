import random


class InterNode(object):
    def __init__(self,nextlayer, complexity):
        self.val = 0
        self.links=nextlayer
        if nextlayer != None:
        	counter=0
        	while(counter<len(self.links)):
        		if(random.randint(0,100)<=complexity):
        			self.links[counter]=nextlayer[random.randint(0,len(nextlayer)-1)]
        		else:
        			self.links[counter]=None
        		counter=counter+1

board =[0,0,0],[0,0,0],[0,0,0]
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

def pvp(b):
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
def buildlastlayer(s):
	lastlayer=[0]*s
	temparray=[0]*s
	z=0
	while(z<s):
		lastlayer[z]=InterNode(temparray,-1)
		z=z+1
	return lastlayer	


x=[1,2,3]
test=InterNode(x,100)
testar=[test]
test2=InterNode(testar,100)
print(test2.links[0].links)
yy=buildlastlayer(5)
print(yy[0].links)