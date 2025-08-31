from Extras.Buscaminas.board import Board
from Extras.Buscaminas.graphics import Graphics

if __name__ == "__main__":
    board = Board(10, 10, 0.20, 20)
    graphics = Graphics(600, 800, board)
    graphics.main_loop()