import random
HANGMAN_PICS = ['''
  -----
  |   |
      |
      |
      |
      |
=========''', '''
  -----
  |   |
  O   |
      |
      |
      |
=========''', '''
  -----
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  -----
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  -----
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
list_of_words = ["sloth", "koala", "leopard", "tiger", "panda", "elephant", "giraffe","pumpkin","python","intersection","recursive","freckle","month","easy","turkey","if"]
random_choice= random.randint(0,len(list_of_words)-1)
back_word = list_of_words[random_choice]
front_word = []
for i in range(len(back_word)):
    front_word.append("_")
game_finished = False
tryes = 0
guesed_letters = []
while not game_finished:
    for i in range(len(front_word)):
        print(front_word[i], end="")
    print()
    valid_input = False
    while not valid_input:
        letter_choice = input("Input the letter here -")
        try:
            letter_choice = str(letter_choice)
        except:
            print("Enter thr letter")
        else:
            if len(letter_choice) == 1:
                letter_choice = letter_choice.lower()
                if letter_choice in guesed_letters:
                    print("You guessed this letter before")
                else:
                    guesed_letters.append(letter_choice)
                    valid_input = True
            else:
                print("Input one letter!!!")
    if letter_choice in back_word:
        letter_place = []
        for i in range(len(back_word)):
            if back_word[i] == letter_choice.lower():
                front_word[i]= letter_choice.upper()
                print("open the letter "+str(letter_choice.upper()))
        if "_" not in front_word:
            for i in range(len(front_word)):
                print(front_word[i], end="")
            print()
            print("Yea you are right that is "+ str(back_word))
            game_finished = True
    else:
        print("Ther is not letter "+str(letter_choice))
        print(HANGMAN_PICS[tryes])
        if tryes == 6:
            print("HE DIED BECAUSE OF YOU")
            print("Actualy the word is "+str(back_word))
            game_finished = True
        tryes +=1 

                