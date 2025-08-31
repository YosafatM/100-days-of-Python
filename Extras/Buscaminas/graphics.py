import random

import pygame
import sys

from Extras.Buscaminas.board import Board
from Extras.Buscaminas.values import *


class Graphics:
    def __init__(self, width: int, height: int, board: Board):
        pygame.init()

        self.board = board
        self.width = width
        self.height = height
        self.button_states = [[False for _ in range(board.x_size)] for _ in range(board.y_size)]

        self.offset_top = 80
        self.cell_width = self.width // self.board.x_size
        self.cell_height = (self.height - self.offset_top) // self.board.y_size

        self.lose = False
        self.win = False

        self.is_hovering = False
        self.has_clicked = False
        self.is_welcoming = True
        self.counter_clock = 0

        # Pick random messages
        self.current_message = ""
        self.welcome_message_index = random.randint(0, len(MESSAGES_WELCOME) - 1)
        self.lose_message_index = random.randint(0, len(MESSAGES_LOSE) - 1)
        self.win_message_index = random.randint(0, len(MESSAGES_WIN) - 1)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()


    def _draw_top_message(self, font, message: str):
        label = font.render(message, True, BLACK)
        label_rect = label.get_rect(center=(self.width // 2, self.offset_top // 2))
        self.screen.blit(label, label_rect)


    def _draw_elements(self):
        self.screen.fill(LIGHTGRAY)
        font = pygame.font.SysFont("monospace", 20)

        # Draw messages
        if not self.lose and not self.win:
            if self.counter_clock == 0:
                if self.has_clicked:
                    self.current_message = MESSAGES_LUCK[pygame.time.get_ticks() // 2000 % len(MESSAGES_LUCK)]
                elif self.is_welcoming:
                    self.current_message = MESSAGES_WELCOME[self.welcome_message_index]
                else:
                    self.current_message = MESSAGES_NERVOUS[pygame.time.get_ticks() // 2000 % len(MESSAGES_NERVOUS)]
            else:
                self.counter_clock += 1
                if self.counter_clock > 15000:
                    self.counter_clock = 0
                    self.is_welcoming = False
                    self.has_clicked = False
        elif self.lose:
            self.current_message = MESSAGES_LOSE[self.lose_message_index]
        elif self.win:
            self.current_message = MESSAGES_WIN[self.win_message_index]

        self._draw_top_message(font,  self.current_message)

        # Draw minesweeper grid
        for y in range(self.board.y_size):
            for x in range(self.board.x_size):
                rect = pygame.Rect(x * self.cell_width,
                                   self.offset_top + y * self.cell_height,
                                   self.cell_width,
                                   self.cell_height)

                color = GRAY
                text = None

                if self.button_states[y][x]:
                    cell_value = self.board.get_cell(x, y)
                    text = str(cell_value)

                    if cell_value == -1:
                        color = RED
                        text = 'X'
                        self.lose = True
                    elif cell_value == 0:
                        color = GREEN
                    else:
                        color = WHITE

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)  # Border

                if text:
                    label = font.render(text, True, BLACK)
                    label_rect = label.get_rect(center=rect.center)
                    self.screen.blit(label, label_rect)


    def _event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.lose or self.win:
                    continue

                self.has_clicked = True
                coordinates = pygame.mouse.get_pos()
                x = coordinates[0] // self.cell_width
                y = (coordinates[1] - self.offset_top) // self.cell_height

                if 0 <= x < self.board.x_size and 0 <= y < self.board.y_size:
                    self.button_states[y][x] = True

                    if self.board.get_cell(x, y) == 0:
                        self._reveal_adjacent_cells(x, y)


    def _reveal_adjacent_cells(self, x: int, y: int) -> None:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                if 0 <= y + dy < self.board.y_size and 0 <= x + dx < self.board.x_size:
                    if not self.button_states[y + dy][x + dx]:
                        self.button_states[y + dy][x + dx] = True

                        if self.board.get_cell(x + dx, y + dy) == 0:
                            self._reveal_adjacent_cells(x + dx, y + dy)


    def _check_if_player_won(self) -> bool:
        for y in range(self.board.y_size):
            for x in range(self.board.x_size):
                if not self.button_states[y][x] and self.board.get_cell(x, y) != -1:
                    return False
        return True


    def main_loop(self):
        while True:
            self._event_handler()
            self._draw_elements()

            self.win = self._check_if_player_won()

            pygame.display.flip()
            self.clock.tick(60)