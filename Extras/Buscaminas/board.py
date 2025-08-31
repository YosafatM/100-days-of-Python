import random

class Board:
    def __init__(self, x_size: int, y_size: int, probability=0.15, max_num_mines=15):
        self.x_size = x_size
        self.y_size = y_size
        self.probability = probability
        self.max_num_mines = max_num_mines

        self.num_mines = 0

        self.board = [[0 for _ in range(x_size)] for _ in range(y_size)]
        self._generate_mines()


    def _generate_mines(self) -> None:
        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.num_mines >= self.max_num_mines:
                    return

                if random.random() < self.probability:
                    self.board[y][x] = -1
                    self._increment_adjacent_cells(x, y)
                    self.num_mines += 1


    def _increment_adjacent_cells(self, x: int, y: int) -> None:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                # Check bounds
                if 0 <= y + dy < self.y_size and 0 <= x + dx < self.x_size:
                    # Don't increment the mine cell itself u other mines
                    if self.board[y + dy][x + dx] != -1:
                        self.board[y + dy][x + dx] += 1


    def get_cell(self, x: int, y: int) -> int:
        if 0 <= x < self.x_size and 0 <= y < self.y_size:
            return self.board[y][x]
        else:
            raise IndexError("Cell coordinates out of bounds")