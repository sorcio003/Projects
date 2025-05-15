import sqlite3
from random import randint

conn = sqlite3.connect('Database/database.db')
cur = conn.cursor()
rarity = "3"
type = "attack"
i = 0
pg = list()
cur.execute(f'SELECT * from Characters where Rarity = {rarity} and Type = "{type}"')
for characters in cur:
    print(characters)
    pg.append(characters)
    i += 1
if i > 1:
    select = randint(1,i)
    print(pg[select-1])
    print(pg[select-1][0])
    
    
