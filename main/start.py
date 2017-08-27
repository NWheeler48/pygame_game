import pygame

class start(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) # call Sprite initializer
		self.image = pygame.image.load("start.png")
		self.image = pygame.transform.scale(self.image,(200,200))
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = 0,0
		

