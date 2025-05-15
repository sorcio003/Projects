import pygame, sys, os

def Path():
    path = os.getcwd()

    path = path.split('\\')
    new_path = ""

    for parola in path:
        new_path += parola+"\\"
        if parola == "Desktop":
            break
    
    return new_path

def createTXT(text_1, text_2, text_3):
    file = open(Path()+"g-code.txt", 'w')
    
    y = int(text_2) 
    
    file.write("M3\n")
    file.write("F500\n")
    file.write("G92 X0\n")
    file.write("G92 Y0\n")
    for i in range(0,text_3,2):
        file.write("G01 X0 Y"+str(y*i)+"\n")
        file.write("G01 X"+text_1+" Y"+str(y*i)+"\n")
        file.write("G01 X"+text_1+" Y"+str(y*(i+1))+"\n")
        file.write("G01 X0 Y"+str(y*(i+1))+"\n")
    file.write("M5")
    
    file.close()

def displayText(screen, name, x, y):
    base_font = pygame.font.Font(None, 32)
    
    text = base_font.render(name, True, (0,0,0))
    pygame.draw.rect(screen, (0,0,0), (x-10,y+10,x-20, 70), 2)
    screen.blit(text, (x, y+35))
