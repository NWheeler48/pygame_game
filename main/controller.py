import pygame 
from background import Background

class controller():

	def __init__(self):
		'''Intializes the controller, sets up screen, clock, and repeated keys''' 
		pygame.init() 
		self.clock = pygame.time.Clock() 
		self.screen = pygame.display.set_mode((1000,1000))
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert() 
		self.white = (250,250,250)
		self.black = (0,0,0) 
		#self.background.fill(self.black)

		# TODO trying something
		self.screen.blit(self.background,(0,0))
		pygame.display.flip()
		pygame.key.set_repeat(500,30) #held key contiunes (delay, interval) 
		bground = Background('cavern.png', [0,0])
		while True:
			self.screen.fill([255,255,255])
			self.screen.blit(bground.image, bground.rect)
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
