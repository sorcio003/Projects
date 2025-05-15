import pygame, sys, os
from button import Button
from text_field import Text_Field
from function import createTXT, displayText

pygame.init()
clock = pygame.time.Clock()
background = pygame.image.load("creativity_lab.png")
bg_color = (255, 255, 255)
screen = pygame.display.set_mode((700,400))

pygame.display.set_caption("Mech3 File.txt")

running = True

cordinate = []

text = Text_Field(250,200,140,32)
text_2 = Text_Field(400,200,140,32)
text_3 = Text_Field(400,300,140,32)

button = Button(550, 300)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            text.isCollided(event)
            text_2.isCollided(event)
            text_3.isCollided(event)
            
        if event.type == pygame.KEYDOWN:
            text.writing(event) 
            text_2.writing(event) 
            text_3.writing(event) 
    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            button.onMouseButtonDown(text.user_text, text_2.user_text, text_3.user_text, cordinate, event) 
            r = int(text_3.user_text)
            createTXT(text.user_text, text_2.user_text, r)

    screen.fill(bg_color)
    screen.blit(background, (20, 20))
    displayText(screen, "G-CODE GENERATOR", 300, 25)
    
    text.Draw(screen, "Lunghezza")
    text_2.Draw(screen, "Altezza")
    text_3.Draw(screen, "Ripetizioni")
    button.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)