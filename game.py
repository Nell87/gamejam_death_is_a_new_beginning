# Import main packages
import pygame

# Custom imports
from map_settings import *

# Global variables
surface = 0

# Initialize:
def init():
	global surface 
	pygame.init()	
	surface = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Death is a new beginning!!!")
	loadSprites()


# Load sprites
def loadSprites():
	global sprite_grass
	sprite_grass = pygame.image.load("sprites/grass.png")


# Drawing the grid
def drawGrid():
	for x in range(0, screen_width, tile_size):
		pygame.draw.line(surface, green, (x,0), (x, screen_height/2))

	for y in range(0, (int)(screen_height/2), tile_size):
		pygame.draw.line(surface, green, (0,y), (screen_width, y))

# Drawing the sprites
def drawSprite(sprite, x, y):
	col = 80*x
	row = 80*y
	surface.blit(sprite, (col,row))

# Main function 
def main():
	init()
	drawGrid()

	for x in range(0, (int)(screen_width/tile_size)):
		for y in range(0, (int)((screen_height/tile_size)/2)):
			drawSprite(sprite_grass, x,y)


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


#call the "main" function if running this script
if __name__ == '__main__': main()

###########################################################################################

