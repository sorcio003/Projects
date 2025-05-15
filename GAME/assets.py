import pygame

#Button image
image = pygame.image.load("Assets/button/summon.png")
reset = pygame.image.load("Assets/button/reset.png")

#Background Assets
background = pygame.image.load("Assets/BG/Background.png")

#Void Card 
none_card = pygame.image.load("Assets/Card/void.png")

#Coin
coin = pygame.image.load("Assets/Gems/blue_coin.png")
coin = pygame.transform.scale(coin, (30,30))