import pygame
import random
import config


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        # Top Right Bottom Left
        self.walls = [True, True, True, True]
        self.visited = False

    def show(self, screen):
        x = self.i * config.w
        y = self.j * config.w

        if self.walls[0]:
            pygame.draw.line(screen, (255, 255, 255),
                             (x, y), (x + config.w, y))
        else:
            pygame.draw.line(screen, (0, 0, 0),
                             (x, y), (x + config.w, y))

        if self.walls[1]:
            pygame.draw.line(screen, (255, 255, 255),
                             (x + config.w, y), (x + config.w, y + config.w))
        else:
            pygame.draw.line(screen, (0, 0, 0),
                             (x + config.w, y), (x + config.w, y + config.w))

        if self.walls[2]:
            pygame.draw.line(screen, (255, 255, 255),
                             (x + config.w, y + config.w), (x, y + config.w))
        else:
            pygame.draw.line(screen, (0, 0, 0),
                             (x + config.w, y + config.w), (x, y + config.w))

        if self.walls[3]:
            pygame.draw.line(screen, (255, 255, 255),
                             (x, y + config.w), (x, y))
        else:
            pygame.draw.line(screen, (0, 0, 0),
                             (x, y + config.w), (x, y))

        if self.visited:
            pygame.draw.rect(screen, (0, 0, 0),
                             (x + 1, y + 1, config.w - 1, config.w - 1))

    def highlight(self, screen):
        x = self.i * config.w
        y = self.j * config.w

        s = pygame.Surface((config.w - 1, config.w - 1))
        s.set_alpha(150)        # 255 full fill
        s.fill((255, 165, 0))
        screen.blit(s, (x + 1, y + 1))

    def check_neighbours(self, grid):
        neighbours = []

        top = config.index(self.i, self.j-1)
        right = config.index(self.i+1, self.j)
        bottom = config.index(self.i, self.j+1)
        left = config.index(self.i-1, self.j)

        if top != None and not grid[top].visited:
            neighbours.append(grid[top])
        if right != None and not grid[right].visited:
            neighbours.append(grid[right])
        if bottom != None and not grid[bottom].visited:
            neighbours.append(grid[bottom])
        if left != None and not grid[left].visited:
            neighbours.append(grid[left])

        if len(neighbours) > 0:
            return neighbours[random.randint(0, len(neighbours)-1)]
        return None

    def remove_walls(self, neighbour):
        x = self.i - neighbour.i
        # Right
        if x == -1:
            self.walls[1] = False
            neighbour.walls[3] = False
        # Left
        elif x == 1:
            self.walls[3] = False
            neighbour.walls[1] = False

        y = self.j - neighbour.j
        # Bottom
        if y == -1:
            self.walls[2] = False
            neighbour.walls[0] = False
        # Top
        elif y == 1:
            self.walls[0] = False
            neighbour.walls[2] = False
