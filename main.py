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
		# Pixels to move each time
		self.x_dist = 5
		self.y_dist = 5
	
	def move(self,key):
		xMove = 0;
		yMove = 0;
		if (key == K_RIGHT):
			xMove = self.x_dist
		elif (key == K_LEFT):
			xMove = -self.x_dist
		elif (key == K_UP):
			yMove = -self.y_dist
		elif (key == K_DOWN):
			yMove = self.y_dist
		
		self.rect.move_ip(xMove,yMove);


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
		pygame.key.set_repeat(500, 30)
		clock = pygame.time.Clock()
		self.LoadSprites()

		while 1:
			clock.tick(50)
			keystates={'up':False, 'down':False, 'left':False, 'right':False}
			pygame.display.flip()
			self.hero_sprites.draw(self.screen)
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == K_UP:
						keystates['up']=True
					elif event.key == K_DOWN:
						keystates['down'] = True
					elif event.key == K_LEFT:
						keystates['left'] = True
					elif event.key == K_RIGHT:
						keystates['right'] = True
						
			#keys = pygame.key.get_pressed()
			#if keys[K_LEFT]:
			#	keystates['left'] = True
			#if keys[K_RIGHT]:
			#	keystates['right'] = True
			#if keys[K_UP]:
			#	keystates['up'] = True
			#if keys[K_DOWN]:
			#	keystates['down'] = True

			if keystates['up'] == True:
				self.screen.fill((0,0,0))
				self.hero.move(K_UP)
			if keystates['down'] == True:
				self.screen.fill((0,0,0))
				self.hero.move(K_DOWN)
			if keystates['left'] == True:
				self.screen.fill((0,0,0))
				self.hero.move(K_LEFT)
			if keystates['right'] == True:
				self.screen.fill((0,0,0))
				self.hero.move(K_RIGHT)

if __name__ == "__main__":
	MainWindow = PyManMain()
	MainWindow.MainLoop()
