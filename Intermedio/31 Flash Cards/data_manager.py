import pandas as pd
import random as rd

ORIGINAL_PATH = "./data/french_words.csv"
SAVE_PATH = "./data/words_to_learn.cvs"
COLUMN_FRENCH = "French"
COLUMN_ENGLISH = "English"


class DataManager:
    def __init__(self):
        try:
            self.data = pd.read_csv(SAVE_PATH)
        except FileNotFoundError:
            self.data = pd.read_csv(ORIGINAL_PATH)
        finally:
            self.end = self.data[COLUMN_FRENCH].count()

    def get_pair(self):
        if self.end == 0:
            return Pair("Tout est terminé", "All completed")

        row = self.data.iloc[rd.randint(0, self.end - 1)]
        self.end -= 1
        return Pair(row[COLUMN_FRENCH], row[COLUMN_ENGLISH])

    def remove_pair(self, pair):
        self.data = self.data[self.data[COLUMN_FRENCH] != pair.question]

    def save_pairs(self):
        self.data.to_csv(SAVE_PATH, index=False)


class Pair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    @staticmethod
    def get_question_title():
        return COLUMN_FRENCH

    @staticmethod
    def get_answer_title():
        return COLUMN_ENGLISH
