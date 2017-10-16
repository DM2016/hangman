#chr 10, hangman game
def hangman(word):  #define your module
    wrong = 0  #stores and keeps track of # of wrong guesses, start off with 0 wrong answers
    stages = ["",
              "___________           ",  #hangman figure
              "|                     ",
              "|          |          ",
              "|          0          ",
              "|         /|\         ",
              "|         / \         ",
              "|                     ",
              ]
    rletters = list(word) #variable that contains list that holds each character in the variable word
    board = ["_"] * len(word)  #list of strings used to keep track of the hints given to player 2
    win = False  #start 
    print("Welcome to Hangman!")
    while wrong < len(stages) - 1:  #controls how many chances player 2 has to guess
        print("\n")
        msg = "Guess a letter.\n"  #message to input a letter to guess
        char = input(msg) 
        if char in rletters:  #updates board list
            cind = rletters.index(char) #uses index get first index of the letter that player two guessed
            board[cind] = char
            rletters[cind] = '$'  #returns the indexes after the first index, finds all occurances of a correctly guessed letter
        else:
            wrong += 1  #increments wrong guesses
        print((" ".join(board)))
        e  = wrong + 1
        print("\n".join(stages[0: e]))  #adds new line to each string in stages list so each string in list prints on a separate line
        if "_" not in board: #checks for presence of empty underscores to see if player won  
            print("You win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))  #tells player if they lose
        print("You Died! It was {}. ".format(word))

hangman("cat")
