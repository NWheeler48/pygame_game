import pygame 
from background import Background
import start 
class controller():

	def __init__(self):
		'''Intializes the controller, sets up screen, clock, and repeated keys''' 
		pygame.init() 
		height = 800
		width = height 
		self.clock = pygame.time.Clock() 
		self.screen = pygame.display.set_mode((height,width))
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert() 
		self.white = (250,250,250)
		self.black = (0,0,0) 
		#self.background.fill(self.black)

		# TODO trying something
		self.screen.blit(self.background,(0,0))
		#pygame.display.flip()
		pygame.key.set_repeat(500,30) #held key contiunes (delay, interval) 
		bground = Background('cavern.png', [0,0],height,width)
		button = start.start() 
		self.startScreen = True
		self.gameScreen = False
		self.endScreen = False
		while self.startScreen == True: 
			self.screen.fill(self.white) 
			self.screen.blit(button.image,(300,400))
			pygame.display.flip() 
			for event in pygame.event.get():
				loci = pygame.mouse.get_pos() 
				clicker = pygame.mouse.get_pressed()
				xcor = False
				locix = loci[0]
				if locix >= 345 and locix <= 440:
					xcor = True
				if xcor == True and clicker[0] == 1:
					self.startScreen = False
					self.gameScreen = True
				if event.type == pygame.QUIT: #to quit hit x in top right corner
						return 
		while self.gameScreen == True:
			self.screen.fill([255,255,255])
			self.screen.blit(bground.image, bground.rect)
			pygame.display.flip() 
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT: #to quit hit x in top right corner
						return 
			

def main():

	# Initialize all the game objects




	'''Runs the controller infinitely until quit'''
	while True:
		controller()
		return
main()
