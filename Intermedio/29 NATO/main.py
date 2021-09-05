import pandas

PATH = "nato_phonetic_alphabet.csv"
MESSAGE = "Insert a word: "
ERROR = "Insert just alphabetical symbols, please"
K_LETTER = "letter"
K_CODE = "code"

data_frame = pandas.read_csv(PATH)
nato_dict = {row[K_LETTER]:row[K_CODE] for (index, row) in data_frame.iterrows()}

word = ""
while word.lower() != "exit":
    word = input(MESSAGE).upper()

    try:
        nato_list = [nato_dict[letter] for letter in word]
        print(nato_list)
    except KeyError:
        print(ERROR)
    finally:
        print()
