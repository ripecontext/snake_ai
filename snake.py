import pygame


class Snake:

    def __init__(self, position, board_size):

        self.body = [[position[0]-1, position[1]], position]
        self.board_size = board_size

        self.direction = 1

    def show(self, window, scale, food_position):

        pygame.draw.rect(window, (255, 0, 0), (food_position[0] * scale, food_position[1] * scale, scale, scale))

        for piece in self.body:

            pygame.draw.rect(window, (0, 255, 0), (piece[0] * scale, piece[1] * scale, scale, scale))

    def move(self, has_eaten):

        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

        self.body.append([self.body[-1][0] + directions[self.direction][0],
                          self.body[-1][1] + directions[self.direction][1]])

        dead = self.isDead()

        if not has_eaten:

            self.body.remove(self.body[0])

        return dead

    def isDead(self):

        if self.body[-1] in self.body[:-1]:
            return True

        elif not (0 <= self.body[-1][0] < self.board_size and 0 <= self.body[-1][1] < self.board_size):
            return True

        return False

    def decideDirection(self, food_pos):

        checks = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        cost = [0, 0, 0, 0]

        for check in range(4):

            new_head_pos = [self.body[-1][0] + checks[check][0],
                            self.body[-1][1] + checks[check][1]]

            manhattan_distance_to_food = abs(new_head_pos[0] - food_pos[0]) + abs(new_head_pos[1] - food_pos[1])
            if (new_head_pos in self.body
                    or not (0 <= self.body[-1][0] < self.board_size and 0 <= self.body[-1][1] < self.board_size)):
                cost[check] += 1000

            cost[check] += manhattan_distance_to_food

        return cost.index(min(cost))
