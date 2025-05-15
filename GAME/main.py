import pygame, sys, asyncio
from random import randint
import sqlite3
from config import *
from assets import *
from Player import *
from function import *
from database_load import *


async def main():
	class Button():
		def __init__(self, x, y, image):
			self.image = image
			self.rect = self.image.get_rect()
			self.rect.topleft = (x,y)
			self.clicked = False

		def draw(self):
			screen.blit(self.image, (self.rect.x, self.rect.y))
		def action(self):
			action = False

			pos = pygame.mouse.get_pos()

			if self.rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
					self.clicked = True
					action = True
				if pygame.mouse.get_pressed()[0] == 0:
					self.clicked = False
					action = False

			

			return action

	# General setup
	pygame.init()
	clock = pygame.time.Clock()

	# Game Screen
	screen = pygame.display.set_mode((screen_width,screen_height))
	pygame.display.set_caption("Sprite Animation")

	x_pos = 100
	y_pos = 100

	money = 100
	#First pressure for Summon
	first_pressure = False

	player = Player(x_pos,y_pos)
	moving_sprites.add(player)

	summon_button = Button(300, 100, image)
	reset_button = Button(300, 170, reset)

	pressed = pygame.key.get_pressed()
	def draw_text():
		text = font.render(str(money), True, white)
		screen.blit(text, (500,15))
	def draw_name(pg):
		text = Font.render(pg, True, (0,0,0))
		screen.blit(text, (x_pos+10,y_pos-25))

	nome = ""
	rooster = list()

	while True:
		for event in pygame.event.get():		
			if summon_button.action() and money >= 10:
				pg = list()
				first_pressure = True
				rare = 0
				i = randint(0,100)
				type_card = random_type()
				card = random_Rarity(i, type_card)
				star = random_Star(i)
				rare = check_rarity(i)
				pg.append(load_pg(rare, type_card))
				player.load_animation(pg[0][0],pg[0][5])
				nome = pg[0][1]
				rooster.append(pg)
				money -=10
			if reset_button.action() and money == 0:
				nome = ""
				first_pressure = False
				money = 100
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		player.attack()

		# Drawing
		screen.fill((0,0,0))
		screen.blit(background, (0,0))
		screen.blit(coin, (450,10))
		draw_text()
		summon_button.draw()
		reset_button.draw()
		if not first_pressure:
			screen.blit(none_card, (x_pos-40,y_pos-50))
		else:
			screen.blit(card, (x_pos-40,y_pos-50))
			moving_sprites.draw(screen)
			moving_sprites.update(0.25)
			screen.blit(star, (x_pos-40,y_pos-50))
		
		draw_name(nome)
		pygame.display.flip()
		clock.tick(60)
		await asyncio.sleep(0)

asyncio.run(main())