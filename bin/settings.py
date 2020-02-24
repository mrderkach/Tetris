# Settings menu

import pygame, sys, math
from pygame.locals import *

from bin import *
from bin.geom import *

from parametres import buttons
from parametres.buttons import *

pygame.init()
tick_pos = (570, 215)

#------
#Loading music and pictures
#------
music = ['music/music1.mp3']
way = 'storage/Buttons/'

back_0 = pygame.image.load('{}back_0.png'.format(way))
back_1 = pygame.image.load('{}back_1.png'.format(way))
back_2 = pygame.image.load('{}back_2.png'.format(way))

BACK = '1'

def save_n_quit(scr_resolution, fullscr, mus_volume):
    f = open('parametres/settings.py', 'w')
    setts = [scr_resolution, fullscr, mus_volume]
    f.write('''
screen_resolution = {0[0]}
full_screen = {0[1]}
music_volume = {0[2]}                          # 0 ... 1 set music volume
'''.format(setts))
    return setts

def change_setts(setts):
    if setts[1]:
        screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(setts[0])
    scr_resolution, fullscr, mus_volume = setts
    pos_mus = (526 + int(mus_volume * 200), 295)
    moving = False
    change_mus = False
    
    settings_menu = pygame.image.load('storage/settings_{0[0]}_{0[1]}.jpg'.format(setts[0])).convert()
    cursor_mus = pygame.image.load('storage/cursor_mus.jpg').convert()
    tick = pygame.image.load('storage/tick.jpg').convert() 
    
    upgrade_buttons = True
    last_command = 0
    last_active = False    
    
    screen.blit(settings_menu, (0, 0))
    screen.blit(cursor_mus, pos_mus)
    if fullscr:
        screen.blit(tick, tick_pos)
    pygame.display.update() 
    while True:
        if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load(music[0])
                    pygame.mixer.music.play(10)   
                    pygame.mixer.music.set_volume(mus_volume)   
                    
        #------
        #UPDATING BUTTONS
        #------
        cursor = Point(pygame.mouse.get_pos()) 
        if upgrade_buttons:
            active = False
            
            if cursor.is_belong(Quit_button) and not moving:
                screen.blit(back_1, Quit_button.first())
                active = True
            else:
                screen.blit(back_0, Quit_button.first())          
        
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
            save_n_quit(scr_resolution, fullscr, mus_volume)
            exit()  
                    
        elif event.type == MOUSEBUTTONDOWN:
            cursor = Point(event.pos)
            
            if cursor.is_belong(Quit_button):
                screen.blit(back_2, Quit_button.first()) 
                last_command = BACK  
                upgrade_buttons = False
                
            #Cursor at cursor of music Trackbar
            elif cursor.is_belong(Polygon([Point(pos_mus), Point(pos_mus[0], pos_mus[1] + 30), Point(pos_mus[0] + 13, pos_mus[1] + 30), Point(pos_mus[0] + 13, pos_mus[1])])):
                moving = True
                
            #cursor at fullscreen tick
            elif cursor.is_belong(Polygon([Point(573, 221), Point(573, 258), Point(609, 258), Point(609, 221)])):
                if not fullscr:
                    fullscr = 1
                    screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
                else:
                    fullscr = 0
                    screen = pygame.display.set_mode(setts[0])  
                screen.blit(settings_menu, (0, 0))
                screen.blit(cursor_mus, pos_mus)  
                if fullscr:
                    screen.blit(tick, tick_pos)                
                pygame.display.update()
                    
        elif event.type == MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if moving or (y >= 305 and y <= 315 and x >= 526 and x <= 726):
                change_mus = True
                moving = False
                
            elif last_command == BACK and cursor.is_belong(Quit_button):
                return save_n_quit(scr_resolution, fullscr, mus_volume)   
            
            upgrade_buttons = True
                
        if moving or change_mus:
            x, y = pygame.mouse.get_pos()
            if x < 526:
                x = 526
            if x > 714:
                x = 714
            screen.blit(settings_menu, (0, 0))
            screen.blit(cursor_mus, (x, 295))
            screen.blit(back_0, Quit_button.first())
            if fullscr:
                screen.blit(tick, tick_pos)            
            pos_mus = (x, 295)
            mus_volume = (pos_mus[0] - 526) / 188
            pygame.mixer.music.set_volume(mus_volume)  
            change_mus = False
        pygame.display.update()