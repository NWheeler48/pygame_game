import pygame, os, sys


"""
A base class for PyGame:

All classes that loads sprites or has sound will need to inherit this class
"""
class PyGameBase:

	def __init__(self):
		self.data = []

	def load_image(name, colorkey=None):
		'''Loads an image and converts it to use in pygame'''
		fullname = os.path.join("assets", name)
		image = pygame.image.load(fullname)
		image = image.convert_alpha()
		'pygame.transform.scale(image,(75,75))'#prob not needed
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
		return image, image.get_rect()

	def load_sound(name):
		'''Loads a ogg file for sound'''
		fullname = os.path.join('assets', name)
		sound = pygame.mixer.Sound(fullname)
		return sound


