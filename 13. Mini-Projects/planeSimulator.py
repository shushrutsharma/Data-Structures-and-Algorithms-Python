from scene import *
from math import *
from random import *
from time import *
timesHold = []

SYSTEMLIST = ['BtF','WtA','R','Ste','Wil','FtB','']
#SYSTEMLIST = ['Wil','']
TRANSITION = True


class Game (Scene):
	def setup(self):	
		#R  : Random
		#BtF: Back to Front
		#FtB: Front to Back
		#WtA: Window Middle Aisle
		#Ste: Steffen method
		#Wil: WILMA
		
		try:
			self.method = SYSTEMLIST.index(self.SYSTEM)+1
		except:
			self.method = 0
		#if self.method == len(SYSTEMLIST):
			
			
			
		#print(self.method,'=====')
		self.background_color='#f6fbff'
		font = ('Avenir Next', 12)
		self.textB = LabelNode('',font)
		self.textB.color = 'black'
		self.add_child(self.textB)
		self.textB.position = (50,self.size.h-30-self.method*50)
		
		self.SYSTEM = SYSTEMLIST[self.method]
		if self.SYSTEM == 'R':
			self.textB.text='Random'
		if self.SYSTEM == 'BtF':
			self.textB.text='Back to Front'
		if self.SYSTEM == 'FtB':
			self.textB.text='Front to Back'
		if self.SYSTEM == 'WtA':
			self.textB.text='Window to Aisle'
		if self.SYSTEM == 'Ste':
			self.textB.text='Steffen Method'
		if self.SYSTEM == 'Wil':
			self.textB.text='WILMA'
		
		self.studder = time()+10000
		self.line = []
		
		self.seatMap = []
		for i in range(24):
			temp = []
			for j in range(6):
				temp.append([' '])
			self.seatMap.append(temp)
			
			self.line.append(temp)
		
			
		for i in range(len(self.seatMap)):
			for j in range(len(self.seatMap[i])):
				self.seat(i,j)
				
		
		temp = []
		for i in self.seatMap:
			for j in i:
				temp.append(j)
				
		
		self.seatMap = temp
		if self.SYSTEM == 'R':
			shuffle(self.seatMap)
		if self.SYSTEM == 'BtF':
			n = len(self.seatMap)//3
			one=self.seatMap[0:n]
			two=self.seatMap[n:n*2]
			three=self.seatMap[n*2:n*3]
			shuffle(one)
			shuffle(two)
			shuffle(three)
			self.seatMap = three + two + one
		if self.SYSTEM == 'FtB':
			n = len(self.seatMap)//3
			one=self.seatMap[0:n]
			two=self.seatMap[n:n*2]
			three=self.seatMap[n*2:n*3]
			shuffle(one)
			shuffle(two)
			shuffle(three)
			self.seatMap = one + two + three
		if self.SYSTEM == 'WtA':
			n = len(self.seatMap)//3
			one = []
			two = []
			three = []
			
			for i in range(0,len(self.seatMap)//3):
				one.append(self.seatMap[3*i])
				two.append(self.seatMap[3*i+1])
				three.append(self.seatMap[3*i+2])
			shuffle(one)
			shuffle(two)
			shuffle(three)
			
			self.seatMap = three + two + one
		if self.SYSTEM == 'Ste':
			temp = []
			for i in self.seatMap:
				temp.append(' ')
			#print(len(self.seatMap))
			for i in range(len(self.seatMap)):
			
				number = [11,8,5,2,10,7,4,1,9,6,3,0]
				
				
				temp[i] = self.seatMap[(number[i//12]+(11-(i%12))*12)]
				
			self.seatMap = temp
		if self.SYSTEM == 'Wil':
			n = len(self.seatMap)//2
			one=self.seatMap[0:n]
			two=self.seatMap[n:n*2]
			oneW=[]
			twoW=[]
			for i in range(len(one)-1,1,-3):		
				oneW.append(one.pop(i))
				twoW.append(two.pop(i))
			for i in two:
				i.color = '#bfffbf'
			for i in twoW:
				i.color = '#bbbfff'
			for i in one:
				i.color = '#ffbfbf'
			for i in oneW:
				i.color = '#ffffbf'
			
			shuffle(one)
			shuffle(two)
			shuffle(oneW)
			shuffle(twoW)
			self.seatMap = twoW + two + oneW + one
			
		
		for i in range(len(self.seatMap)):
			#self.person(i%6,i//6)
			self.person(i//6,i%6)
			
		
		temp = []
		for i in self.line:
			for j in i:
				temp.append(j)
				j.assigned.position = j.gotoPos[0], j.gotoPos[1]+836
		self.line = temp
		self.end = False
		self.done = False
		self.enter = True
		self.moving = False
		
		
		
	def update(self):
		if self.enter:
			if not self.moving:
				self.studderB = time()
				self.moving = True
			if self.moving:
				acc = (((self.studderB)-time()+4)**2)/1.5
				#for item in self.line:
				#	item.position = item.position.x,item.position.y-acc
				for item in self.seatMap:
					item.position = item.position.x,item.position.y-acc
			item = self.seatMap[0]
			if item.position.y < item.assigned.gotoPos[1]:
				self.enter = False 
				for item in self.seatMap:
					item.position = item.assigned.gotoPos
				self.START = time()
			#print(item.position.y - item.assigned.gotoPos[1])
			
		if not self.enter:
			for i in range(len(self.line)):
				k = self.line[i]
				dis=True
				minDis=1000
				for l in range(i):
					j = self.line[l]
					temp = abs(k.position.y - j.position.y)
					if temp < minDis and j != k and not j.inSeat:
						minDis=temp
				dis = (minDis > 30)
				
				spe = 8
				n = 1.5
				speSeat = 4
				'''
				spe = 16
				n = 0
				speSeat = 16
				'''
				
				
				if not k.inSeat and not k.paused:
					if dis or i == 0:
						k.position=(k.position.x,k.position.y+spe)
						
				if k.paused and not k.inSeat:
					pick = k.assigned
					
					
					
					if (pick.position.x < self.size.w/2):
						for l in self.seatMap:
							if l.position.y == pick.position.y and l.position.x > pick.position.x and l.position.x < self.size.w/2:
								if l.assigned.inSeat:
									speSeat-=n
								
					if (pick.position.x > self.size.w/2):
						for l in self.seatMap:
							if l.position.y == pick.position.y and l.position.x < pick.position.x and l.position.x > self.size.w/2:
								if l.assigned.inSeat:
									speSeat-=n
					
							
					if (k.gotoPos[0] < self.size.w/2):
						k.position=(k.position.x-speSeat,k.position.y)
					else:
						k.position=(k.position.x+speSeat,k.position.y)
				if (k.position.y >= k.gotoPos[1]) and not k.paused and not k.inSeat:
					
					
					
					k.paused = True
					#k.color='white'
					k.position = (k.position.x,k.gotoPos[1])
				
				
				
				if abs(k.position.x - (self.size.w/2)) > 30:
					k.inSeat = True
					#k.position = k.gotoPos	
					#k.color='blue'
				
	
				if k.inSeat and not self.done:
					pick = k.assigned
					
					
					
					if (pick.position.x < self.size.w/2):
						for l in self.seatMap:
							if l.position.y == pick.position.y and l.position.x > pick.position.x and l.position.x < self.size.w/2:
								if l.assigned.inSeat:
									speSeat-=n
								
					if (pick.position.x > self.size.w/2):
						for l in self.seatMap:
							if l.position.y == pick.position.y and l.position.x < pick.position.x and l.position.x > self.size.w/2:
								if l.assigned.inSeat:
									speSeat-=n
					
							
					if (k.gotoPos[0] < self.size.w/2):
						#k.color='red'
						k.position=(k.position.x-speSeat,k.position.y)
						if (k.position.x - k.gotoPos[0]) <= 0:
							k.position = k.gotoPos
					else:
						
						k.position=(k.position.x+speSeat,k.position.y)
						if (k.position.x - k.gotoPos[0]) >= 0:
							k.position = k.gotoPos
				
			
				
					
			#self.line[0].color='green'
			#print(self.line[1].paused)
			#print(self.line[1].time-time())
			
		if self.line[-1].inSeat:
			test = True
			for i in self.line:
				if not i.position == i.assigned.position:
					test = False
			if test:
				self.end = True
		if self.end and not self.done:
			self.studder=time()+4
			timesHold.append(time()-self.START)
			self.done = True
		if self.done:
			acc = ((time()-(self.studder-4))**2)/1.5
			#print(acc)
			for item in self.line:
				item.position = item.position.x,item.position.y-acc
			for item in self.seatMap:
				item.position = item.position.x,item.position.y-acc
			
			#for item in self.seatMap:
			#	item.remove_from_parent()
		if self.studder < time():
			for item in self.line:
				item.remove_from_parent()
			for item in self.seatMap:
				item.remove_from_parent()
			
			sum = 0
			for i in timesHold:
				sum+=i
			
			
			font = ('Avenir Next', 12)
			self.textT = LabelNode('Error',font)
			self.textT.color = 'black'
			self.add_child(self.textT)
			self.textT.position = (50,self.size.h-50-self.method*50)
			
			score = str(timesHold[-1])[0:5] + ' seconds'
			self.textT.text = score
			#print('Average:',sum/len(timesHold),'  Runs:',len(timesHold))
			
			self.setup()
			
	def seat(self,row,seat):
		
		place=SpriteNode('pzl:Gray3')
		
		place.assigned = 0
		
		place.scale = 0.9
		place.inSeat = False
		self.add_child(place)
		#if row % 5 == 0:
		#	tile.color='red'
		
		if self.SYSTEM == 'BtF':
			n = len(self.seatMap)/3
			if 0 <= row and n > row:
				place.color='#ffbfbf'
			if n <= row and 2*n > row:
				place.color='#bfffbf'
			if 2*n <= row and 3*n > row:
				place.color='#bbbfff'
				
		if self.SYSTEM == 'FtB':
			n = len(self.seatMap)/3
			if 0 <= row and n > row:
				place.color='#bbbfff'
			if n <= row and 2*n > row:
				place.color='#bfffbf'
			if 2*n <= row and 3*n > row:
				place.color='#ffbfbf'
		
		if self.SYSTEM == 'WtA':
		
			if seat == 2 or seat == 5:
				place.color='#bbbfff'
			if seat == 1 or seat == 4:
				place.color='#bfffbf'
			if seat == 0 or seat == 3:
				place.color='#ffbfbf'
		n=5
		'''
		if self.SYSTEM == 'Ste':		
			print('Ok')
			place.color = (randint(0,n)/n, randint(0,n)/n, randint(0,n)/n)
			print(place.color)
		'''
		self.seatMap[row][seat] = place
		rowSpace = 30
		seatSpace = 30
		if seat >= len(self.seatMap[0])/2:
			x=self.size.w/2+(seat-2.5)*seatSpace+seatSpace/2
		else:
			x=self.size.w/2+(-seat-0.5)*seatSpace-seatSpace/2
		place.position=(x,(row+1)*rowSpace)
		
		
		
	def person(self,row,seat):
		person=SpriteNode('pzl:BallGray')
		person.z_position = 4
		person.scale = 1
		person.inSeat = False
		person.paused = False
		person.time = time()+1000
		self.add_child(person)
		#if row % 5 == 0:
		#	tile.color='red'
		
		#colorList=[(1.0,0.0,0.0,1.0),(1.0,0.65,0.0,1.0),(1.0,1.0,0.0,1.0),(0.0,0.5,0.0,1.0),(0.0,0.0,1.0,1.0),(0.5,0.0,0.5,1.0),(1.0,0.75,0.8,1.0)]
		#person.color=choice(colorList)
		
		'''
		if self.SYSTEM != 'R':
			n = len(self.seatMap)/18
			if 0 <= row and n > row:
				person.color='#9ba4ff'
			if n <= row and 2*n > row:
				person.color='#9bffa4'
			if 2*n <= row and 3*n > row:
				person.color='#ff9b9b'
		'''
		
		self.line[row][seat] = person
		self.seatMap[row*6+seat].assigned = person
		person.assigned = self.seatMap[row*6+seat]
		rowSpace = 30
		
		person.color = person.assigned.color
		
		person.gotoPos = [self.seatMap[row*6+seat].position.x,self.seatMap[row*6+seat].position.y]
		
		person.row = row
		person.seat = seat
		
		person.position=(self.size.w/2,-(row*6+seat)*rowSpace-400)
		
if __name__ == '__main__':
	run(Game(), PORTRAIT, show_fps=True)
