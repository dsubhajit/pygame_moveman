import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

from helper import *

class Hero(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('man.png',-1)
		self.positionx = 10
		self.positiony = 10

class PyManMain:
	def __init__(self, width=640,height=480):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))

	def LoadSprites(self):
		self.hero = Hero()
		self.hero_sprites = pygame.sprite.RenderPlain((self.hero))

	def MainLoop(self):
		self.LoadSprites()
		while 1:
			self.hero_sprites.draw(self.screen)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()

if __name__ == "__main__":
	MainWindow = PyManMain()
	MainWindow.MainLoop()
