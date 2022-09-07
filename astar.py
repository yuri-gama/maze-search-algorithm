from queue import PriorityQueue
import pygame
import math


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
    # return abs(x1 - x2) + abs(y1 - y2)


def algorithm_bfs(draw, grid, start, end, save_img):
    stack = [start]
    start.score = 0
    save_img()
    while len(stack):

        current = stack.pop(0)

        if current == end:
            current.draw_path(draw, save_img)
            end.make_end()
            start.make_start()
            draw()
            save_img()
            print(current.score)
            return True

        for node in current.neighbors:
            if node not in stack and not node.visited:
                if node == start:
                    print('aq')
                node.score = current.score + 1
                stack.append(node)
                node.came_from = current
                node.make_open()

        current.make_visited()
        if current != start:
            current.make_closed()

        draw()
        save_img()

    return False


def algorithm(draw, grid, start, end, save_img):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    g_score = {node: float("inf") for row in grid for node in row}
    f_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            current.draw_path(draw, save_img)
            end.make_end()
            start.make_start()
            draw()
            save_img()
            print(g_score[end])
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                neighbor.came_from = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        save_img()

        if current != start:
            current.make_closed()

    return False
