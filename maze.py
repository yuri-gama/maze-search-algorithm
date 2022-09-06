from model import *
from astar import *
import load_map


def draw_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for row in range(rows):
        grid.append([])
        for col in range(rows):
            node = Node(row, col, gap, rows)
            grid[row].append(node)

    return grid


def draw_grid(window, rows, width):
    gap = width // rows
    for row in range(rows):
        pygame.draw.line(window, GREY, (0, row * gap), (width, row * gap))
        for col in range(rows):
            pygame.draw.line(window, GREY, (col * gap, 0), (col * gap, width))


def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()


def get_clicked_position(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap

    print((row, col))
    return row, col


def clear(rows, width):
    grid = make_grid(rows, width)

    start = None
    end = None

    run = True
    started = False

    return grid, start, end, run, started


def main(window, rows, width):
    grid, start, end, run, started = clear(rows, width)

    while run:
        draw(window, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:
                print('-')
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, rows, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, rows, width)
                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None
                if node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start is not None and end is not None:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    algorithm(lambda: draw(window, grid, rows, width), grid, start, end, draw_path)

                if event.key == pygame.K_l:
                    start, end = load_map.project01(grid)

                if event.key == pygame.K_c:
                    grid, start, end, run, started = clear(rows, width)

    pygame.quit()
