# Displays highscores

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

back_0 = pygame.image.load('{}back_0.png'.format(way))
back_1 = pygame.image.load('{}back_1.png'.format(way))
back_2 = pygame.image.load('{}back_2.png'.format(way))

BACK = '1'

def show_scoretable(highscores, setts):
    if setts[1]:
        screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(setts[0])
        
    score_pict = pygame.image.load('storage/scoretable_{0[0]}_{0[1]}.jpg'.format(setts[0])).convert()
    screen.blit(score_pict, (0, 0))
    
    font = pygame.font.Font(None,40)
    i = 0
    for result in highscores:
        s = str(i + 1) + ')  ' + result[1]
        text = font.render(s, 1, (255, 255, 255))        
        screen.blit(text, (200 - 15 * (i // 9), 150 + i * 30))
        
        text = font.render(str(result[0]), 1, (255, 255, 255))        
        screen.blit(text, (550, 150 + i * 30))        
        i += 1

    pygame.display.update()
    
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
            
            if cursor.is_belong(Back_button):
                screen.blit(back_1, Back_button.first())
                active = True
            else:
                screen.blit(back_0, Back_button.first())          
        
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
            
            if cursor.is_belong(Back_button):
                screen.blit(back_2, Back_button.first()) 
                last_command = BACK  
                upgrade_buttons = False                
            
        elif event.type == MOUSEBUTTONUP:
            if last_command == BACK and cursor.is_belong(Back_button):
                return 2  
            
            upgrade_buttons = True        