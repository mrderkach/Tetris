WIDTH, HEIGHT = 15, 28
SQUARE_SIZE = 20
NFIELD_CELLS = 12                        #cells before the field
#Figures in 4x4 square
figures = [[[0, 1], [0, 2], [1, 2], [1, 1], (30, 144, 255)],               # O
           [[0, 0], [0, 1], [0, 2], [0, 3], (255, 0, 0)],                # I
           [[0, 1], [0, 2], [0, 3], [1, 3], (0, 255, 255)],                # L
           [[0, 1], [0, 2], [0, 3], [1, 1], (60, 170, 60)],                # L-2
           [[0, 1], [0, 2], [1, 2], [1, 3], (127, 255, 119)],              # Z
           [[1, 1], [1, 2], [0, 2], [0, 3], (253, 233, 16)],                # Z-2
           [[0, 1], [0, 2], [0, 3], [1, 2], (255, 153, 0)]]              # T

nspeed = 250                            #speed of passive falling
dspeed = 35                             #increase speed per 10 figures
bgcolor = (245, 245, 220)                #color of way of figure and of the field under them
title = 'TETRIS @Denis'
speed_lvl = [10, 10, 15, 25, 50, 50]     #250, 215, 180, 145, 110, 80

#giving figures normal coordinates
for current in range(len(figures)):
    for cell in range(len(figures[current]) - 1):
        figures[current][cell][1] += NFIELD_CELLS + WIDTH // 2 - 2