import sys, pygame
from pygame.locals import *

from bin import *
from bin.geom import *
from bin.play import *
from bin.GO_menu import *
from bin.instructions import *
from bin.new_record import *
from bin.settings import *
from bin.pause import *

from parametres import *
from parametres.buttons import *
from parametres.settings import *
from parametres.game_setts import *
from parametres.highscores import *

pygame.init()
pygame.display.set_caption(title)
setts = [screen_resolution, full_screen, music_volume]

if setts[1]:
    screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(setts[0])

#------
#Loading music and pictures
#------

music = ['music/music1.mp3']
way = 'storage/Buttons/'

main_menu = pygame.image.load('storage/Main_menu_{0[0]}_{0[1]}.jpg'.format(setts[0])).convert()
play_0 = pygame.image.load('{}Play_0.png'.format(way))
play_1 = pygame.image.load('{}Play_1.png'.format(way))
play_2 = pygame.image.load('{}Play_2.png'.format(way))

instruct_0 = pygame.image.load('{}instruct_0.png'.format(way))
instruct_1 = pygame.image.load('{}instruct_1.png'.format(way))
instruct_2 = pygame.image.load('{}instruct_2.png'.format(way))

highsc_0 = pygame.image.load('{}highsc_0.png'.format(way))
highsc_1 = pygame.image.load('{}highsc_1.png'.format(way))
highsc_2 = pygame.image.load('{}highsc_2.png'.format(way))

setts_0 = pygame.image.load('{}setts_0.png'.format(way))
setts_1 = pygame.image.load('{}setts_1.png'.format(way))
setts_2 = pygame.image.load('{}setts_2.png'.format(way))

exit_0 = pygame.image.load('{}exit_0.png'.format(way))
exit_1 = pygame.image.load('{}exit_1.png'.format(way))
exit_2 = pygame.image.load('{}exit_2.png'.format(way))

PLAY = '1'
HIGHSCORES = '2'
SETTINGS = '3'
EXIT = '4'
INSTRUCTIONS = '5'

#------
#Starting menu
#------

highscore_table = highscores
my_event = 2
upgrade_buttons = True
last_command = 0
last_active = False


while True:
    if my_event == 1:                  
        
        #Exit of GO_menu with the restart button
        score, mode, setts = game(setts)
        if mode == 0:
            if score > min(highscores)[0]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/record.mp3')
                pygame.mixer.music.play(0)
                highscore_table = set_new_record(score, highscore_table, setts)       
            my_event = game_over_menu(score, highscore_table, setts)
        else:
            my_event = 1
        continue
            
    elif my_event == 2:           
        
        #Exit of some menu. It needs to refresh main menu 
        screen.blit(main_menu, (0, 0))
        pygame.display.update()   
        my_event = 0
        
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
        if cursor.is_belong(Start_button):
            screen.blit(play_1, Start_button.first())
            active = True
        else:
            screen.blit(play_0, Start_button.first())
            
        if cursor.is_belong(Instructions_button):
            screen.blit(instruct_1, Instructions_button.first())
            active = True
        else:
            screen.blit(instruct_0, Instructions_button.first())     
            
        if cursor.is_belong(Highscores_button_menu):
            screen.blit(highsc_1, Highscores_button_menu.first())
            active = True
        else:
            screen.blit(highsc_0, Highscores_button_menu.first())   
            
        if cursor.is_belong(Settings_button):
            screen.blit(setts_1, Settings_button.first())
            active = True
        else:
            screen.blit(setts_0, Settings_button.first())
            
        if cursor.is_belong(Quit_button):
            screen.blit(exit_1, Quit_button.first())
            active = True
        else:
            screen.blit(exit_0, Quit_button.first())          
    
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
        
        upgrade_buttons = False
        
        if cursor.is_belong(Start_button):
            screen.blit(play_2, Start_button.first())
            last_command = PLAY
            
        elif cursor.is_belong(Instructions_button):
            screen.blit(instruct_2, Instructions_button.first()) 
            last_command = INSTRUCTIONS        
        
        elif cursor.is_belong(Highscores_button_menu):
            screen.blit(highsc_2, Highscores_button_menu.first()) 
            last_command = HIGHSCORES           
            
        elif cursor.is_belong(Settings_button):
            screen.blit(setts_2, Settings_button.first()) 
            last_command = SETTINGS
                        
        elif cursor.is_belong(Quit_button):
            screen.blit(exit_2, Quit_button.first()) 
            last_command = EXIT       
            
        pygame.display.update()
        
    elif event.type == MOUSEBUTTONUP:
            
        if last_command == PLAY and cursor.is_belong(Start_button):
            score, mode, setts = game(setts)
            if mode == 0:
                if score > min(highscores)[0]:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('music/record.mp3')
                    pygame.mixer.music.play(0)
                    highscore_table = set_new_record(score, highscore_table, setts)
                my_event = game_over_menu(score, highscore_table, setts)
            else:
                my_event = 1 
                
        elif last_command == INSTRUCTIONS and cursor.is_belong(Instructions_button):
            my_event = show_instructions(setts)
            
        elif last_command == HIGHSCORES and cursor.is_belong(Highscores_button_menu):
            my_event = show_scoretable(highscore_table, setts)   
            
        elif last_command == SETTINGS and cursor.is_belong(Settings_button):
            setts = change_setts(setts)
            my_event = 2 
            
        elif last_command == EXIT and cursor.is_belong(Quit_button):
            pygame.quit()
            sys.exit()            
        
        upgrade_buttons = True   