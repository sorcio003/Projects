from random import randint
import pygame

def random_type():
		j = randint(1,4)
		type_card= ""
		if j == 1:
			type_card = "attack"
		if j == 2:
			type_card = "defense"
		if j == 3:
			type_card = "support"
		if j == 4:
			j = randint(1,100)
			if j > 75:
				j = randint(1,3)
				if j == 1:
					type_card = "attack_crystal_spell"
				if j == 2:
					type_card = "defense_crystal_spell"
				if j == 3:
					type_card = "support_crystal_spell"
			else:
				j = randint(1,3)
				if j == 1:
					type_card = "attack"
				if j == 2:
					type_card = "defense"
				if j == 3:
					type_card = "support"
			
		print(type_card)
		return type_card
def random_Rarity(i, type_card):
		card = pygame.image.load(f"Assets/Card/card_attack.png")
		if ("crystal_spell" in type_card):
			card = pygame.image.load(f"Assets/Card/card_{type_card}_5star.png")
			return card
		elif i <= 75:
			card = pygame.image.load(f"Assets/Card/card_{type_card}.png")
		elif i > 75 and i <= 90:
			card = pygame.image.load(f"Assets/Card/card_{type_card}_5star.png")
		elif i > 90:
			card = pygame.image.load(f"Assets/Card/card_{type_card}_legendary_12star.png")
		print(i)
		return card
def random_Star(i):
		rarity = ""
		if i <= 75:
			rarity = (pygame.image.load("Assets/Rarity/3_Star.png"))
		elif i > 75 and i <= 90:
			rarity = (pygame.image.load("Assets/Rarity/5_Star.png"))
		elif i > 90:
			rarity = (pygame.image.load("Assets/Rarity/12_Star.png"))

		return rarity
def check_rarity(i):
		rarity = 0
		if i <= 75:
			rarity = 3
		elif i > 75 and i <= 90:
			rarity = 5
		elif i > 90:
			rarity = 12
		print(rarity)

		return rarity
