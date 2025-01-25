
import pygame as pg
import sys
import numpy as np

pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("The Game of Life")
clock = pg.time.Clock()
ww, wh = pg.display.get_surface().get_size()

rows, cols = ww // 5, wh // 5
running = True
vals = [0, 1]
grid = np.empty((rows, cols), dtype=int)

def drawgrid(grid):
    global rows, cols
    global ww, wh

    rcount = 0
    x, y = 0, 0
    rw, rl = ww // rows, wh // cols

    for i in grid:
        for j in i:
            x += rw
            rcount += 1
            if rcount == ww // rw:
                y += rl
                x = 0
                rcount = 0
            if j == 1:
                color = pg.Color("chartreuse4")
                pg.draw.rect(screen, color, (x , y, rw, rl))

def sim(grid):
    global rows, cols
    newgrid = np.empty((rows,cols), dtype=int) 
    N = rows

    for i in range(rows): 
        for j in range(cols): 

            state = int(grid[i, (j-1)%N] + 
                        grid[i, (j+1)%N] + 
                        grid[(i-1)%N, j] +
                        grid[(i+1)%N, j] + 
                        grid[(i-1)%N, (j-1)%N] +
                        grid[(i-1)%N, (j+1)%N] + 
                        grid[(i+1)%N, (j-1)%N] + 
                        grid[(i+1)%N, (j+1)%N]) 
            
            if grid[i, j] == 1:
                if (state < 2) or (state > 3):                     
                    newgrid[i, j] = 0
                elif (state == 2) or (state == 3):
                    newgrid[i, j] = 1

            elif grid[i, j] == 0:
                if (state == 3):
                    newgrid[i, j] = 1
                else:
                    newgrid[i, j] = 0
 
            
            state = 0

    grid[:] = newgrid[:]
    return grid

def main():
    global running
    global ww, wh
    global grid

    makeGrid = lambda grid : np.random.choice(vals, rows * cols, p=[.5, 0.5]).reshape(rows, cols)
    grid = makeGrid(grid)

    while running :
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False 
            elif event.type == pg.KEYDOWN and pg.K_q:
                    running = False
                    
        screen.fill("black")
        sim(grid)
        drawgrid(grid)
        pg.display.flip()
        clock.tick(30)

    pg.display.quit()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
