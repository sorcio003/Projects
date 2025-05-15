import pygame
import sqlite3
from random import randint

def load_pg(star, type):
		if "crystal_spell" in type:
			star = 5
		i = 0
		select = 0
		pg = list()
		conn = sqlite3.connect('Database/database.db')
		cur = conn.cursor()
		cur.execute(f'SELECT * from Characters where Rarity = "{star}" and Type = "{type}"')
		for characters in cur:
			print(characters)
			pg.append(characters)
			i += 1
		if i > 1:
			select = randint(1,i)
			print(pg[select-1][0])
			return pg[select-1]
		if i == 1:
			select = 1
			print(pg[select-1][0])
			return pg[select-1]
		