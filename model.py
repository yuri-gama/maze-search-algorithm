from settings import *
import pygame


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = CREATE_COLOR
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == CLOSED_COLOR

    def is_open(self):
        return self.color == OPEN_COLOR

    def is_barrier(self):
        return self.color == BARRIER_COLOR

    def is_start(self):
        return self.color == START_COLOR

    def is_end(self):
        return self.color == END_COLOR

    def reset(self):
        self.color = WHITE

    def make_open(self):
        self.color = OPEN_COLOR

    def make_closed(self):
        self.color = CLOSED_COLOR

    def make_barrier(self):
        self.color = BARRIER_COLOR

    def make_end(self):
        self.color = END_COLOR

    def make_start(self):
        self.color = START_COLOR

    def make_path(self):
        self.color = PATH_COLOR

    def make_start(self):
        self.color = START_COLOR

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
