import pygame

class Player(pygame.sprite.Sprite):
		def __init__(self, pos_x, pos_y):
			super().__init__()
			self.attack_animation = False
			self.x = pos_x
			self.y = pos_y
			self.sprites = []
			for i in range(24):
				image = pygame.image.load(f"animation/1/{i}.png")
				self.sprites.append(image)
			self.current_sprite = 0
			self.image = self.sprites[self.current_sprite]

			self.rect = self.image.get_rect()
			self.rect.topleft = [self.x,self.y]
		def load_animation(self, id, frame):

			self.sprites = []
			for i in range(frame-1):
				image = pygame.image.load(f"animation/{id}/{i}.png")
				self.sprites.append(image)
			self.current_sprite = 0
			self.image = self.sprites[self.current_sprite]

			self.rect = self.image.get_rect()
			self.rect.topleft = [self.x,self.y]

		def attack(self):
			self.attack_animation = True

		def update(self,speed):
			if self.attack_animation == True:
				self.current_sprite += speed
				if int(self.current_sprite) >= len(self.sprites):
					self.current_sprite = 0
					self.attack_animation = False

			self.image = self.sprites[int(self.current_sprite)]

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
