import random, time, os
import pygame
from pygame import mixer


pygame.mixer.init() 
pygame.init()


fond=pygame.font.Font('freesansbold.ttf', 50)

screen= pygame.display.set_mode((1400, 900))
pygame.display.set_caption('tri')

screen.fill((255, 255, 255))
class cadre:
	def __init__(self, width, height):
		self.width=width
		self.height=height
		self.cells=[]
		for j in range(height):
			liste=[]
			lst=[]
			for i in range(width):
				liste.append({'ouvert': False, "zone":i+(width*j)})
			self.cells.append(liste)



	def bord(self, i, j):
		if i<1 or i>=self.height-1 or j<1 or j>=self.width-1:
			return True
		else:
			return False


	def ouvre(self):
		l=[]
		for i in range(self.width-1):
				for j in range(self.height-1):
					if not self.bord(i, j):
						v=0
						#for t in range(3):
						liste=liste=[self.cells[i-1][j]['ouvert'] , self.cells[i+1][j]['ouvert'] , self.cells[i][j-1]['ouvert'] , self.cells[i][j+1]['ouvert'] , self.cells[i-1][j-1]['ouvert'] , self.cells[i-1][j+1]['ouvert'] , self.cells[i+1][j-1]['ouvert'] , self.cells[i+1][j+1]['ouvert']]
						b=liste.count(True)
							#if b<=3 or b==2:
							#	v+=1
						#if v==3 or v==2:
						if self.cells[i][j]['ouvert']:
							if b==3 or b==2:
								pass
							else:
								self.cells[i][j]['ouvert']=False
						else:
							if b==3:
								self.cells[i][j]['ouvert']=True
							#else:
							#	self.cells[i][j]['ouvert']=False


	def clear(self):
		width=self.width
		height=self.height
		for j in range(height):
			for i in range(width):
				self.cells[j][i]['ouvert']=False


	def lance(self):
		for i in range(400):
			t=random.randint(0, self.width-1)
			v=random.randint(0, self.height-1)
			if not self.bord(t, v):
				self.cells[t][v]['ouvert']=True

	def print(self):
		run=True
		lff=[i for i in range(10040)]
		blc=10
		recycle=0
		self.lance()
		while run:
			open_cells=0
			screen.fill((255, 255, 255))
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					run=False
				if event.type == pygame.MOUSEBUTTONUP:
					self.lance()
					#pos = pygame.mouse.get_pos()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.clear()

			for i in range(self.width):
				for j in range(self.height):
					#pygame.draw.rect(screen,(0, 0,0) , pygame.Rect(i*blc,j*blc, blc, blc), etr)
					pygame.draw.rect(screen,(0, 0,0) , pygame.Rect(i*blc,j*blc, blc, blc), 0 if self.cells[i][j]['ouvert'] else 2)
					if self.cells[i][j]['ouvert']:
						open_cells+=1
			self.ouvre()
			#time.sleep(0.4)

			niveau1 = pygame.draw.rect(screen,((200,0,0)),(950, 90, 950, 95))
			text1 = fond.render('Ajouter : (CLIC)', True, (255, 255, 255))
			screen.blit(text1,(950, 95))

			niveau1 = pygame.draw.rect(screen,((200,0,0)),(950, 300, 950, 95))
			text1 = fond.render('Effacer : (ESPACE)', True, (255, 255, 255))
			screen.blit(text1,(950, 305))


			niveau1 = pygame.draw.rect(screen,((200,0,0)),(950, 800, 950, 95))
			if open_cells==recycle:
				txt='stable'
				text1 = fond.render(txt, True, (255, 255, 255))
				screen.blit(text1,(950, 840))
			text1 = fond.render('Habitant: '+str(open_cells), True, (255, 255, 255))
			recycle=open_cells
			screen.blit(text1,(950, 800))
			pygame.display.update()


cdr=cadre(90, 90)

cdr.print()





