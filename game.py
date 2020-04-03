import pygame
import sys
from map_settings import *


# GAME 
pygame.init()
surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello!!!")

surface.fill(green)




# Maintain the screen opened 
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			pygame.quit()
			sys.exit()
	pygame.display.update()




# Drawing the grid
def draw_grid(self):
	for x in range(0, width, tile_size):
		pygame.draw.line(self.screen, WHITE, (x,0), (x, height))


# Draw function
def draw(self):
	self.screen.fill(DARKGREY)