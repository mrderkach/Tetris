# Displaying instructions menu


import pygame, sys
from pygame.locals import *

from bin import geom
from bin.geom import *

from parametres import buttons
from parametres.buttons import *

pygame.init()
instruct_1 = pygame.image.load('storage/Instruction_1.jpg')
instruct_2 = pygame.image.load('storage/Instruction_2.jpg')
n = 2

#------
#Loading music and pictures
#------
music = ['music/music1.mp3']
way = 'storage/Buttons/'

next_p_0 = pygame.image.load('{}next_p_0.png'.format(way))
next_p_1 = pygame.image.load('{}next_p_1.png'.format(way))
next_p_2 = pygame.image.load('{}next_p_2.png'.format(way))

prev_p_0 = pygame.image.load('{}prev_p_0.png'.format(way))
prev_p_1 = pygame.image.load('{}prev_p_1.png'.format(way))
prev_p_2 = pygame.image.load('{}prev_p_2.png'.format(way))

menu_0 = pygame.image.load('{}menu_0.png'.format(way))
menu_1 = pygame.image.load('{}menu_1.png'.format(way))
menu_2 = pygame.image.load('{}menu_2.png'.format(way))

NEXT_PAGE = '1'
PREV_PAGE = '2'
MENU = '3'

def show_instructions(setts):
    if setts[1]:
        screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(setts[0])
        
    page = 1
    refresh = True            #means, that we need to refresh page
    upgrade_buttons = True
    last_command = 0
    last_active = False    

    while 1:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(music[0])
            pygame.mixer.music.play(10)          

        # Show instructions based on the number of page
        if refresh:
            if page == 1:
                screen.blit(instruct_1, (0, 0))
                pygame.display.update()  
                refresh = False
            else:
                screen.blit(instruct_2, (0, 0))
                pygame.display.update()  
                refresh = False
                
        #------
        #UPDATING BUTTONS
        #------
        cursor = Point(pygame.mouse.get_pos()) 
        if upgrade_buttons:
            active = False
            
            if page != n:
                if cursor.is_belong(Next_page):
                    screen.blit(next_p_1, Next_page.first())
                    active = True
                else:
                    screen.blit(next_p_0, Next_page.first())
                
            if page != 1:
                if cursor.is_belong(Prev_page):
                    screen.blit(prev_p_1, Prev_page.first())
                    active = True
                else:
                    screen.blit(prev_p_0, Prev_page.first())     
                
            if cursor.is_belong(Main_menu):
                screen.blit(menu_1, Main_menu.first())
                active = True
            else:
                screen.blit(menu_0, Main_menu.first())   
                
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
            
            if cursor.is_belong(Next_page) and page != n:
                screen.blit(next_p_2, Next_page.first())
                last_command = NEXT_PAGE               
                
            elif cursor.is_belong(Prev_page) and page != 1:
                screen.blit(prev_p_2, Prev_page.first())
                last_command = PREV_PAGE               
                
            elif cursor.is_belong(Main_menu):
                screen.blit(menu_2, Main_menu.first())
                last_command = MENU   
                
            pygame.display.update()
            
        elif event.type == MOUSEBUTTONUP:
                        
            if last_command == NEXT_PAGE and cursor.is_belong(Next_page):
                if page != n:
                    page += 1
                    refresh = True 
                
            elif last_command == PREV_PAGE and cursor.is_belong(Prev_page):
                if page != 1:
                    page -= 1
                    refresh = True 
                
            elif last_command == MENU and cursor.is_belong(Main_menu):
                return 2            
            
            upgrade_buttons = True        