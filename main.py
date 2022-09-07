from maze import *
import os

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")

if not os.path.exists('img'):
    os.makedirs('img')
main(WIN, ROWS, WIDTH)
os.rmdir('img')
