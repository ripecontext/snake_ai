import pygame
import time
import random
from snake import Snake


def Main():

    window_size = 400
    board_size = 40
    scale = window_size / board_size

    window = pygame.display.set_mode([window_size, window_size])

    snake = Snake([3, 3], board_size)

    food_position = [random.randint(0, board_size - 1), random.randint(0, board_size - 1)]

    running = True
    while running:

        has_eaten = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    snake.direction = 0
                elif keys[pygame.K_RIGHT]:
                    snake.direction = 1
                elif keys[pygame.K_DOWN]:
                    snake.direction = 2
                elif keys[pygame.K_LEFT]:
                    snake.direction = 3

        window.fill((0, 0, 0))

        while food_position in snake.body:
            food_position = [random.randint(0, board_size - 1), random.randint(0, board_size - 1)]
            has_eaten = True

        snake.direction = snake.decideDirection(food_position)

        snake.show(window, scale, food_position)
        running = not snake.move(has_eaten) and running

        pygame.display.flip()
        time.sleep(0.05)


if __name__ == "__main__":
    Main()