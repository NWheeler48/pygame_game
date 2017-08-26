import pygame 
class controller():
	def __init__(self):
	'''Intializes the controller and sets up the game window'''
		pygame.init() 
		self.screen = pygame.display.set_mode((600,600))
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert() 
		self.white = (250,250,250)
		self.black = (0,0,0) 
		self.background.fill(self.black) 
		self.screen.blit(self.background,(0,0))
		pygame.display.flip() 
		while True: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT: #to quit hit x in top right corner
						return 
			

def main():
	'''Runs the controller infinetly until quit''' 
	while True:
		controller()
		return 
main()  
