import pygame, sys

class Button:
    
    def __init__(self, x, y):
        self.width = 100
        self.height = 50
        self.x = x
        self.y = y
        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x,self.y,self.width, self.height)
        self.base_font = pygame.font.Font(None, 32)
        self.color = pygame.Color('lightskyblue3')
        self.text = self.base_font.render("Crea", True, self.color)
        
    def draw(self, screen):
        pygame.draw.rect(screen, (100,0,0), (self.x,self.y,self.width, self.height))
        pygame.draw.rect(screen, (255,255,255), (self.x,self.y,self.width-3, self.height-5))
        pygame.draw.rect(screen, (0,0,0), (self.x,self.y,self.width-2, 1), 2)
        pygame.draw.rect(screen, (0,0,0), (self.x,self.y,1, self.height), 2)
        screen.blit(self.text, (self.x +22,self.y +12))
    
    def onMouseButtonDown(self, text, text1, text2, coordinate, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.button_rect.collidepoint(event.pos):
            print("Clicked")
            if not coordinate:
                coordinate = []
            coordinate.append(text)
            coordinate.append(text1)
            coordinate.append(text2)
            print(coordinate)
