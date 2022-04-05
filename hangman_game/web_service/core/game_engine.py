from web_service.objects.guess_model import Guess
from web_service.objects.word_model import Word
from web_service.objects.setup_model import Setup
from web_service.objects.word_list import WordList
import random
import logging


class GameEngine():
    '''
    Runs the game
    '''

    def __init__(self, word_list: WordList):
        self.max_error = 10
        self.error = 0
        self.word_list = word_list

    def new_game(self, setup: Setup):
        logging.info('Creating new game')
        setup_dict = setup.dict()
        self.max_error = setup_dict.max_error
        self.error = 0
        self.word = random.choice(self.word_list)
        logging.info("New game created with the word {word} and {max_error} max errors.".format(
            word=self.word, max_error=self.max_error))

    def make_guess(guess: Guess):
        guess_dict = guess.dict()
        if guess_dict.letter in
