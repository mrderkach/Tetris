# Displays menu after a player has achieved a new highscore. 
# Asks player for a highscore name and continues to main menu.

import pygame, sys
from pygame.locals import *

from bin import geom
from bin.geom import *

from parametres import buttons
from parametres.buttons import *

pygame.init()

#------
#Loading music and pictures
#------
music = ['music/music1.mp3']
way = 'storage/Buttons/'

cont_0 = pygame.image.load('{}cont_0.png'.format(way))
cont_1 = pygame.image.load('{}cont_1.png'.format(way))
cont_2 = pygame.image.load('{}cont_2.png'.format(way))

CONTINUE = '1'

# Save the highscore
def save_n_quit(name, score, highscores):    
    if name == '':
        name = 'Player'
    highscores_new = highscores[:-1] + [(score, name)]
    highscores_new.sort()
    
    f = open('parametres/highscores.py', 'w')
    f.write('''highscores = [({0[0][0]}, '{0[0][1]}'),
    ({0[1][0]}, '{0[1][1]}'),
    ({0[2][0]}, '{0[2][1]}'),
    ({0[3][0]}, '{0[3][1]}'),
    ({0[4][0]}, '{0[4][1]}'),
    ({0[5][0]}, '{0[5][1]}'),
    ({0[6][0]}, '{0[6][1]}'),
    ({0[7][0]}, '{0[7][1]}'),
    ({0[8][0]}, '{0[8][1]}'),
    ({0[9][0]}, '{0[9][1]}')]
'''.format(highscores_new[::-1]))
    
    return highscores_new[::-1]    
    
# Ask player for a name
def set_new_record(score, highscores, setts):
    if setts[1]:
        screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(setts[0]) 
        
    new_record_pict = pygame.image.load('storage/new_record_{0[0]}_{0[1]}.jpg'.format(setts[0])).convert()
    new_text = pygame.image.load('storage/record_nick.jpg').convert()      
        
    screen.blit(new_record_pict, (0, 0))  
    
    font = pygame.font.Font(None,50)
    text = font.render(str(score), 1, (255, 255, 255))        
    screen.blit(text, (260, 278))
    pygame.display.update() 
    
    pos = 0
    name = ''
    upper = 0
    upgrade_buttons = True
    last_command = 0
    last_active = False     
    
    while True:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(music[0])
            pygame.mixer.music.play(10)
            
        #------
        #UPDATING BUTTONS
        #------
        cursor = Point(pygame.mouse.get_pos()) 
        if upgrade_buttons:
            active = False
            
            if cursor.is_belong(Continue_button):
                screen.blit(cont_1, Continue_button.first())
                active = True
            else:
                screen.blit(cont_0, Continue_button.first())          
        
            if active and not last_active:
                last_active = True
                #pygame.mixer.music.load('music/button.mp3')
                #pygame.mixer.music.play(0)            
            elif not active:
                last_active = False
        pygame.display.update()   
        
        #------
        #DOING USER COMMANDS
        #------       
                    
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:
            cursor = Point(event.pos)
            
            if cursor.is_belong(Continue_button):
                screen.blit(cont_2, Continue_button.first()) 
                last_command = CONTINUE
                upgrade_buttons = False                 
            
        elif event.type == KEYDOWN:
            letter = event.key
            
            if letter > 96 and letter < 123 and pos < 21:                    #characters
                if upper == 0:
                    name += chr(letter)
                else:
                    name += chr(letter - 32)
                font = pygame.font.Font(None,50)
                text = font.render(name, 1, (255, 255, 255))        
                screen.blit(text, (325, 192)) 
                pygame.display.update() 
                pos += 1
                
            elif letter == K_RSHIFT or letter == K_LSHIFT:
                upper += 1
                
            elif (letter == K_SPACE or (letter > 45 and letter < 58)) and pos < 21:         # 0-9 and ' ', '.' and '/'
                name += chr(letter)
                font = pygame.font.Font(None,50)
                text = font.render(name, 1, (255, 255, 255))        
                screen.blit(text, (325, 192))
                pygame.display.update() 
                pos += 1
                
            elif letter == K_BACKSPACE:
                pos -= 1
                name = name[:-1]
                screen.blit(new_text, (305, 150))
                font = pygame.font.Font(None,50)
                text = font.render(name, 1, (255, 255, 255))        
                screen.blit(text, (325, 192))
                pygame.display.update()
                
            elif letter == 13:
                return save_n_quit(name, score, highscores)
                
        elif event.type == KEYUP and (event.key == K_RSHIFT or event.key == K_LSHIFT):
            upper -= 1
            
        elif event.type == MOUSEBUTTONUP:
            if last_command == CONTINUE and cursor.is_belong(Continue_button):
                return save_n_quit(name, score, highscores) 
            
            upgrade_buttons = True          