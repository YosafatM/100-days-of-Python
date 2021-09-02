#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as handle:
    card = handle.read()

names = []
with open("./Input/Names/invited_names.txt") as handle:
    for line in handle.readlines():
        names.append(line.replace("\n", ""))

for name in names:
    new_card = card.replace("[name]", name)

    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as handle:
        handle.write(new_card)
