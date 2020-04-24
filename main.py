import pygame
import config
from cell import Cell
pygame.init()

screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption('Maze Generator')
clock = pygame.time.Clock()

grid = []

# Initialize cells
for j in range(config.rows):
    for i in range(config.cols):
        grid.append(Cell(i, j))


current = grid[0]
stack = []


def recursive_backtracker():
    global current, stack
    current.visited = True
    neighbour = current.check_neighbours(grid)
    if neighbour != None:
        stack.append(current)
        current.remove_walls(neighbour)
        current = neighbour
    elif len(stack) > 0:
        current = stack.pop()


def redraw_window():
    screen.fill((51, 51, 51))

    for cell in grid:
        cell.show(screen)

    current.highlight(screen)
    recursive_backtracker()

    pygame.display.update()


# mainloop
run = True
while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redraw_window()

pygame.quit()
