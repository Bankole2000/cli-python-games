"""
File: main.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Project #2
Task: Solo & MultiPlayer Hangman game
"""

import random
from getpass import getpass
from words import word_list
from stages import display_hangman

maxTries = 7


class Player:
    def __init__(self, name, playerNumber, score=0, tries=0, isGuesser=False):
        self.name = name
        self.score = score
        self.tries = tries
        self.isGuesser = isGuesser
        self.playerNumber = playerNumber

    def __str__(self):
        return (f"Name: {self.name}\nGames Won: {self.score}\nSet Word: {self.isGuesser}")


def get_word():
    word = random.choice(word_list)
    return word.upper()


def showScores(guesser, wordGiver):
    print(
        f"\t{guesser.name}\tVS\t{wordGiver.name}\nScore\t{guesser.score}\t\t{wordGiver.score}\n")


def startGame(word, guesser, stage, wordGiver, mode):
    wordSpaces = "_" * len(word)
    gameWon = False
    guessedLetters = []
    guessedWords = []
    print("\n====***\t - New Game! - \t***====")
    showScores(guesser, wordGiver)
    print(
        f"It is {guesser.name}'s turn (Player {guesser.playerNumber}) to guess the word")
    input("Press any key to continue...")
    print(stage(guesser.tries))
    print(wordSpaces, end="")
    print(f"\t{len(word)} letters")
    print("\n")
    while not gameWon and guesser.tries < maxTries:
        guess = input(
            f"(Player {guesser.playerNumber}) {guesser.name}, guess a letter or the word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print(
                    f"But (Player {guesser.playerNumber}) {guesser.name}, You already guessed the letter", guess)
            elif guess not in word:
                print(u'\u274C', end="")
                print(
                    f" - Sorry (Player {guesser.playerNumber}) {guesser.name}, Letter {guess}, is not in the word.")
                guesser.tries += 1
                guessedLetters.append(guess)
            else:
                print(u'\u2713', end="")
                print(
                    f" - CORRECT! Good job (Player {guesser.playerNumber}) {guesser.name}, {guess} is in the word!")
                guessedLetters.append(guess)
                wordAsList = list(wordSpaces)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordSpaces = "".join(wordAsList)
                if "_" not in wordSpaces:
                    gameWon = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print(
                    f"But (Player {guesser.playerNumber}) {guesser.name}, You already guessed that word {guess}")
            elif guess != word:
                print(u'\u274C', end="")
                print(
                    f"  - Sorry (Player {guesser.playerNumber}) {guesser.name}, {guess} is not the word.")
                guesser.tries += 1
                guessedWords.append(guess)
            else:
                gameWon = True
                wordSpaces = word
        else:
            print(u'\u274C', end="")
            print(" - Not a valid guess.")
        print(stage(guesser.tries))
        print(wordSpaces, end="")
        print(f"\t{len(word)} letters\n")
    if gameWon:
        print(u'\u2714'*3, end="")
        print(
            f" - YOU WIN!!! CONGRATS {guesser.name} (Player {guesser.playerNumber})! You guessed the word!")
        guesser.score += 1
    else:
        print(u'\u274C'*3, end="")
        print(f" - GAME OVER!!! Sorry, you ran out of tries (Player {guesser.playerNumber}) {guesser.name}. The word was " +
              word + ". Maybe next time!")
        wordGiver.score += 1
    print("\n====***\t- Current Score -\t***====")
    showScores(guesser, wordGiver)
    if input("Play again (y/n)? ").upper() == "Y":
        if mode == "solo":
            newWord = get_word()
            guesser.tries = 0
            startGame(newWord, guesser, stage, wordGiver, mode)
        else:
            if input("Switch Sides (y/n)? ").upper() == "Y":
                newWord = getpass(
                    f" - (Player {guesser.playerNumber}) {guesser.name}. Now it's your turn, please enter the word to be guessed \n(characters will be hidden): ")
                newWord = newWord.upper()
                guesser.tries = 0
                wordGiver.tries = 0
                startGame(newWord, wordGiver, stage, guesser, mode)
            else:
                newWord = getpass(
                    f" - (Player {wordGiver.playerNumber}) {wordGiver.name}, please enter the word to be guessed \n(characters will be hidden): ")
                newWord = newWord.upper()
                guesser.tries = 0
                wordGiver.tries = 0
                startGame(newWord, guesser, stage, wordGiver, mode)

    print("\n====***\t- Final Score -\t***====")
    showScores(guesser, wordGiver)
    input("Press any key to continue...")


def mainMenu():
    while True:
        print("\n=====***! - LET'S PLAY HANGMAN - !***=====")
        print(" - Please Select a Game mode:")
        print(" [1] Single player (vs computer)")
        print(" [2] Multiplayer (vs human)")
        gameMode = int(
            input("\nEnter an option (1) Single player (2) Multiplayer: "))
        if gameMode == 1:
            confirm1 = "n"
            while confirm1 != "Y":
                playerName = input(
                    "\n - Player 1, please enter your name: ").upper()
                confirm1 = input(
                    f" - Player 1, your name is {playerName} - Confirm (y/n)? ").upper()
            SoloPlayer = Player(playerName, 1)
            Computer = Player("Computer", 2)
            setWord = get_word()
            print("\n====***\t  Game Set START!!!\t***====")
            showScores(SoloPlayer, Computer)
            startGame(setWord, SoloPlayer, display_hangman, Computer, "solo")

        elif gameMode == 2:
            confirm1 = confirm2 = "n"
            while confirm1 != "Y":
                player1Name = input(
                    "\n - Player 1, please enter your name: ").upper()
                confirm1 = input(
                    f" - Player 1, your name is {player1Name} - Confirm (y/n)? ").upper()
            Player1 = Player(player1Name, 1)
            while confirm2 != "Y":
                player2Name = input(
                    "\n - Player 2, please enter your name: ").upper()
                confirm2 = input(
                    f" - Player 2, your name is {player2Name} - Confirm (y/n)? ").upper()
            Player2 = Player(player2Name, 2)
            print("\n====***\t  Game Set START!!!\t***====")
            showScores(Player1, Player2)
            if Player1.isGuesser == Player2.isGuesser == False:
                setWord = getpass(
                    f" - (Player 1) {Player1.name}, please enter the word to be guessed \n(characters will be hidden): ")
                setWord = setWord.upper()
                Player2.isGuesser = True
                startGame(setWord, Player2, display_hangman, Player1, "multi")

        else:
            print("Invalid option selected Please enter a valid option")
            continue


mainMenu()
