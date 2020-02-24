# Pause Menu

import pygame, sys
from pygame.locals import *

from bin import *
from bin.geom import *
from bin.settings import *

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

restart_0 = pygame.image.load('{}restart_0.png'.format(way))
restart_1 = pygame.image.load('{}restart_1.png'.format(way))
restart_2 = pygame.image.load('{}restart_2.png'.format(way))

setts_0 = pygame.image.load('{}setts_0.png'.format(way))
setts_1 = pygame.image.load('{}setts_1.png'.format(way))
setts_2 = pygame.image.load('{}setts_2.png'.format(way))

end_game_0 = pygame.image.load('{}end_game_0.png'.format(way))
end_game_1 = pygame.image.load('{}end_game_1.png'.format(way))
end_game_2 = pygame.image.load('{}end_game_2.png'.format(way))

RESTART = '1'
CONTINUE = '2'
SETTINGS = '3'
END_GAME = '4'

def pause_menu(setts):
    if setts[1]:
        screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(setts[0])
    pause_pict = pygame.image.load('storage/Pause_{0[0]}_{0[1]}.jpg'.format(setts[0])).convert()
    
    screen.blit(pause_pict, (0, 0))
    pygame.display.update()
    
    upgrade_buttons = True
    last_command = 0
    last_active = False      
    
    while True:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(music[0])
            pygame.mixer.music.play(10)   
            pygame.mixer.music.set_volume(setts[2])
            
        #------
        #UPDATING BUTTONS
        #------
        cursor = Point(pygame.mouse.get_pos()) 
        if upgrade_buttons:
            active = False
            
            if cursor.is_belong(Continue_game_button):
                screen.blit(cont_1, Continue_game_button.first())
                active = True
            else:
                screen.blit(cont_0, Continue_game_button.first())
                
            if cursor.is_belong(Restart_game_button):
                screen.blit(restart_1, Restart_game_button.first())
                active = True
            else:
                screen.blit(restart_0, Restart_game_button.first())     
                
            if cursor.is_belong(Settings_game_button):
                screen.blit(setts_1, Settings_game_button.first())
                active = True
            else:
                screen.blit(setts_0, Settings_game_button.first())   
                
            if cursor.is_belong(End_game_button):
                screen.blit(end_game_1, End_game_button.first())
                active = True
            else:
                screen.blit(end_game_0, End_game_button.first())             
                
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
            
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            return 1, setts           #same as continue button
            
        elif event.type == MOUSEBUTTONDOWN:
            cursor = Point(event.pos)
            upgrade_buttons = False            
            
            if cursor.is_belong(Continue_game_button):
                screen.blit(cont_2, Continue_game_button.first())
                last_command = CONTINUE               
                
            elif cursor.is_belong(Restart_game_button):
                screen.blit(restart_2, Restart_game_button.first())
                last_command = RESTART
            
            elif cursor.is_belong(Settings_game_button):
                screen.blit(setts_2, Settings_game_button.first())
                last_command = SETTINGS                
                
            elif cursor.is_belong(End_game_button):
                screen.blit(end_game_2, End_game_button.first())
                last_command = END_GAME 
            
            pygame.display.update()
                        
        elif event.type == MOUSEBUTTONUP:
                        
            if last_command == CONTINUE and cursor.is_belong(Continue_game_button):
                return 1, setts
                
            elif last_command == RESTART and cursor.is_belong(Restart_game_button):
                return 2, setts 
             
            elif last_command == SETTINGS and cursor.is_belong(Settings_game_button):
                setts = change_setts(setts)
                screen.blit(pause_pict, (0, 0))
                pygame.display.update()                    
                
            elif last_command == END_GAME and cursor.is_belong(End_game_button):
                return 0, setts         
            
            upgrade_buttons = True         