from web_service.objects.guess_model import Guess
from web_service.objects.word_model import Word
from web_service.objects.setup_model import Setup
from web_service.objects.word_list import WordList
import random
import logging
from fastapi import FastAPI, HTTPException


class GameEngine():
    '''
    Runs the game
    '''

    def __init__(self, word_list: WordList, id):
        self.max_error = 10
        self.error = 0
        self.word_list = word_list
        self.guessed_letters = []
        self.current_word = "_"
        self.id = id

    def new_game(self, setup: Setup):
        logging.info('Creating new game with id {}'.format(self.id))
        setup_dict = setup.dict()
        self.max_error = setup_dict["max_error"]
        self.error = 0
        try:
            self.word = random.choice(self.word_list).dict()["letters"]
            self.current_word = "_" * len(self.word)
        except:
            raise HTTPException(status_code=400, detail="Word List is empty")
        print("test2")
        self.guessed_letters = []
        logging.info("New game created with the word {word} and {max_error} max errors.".format(
            word=self.word, max_error=self.max_error))
        return({"id": self.id})

    def make_guess(self, guess: Guess):
        guessed_letter = guess.dict()["letter"]
        logging.info("Player tried the letter {}".format(guessed_letter))
        if guessed_letter in self.word:
            self.guessed_letters.append(guessed_letter)
            current_word = ""
            for letter in self.word:
                if letter in self.guessed_letters:
                    current_word += letter
                else:
                    current_word += "_"
            self.current_word = current_word
            return({"status": "playing", "word": self.current_word, "errors": self.error})
        else:
            self.error += 1
            if self.error > self.max_error:
                return({"status": "game failed, setup new game", "word": self.word, "errors": self.error})
            else:
                return({"status": "playing", "word": self.current_word, "errors": self.error})
