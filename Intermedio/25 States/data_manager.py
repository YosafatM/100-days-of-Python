import pandas

PATH = "missing_states.csv"
STATE = "state"
X = "x"
Y = "y"


class DataManager:
    def __init__(self, path: str = None):
        try:
            self.data = pandas.read_csv(path)
            self.data.set_index(STATE)
        except:
            print("Se necesita el path de los datos")

    def is_correct(self, answer: str):
        for i in range(0, len(self.data)):
            element = self.data[STATE].iloc[i]

            if element.lower() == answer.lower():
                x = self.data[X].iloc[i]
                y = self.data[Y].iloc[i]
                self.data = self.data[self.data[STATE] != element]

                return True, x, y, element

        return False, None

    def write_csv(self):
        self.data[STATE].to_csv(PATH)
