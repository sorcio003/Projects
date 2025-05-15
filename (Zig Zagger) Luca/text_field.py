import pygame, sys

class Text_Field:
    
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.input_rect = pygame.Rect(x,y,height,width)
        self.active = False
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = '0'
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('gray15')

        self.color = self.color_passive
    
    def isCollided(self, event):
        if self.input_rect.collidepoint(event.pos):
            self.active = True
        else:
            self.active = False
            
    def writing(self, event):
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode 
    
    def Draw(self, screen, name):
        
        text = self.base_font.render(name, True, (0,0,0))
        
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive
        
        pygame.draw.rect(screen, self.color, self.input_rect, 2)
        
        text_surface = self.base_font.render(self.user_text, True, (0,0,0))
        screen.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        screen.blit(text, (self.input_rect.x, self.input_rect.y+35))
        
        self.input_rect.w = max(100,text_surface.get_width() + 10)
