import random


def main():
    def hangman(word):
        wrong = 0
        stages = ["",
                  "_________         ",
                  "|                 ",
                  "|        |        ",
                  "|        0        ",
                  "|       /|\       ",
                  "|       / \       ",
                  "|                 "
                  ]
        rletters = list(word)
        board = ["_"] * len(word)
        win = False
        print("Welcome to Hangman")

        while wrong < len(stages) - 1:
            print("\n")
            guess = "Guess a letter: "
            char = input(guess)
            if char in rletters:
                index = rletters.index(char)
                board[index] = char
                rletters[index] = "$"
            else:
                wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0: e]))
            if "_" not in board:
                print("You win!")
                print(" ".join(board))
                win = True
                break
        if not win:
            print("\n".join((stages[0: wrong])))
            print(f"You lose! It was: {word}")

    words = ['penis', 'ayanah', 'mango', 'chocolate', 'bird', 'summer', 'worm']
    i = random.randint(0, 6)
    hangman(words[i])


main()
