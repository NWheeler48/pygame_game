import pygame 
class controller():
	def __init__(self):
		'''Intializes the controller, sets up screen, clock, and repeated keys''' 
		pygame.init() 
		self.clock = pygame.time.Clock() 
		self.screen = pygame.display.set_mode((600,600))
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert() 
		self.white = (250,250,250)
		self.black = (0,0,0) 
		self.background.fill(self.black) 
		self.screen.blit(self.background,(0,0))
		pygame.display.flip()
		pygame.key.set_repeat(500,30) #held key contiunes (delay, interval) 
		while True: 
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT: #to quit hit x in top right corner
						return 
			

def main():
	'''Runs the controller infinetly until quit''' 
	while True:
		controller()
		return 
main()  
