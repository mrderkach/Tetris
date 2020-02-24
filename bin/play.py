# Displays the window where all the game happens.
# Describes game logic.

import copy, sys, random, pygame, time
from pygame.locals import *

from bin import *
from bin.pause import *

from parametres import game_setts
from parametres.game_setts import *

pygame.init()

# Draw Background
def draw(screen, cell, color, sq_size = SQUARE_SIZE):
    screen.fill(color, (cell[1] * sq_size, cell[0] * sq_size, sq_size, sq_size))

# Draw figure on the game screen
def draw_figure(screen, figure, color = (0, 0, 0)):
    for cell in figure:
        draw(screen, cell, color)

# Draw figure in the "next" section
def draw_next(screen, next_figure_pict, figure, color):
    screen.blit(next_figure_pict, (600, 0))
    i = 0
    for cell in figure:
        draw(screen, (cell[0] + 1, cell[1] + 3.8), color, 10 + SQUARE_SIZE)
        i += 1
    pygame.display.update()
music = ['music/music2.mp3', 'music/music3.mp3']

def game(setts):
    # Load settings
    if setts[1]:
        screen = pygame.display.set_mode(setts[0], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(setts[0])    
    score_pict = pygame.image.load('storage/Score.jpg').convert()
    next_figure_pict = pygame.image.load('storage/Next_figure.jpg').convert() 
    game_play = pygame.image.load('storage/Game_{0[0]}_{0[1]}.jpg'.format(setts[0])).convert()

    screen.blit(game_play, (0, 0))
    falled_figures = 0
    score = 0
    quit = 0
    k = 0
    field = [[False] * (setts[0][0] // SQUARE_SIZE) for i in range(setts[0][1] // SQUARE_SIZE)]
    future = copy.deepcopy(random.choice(figures))   
#    future = copy.deepcopy(figures[1])
    speed = nspeed
    playback = random.choice([0, 1])
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music[playback])
    pygame.mixer.music.play(0) 
    
    pygame.time.set_timer(KEYDOWN, speed)
    
    while True:
        current = copy.deepcopy(future)
        future = copy.deepcopy(random.choice(figures))
#        future = copy.deepcopy(figures[1])
        
        # Check if figures have reached the end of screen
        for cell in current[:-1]:
            if field[cell[0]][cell[1] - NFIELD_CELLS + 1]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/death.mp3')
                pygame.mixer.music.play(0)
                time.sleep(3)
                return score, 0, setts
        
        figure_falling = 1
        draw_figure(screen, current[:-1], current[-1])
        draw_next(screen, next_figure_pict, future[:-1], future[-1])
        pygame.display.update()        
        
        
        #__________________________________________
        #Now current figure is falling
        #__________________________________________
        
        
        
        while True:
            event = pygame.event.wait()
            if not pygame.mixer.music.get_busy():
                playback += 1
                playback %= 2
                pygame.mixer.music.load(music[playback])
                pygame.mixer.music.play(0)     
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYDOWN and event.key == K_ESCAPE:           
                my_event, setts = pause_menu(setts)
                if my_event == 0:                 #end game
                    return score, 0, setts
                elif my_event == 1:               #continue
                    screen.blit(game_play, (0, 0))
                    for i in range(len(field)):
                        for j in range(len(field[i])):
                            if field[i][j]:
                                draw(screen, (i, NFIELD_CELLS + j), field[i][j])
                    draw_figure(screen, current[:-1], current[-1])
                    draw_next(screen, next_figure_pict, future[:-1], future[-1])
                    font = pygame.font.Font(None,40)
                    text = font.render(str(score), 1, (255, 0, 0)) 
                    screen.blit(text, (700, 137))                    
                    pygame.display.update()
                elif my_event == 2:               #restart
                    return 0, 1, setts
                
            elif event.type == KEYDOWN and event.key == K_UNKNOWN:
                for cell in current[:-1]:
                    if cell[0] + 1 >= HEIGHT or field[cell[0] + 1][cell[1] - NFIELD_CELLS]:
                        for cell in current[:-1]:
                            field[cell[0]][cell[1] - NFIELD_CELLS] = current[-1]
                        figure_falling = 0
                        break
                else:
                    draw_figure(screen, current[:-1], bgcolor)
                    for cell in current[:-1]:
                        cell[0] += 1
                    draw_figure(screen, current[:-1], current[-1])
                    pygame.display.update()
                    
            elif event.type == KEYDOWN and event.key == K_LEFT:
                for cell in current[:-1]:
                    if cell[1] - 1 < 0 + NFIELD_CELLS or field[cell[0]][cell[1]  - NFIELD_CELLS - 1]:
                        break
                else:
                    draw_figure(screen, current[:-1], bgcolor)
                    for cell in current[:-1]:
                        cell[1] -= 1
                    draw_figure(screen, current[:-1], current[-1])
                    pygame.display.update()
    
            elif event.type == KEYDOWN and event.key == K_UP:
                center_x = int(sum([cell[0] + 0.5 for cell in current[:-1]]) / len(current[:-1]) + 0.5)
                center_y = int(sum([cell[1] + 0.5 for cell in current[:-1]]) / len(current[:-1]) + 0.5)
                new_figure = [[center_x + center_y - y - 1, x - center_x + center_y] for x, y in current[:-1]] + [current[-1]]
                for x, y in new_figure[:-1]:
                    if not (0 + NFIELD_CELLS <= y < NFIELD_CELLS + WIDTH and 0 <= x < HEIGHT) or field[x][y  - NFIELD_CELLS]:
                        break
                else:
                    draw_figure(screen, current[:-1], bgcolor)
                    current = new_figure
                    draw_figure(screen, current[:-1], current[-1])
                    pygame.display.update()
          
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                for cell in current[:-1]:
                    if cell[1] + 1 >= NFIELD_CELLS + WIDTH or field[cell[0]][cell[1] - NFIELD_CELLS + 1]:
                        break
                else:
                    draw_figure(screen, current[:-1], bgcolor)
                    for cell in current[:-1]:
                        cell[1] += 1
                    draw_figure(screen, current[:-1], current[-1])
                    pygame.display.update()
                    
            elif event.type == KEYDOWN and event.key == K_SPACE:
                pygame.time.set_timer(KEYDOWN, 40)
                
            elif event.type == KEYDOWN and event.key == K_DOWN:
                pygame.time.set_timer(KEYDOWN, 55)
                
            elif event.type == KEYUP and event.key == K_DOWN:
                pygame.time.set_timer(KEYDOWN, speed)        
                
            #____________________________________
            #AFTER-MOVING works
            
            del_lines = 0
            line = HEIGHT - 1
            while line != 1:
                for cell in range(NFIELD_CELLS, NFIELD_CELLS + WIDTH):
                    if not field[line][cell - NFIELD_CELLS]:
                        break
                else:
                    del_lines += 1
                    for line1 in range(line, 0, -1):
                        for cell in range(NFIELD_CELLS, NFIELD_CELLS + WIDTH):
                            draw(screen, (line1, cell), bgcolor)
                            field[line1][cell - NFIELD_CELLS] = field[line1 - 1][cell - NFIELD_CELLS]
                            if field[line1][cell - NFIELD_CELLS]:
                                draw(screen, (line1, cell), field[line1][cell - NFIELD_CELLS])
                    pygame.display.update()

                    field[0] = [False for i in range(WIDTH)]
                    line += 1
                line -= 1
                
            if del_lines != 0:
                if del_lines == 1:
                    score += 10
                elif del_lines == 2:
                    score += 25
                elif del_lines == 3:
                    score += 40
                else:
                    score += 60
            screen.blit(score_pict, (600, 130))
            font = pygame.font.Font(None, 40)
            text = font.render(str(score), 1, (255, 0, 0)) 
            screen.blit(text, (700, 137))

            pygame.display.update()
            
            if not figure_falling:
                break
        #Current figure falled
        
        if speed > 40:
            falled_figures += 1
            if k >= len(speed_lvl):
                speed -= dspeed * (falled_figures // 20)
                falled_figures %= 20         
            else:
                speed -= dspeed * (falled_figures // speed_lvl[k])
                falled_figures, k = (falled_figures % speed_lvl[k]), (k + falled_figures // speed_lvl[k])
            if speed <= 80:
                speed = 80
        pygame.time.set_timer(KEYDOWN, speed)