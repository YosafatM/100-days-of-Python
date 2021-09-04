from game_manager import GameManager
from data_manager import DataManager

data = DataManager("50_states.csv")
game = GameManager()

while game.is_playing():
    answer = game.ask_for_answer()

    if answer.lower() == "exit":
        data.write_csv()
        exit(0)

    data_result = data.is_correct(answer)

    if data_result[0]:
        game.score(xcor=data_result[1], ycor=data_result[2], state=data_result[3])

game.win_game()
