import random
import re


class Hangman:
    """
    A class to represent the Hangman game
    :method play(): Lets the player guess a letter.
    :method start_game(): Calls play() if the player still has lives left or didn't guess the word already.
    :method game_over(): Prints a game-over message.
    :method well_played(): Prints a message displaying the word_to_find, turn_count and error_count.
    """
    def __init__(self):
        """
        Init Hangman with
        :var self.possible_words: A list of words to choose from.
        :var self.word_to_find: A list of all characters in the chosen word to be found.
        :var self.lives: An int that shows the amount of lives left.
        :var self.correctly_guessed_letters: A list with all correctly guessed letters and '_' to represent the
        letters to be found.
        :var self.wrongly_guessed_letters: A list of all wrongly guessed letters.
        :var self.turn_count: An int that shows the amount of turns the player has already played for.
        :var self.error_count: An int that shows the amount of mistakes that were already made.
        """
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = [char for char in random.choice(self.possible_words)]
        self.lives = 5
        self.correctly_guessed_letters = ['_' for i in range(len(self.word_to_find))]
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        """
        Lets the player guess a letter. Checks if the guessed letter is correct and adds it to the right list.
        :return: None
        """
        while True:
            letter = input("Guess a letter. ")
            pattern = re.compile("[a-z]+")
            if pattern.fullmatch(letter) == False:
                print("Please give a lowercase letter: you can choose one from a-z.")
            elif len(letter) != 1:
                print("Only one letter at a time please!")
            else:
                break

        if self.word_to_find.count(letter) > 0:
            position = 0
            for i in range(self.word_to_find.count(letter)):
                index = self.word_to_find.index(letter, position)
                self.correctly_guessed_letters[index] = letter
                position = index + 1

        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1

    def start_game(self):
        """
        Calls play() if the player still has lives left or didn't guess the word already. Prints game stats.
        :return: None
        """
        while True:
            if self.lives == 0:
                Hangman.game_over(self)
                break
            elif self.correctly_guessed_letters.count('_') == 0:
                Hangman.well_played(self)
                break
            else:
                Hangman.play(self)
                self.turn_count += 1
                print('\n', ' '.join(self.correctly_guessed_letters), '\n \n X:',
                      ' '.join(self.wrongly_guessed_letters), '\n Lives:', self.lives, '\n Errors:', self.error_count,
                      '\n Turns:', self.turn_count)

    def game_over(self):
        """
        Prints a game-over message.
        :return: None
        """
        print('GaMe OvEr', '\n', 'Too bad!')

    def well_played(self):
        """
        Prints a message displaying the word_to_find, turn_count and error_count.
        :return: None
        """
        self.word_to_find = ''.join(self.word_to_find)
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!')