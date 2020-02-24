# Game Over Menu

import pygame, sys
from pygame.locals import *

from bin import geom, scoretable, new_record
from bin.geom import *
from bin.scoretable import *
from bin.new_record import *

from parametres import buttons
from parametres.buttons import *

pygame.init()
#------
#Loading music and pictures
#------
music = ['music/music1.mp3']
way = 'storage/Buttons/'

restart_0 = pygame.image.load('{}restart_0.png'.format(way))
restart_1 = pygame.image.load('{}restart_1.png'.format(way))
restart_2 = pygame.image.load('{}restart_2.png'.format(way))

highsc_0 = pygame.image.load('{}highsc_0.png'.format(way))
highsc_1 = pygame.image.load('{}highsc_1.png'.format(way))
highsc_2 = pygame.image.load('{}highsc_2.png'.format(way))

menu_0 = pygame.image.load('{}menu_0.png'.format(way))
menu_1 = pygame.image.load('{}menu_1.png'.format(way))
menu_2 = pygame.image.load('{}menu_2.png'.format(way))

RESTART = '1'
HIGHSCORES = '2'
MENU = '3'

SCORE_COORDINATES = (650, 182)

def game_over_menu(score, highscore_table, setts):
    if setts[1]:
        screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(setts[0])    
    game_over = pygame.image.load('storage\Game_over_{0[0]}_{0[1]}.jpg'.format(setts[0])).convert()    
    
    screen.blit(game_over, (0, 0))  
    
    font = pygame.font.Font(None, 50)
    text = font.render(str(score), 1, (0, 0, 0)) 
    screen.blit(text, SCORE_COORDINATES)
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
            
            if cursor.is_belong(Restart_button):
                screen.blit(restart_1, Restart_button.first())
                active = True
            else:
                screen.blit(restart_0, Restart_button.first())
                
            if cursor.is_belong(Highscores_button):
                screen.blit(highsc_1, Highscores_button.first())
                active = True
            else:
                screen.blit(highsc_0, Highscores_button.first())     
                
            if cursor.is_belong(Menu_button):
                screen.blit(menu_1, Menu_button.first())
                active = True
            else:
                screen.blit(menu_0, Menu_button.first())   
                
            if active and not last_active:
                last_active = True
                #pygame.mixer.music.load('music/button.mp3')
                #pygame.mixer.music.play(0)            
            elif not active:
                last_active = False
        pygame.display.update()   
        
        #------
        #DOING USER's COMMANDS
        #------          

        event = pygame.event.wait()        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()    
            
        elif event.type == MOUSEBUTTONDOWN:
            cursor = Point(event.pos)
            upgrade_buttons = False
            
            if cursor.is_belong(Restart_button):
                screen.blit(restart_2, Restart_button.first())
                last_command = RESTART
            
            elif cursor.is_belong(Highscores_button):
                screen.blit(highsc_2, Highscores_button.first())
                last_command = HIGHSCORES           
                
            elif cursor.is_belong(Menu_button):
                screen.blit(menu_2, Menu_button.first())
                last_command = MENU                 
            
            pygame.display.update()
                        
        elif event.type == MOUSEBUTTONUP:
                        
            if last_command == RESTART and cursor.is_belong(Restart_button):
                return 1
                
            elif last_command == HIGHSCORES and cursor.is_belong(Highscores_button):
                show_scoretable(highscore_table, setts)
                
                screen.blit(game_over, (0, 0))    
                
                font = pygame.font.Font(None, 50)
                text = font.render(str(score), 1, (0, 0, 0)) 
                screen.blit(text, SCORE_COORDINATES)
                pygame.display.update() 
                
            elif last_command == MENU and cursor.is_belong(Menu_button):
                return 2            
            
            upgrade_buttons = True         