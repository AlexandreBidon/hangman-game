
from hangman_game.web_service.objects.word_model import Word


class WorldList():

    def __init__(self):
        self.list = []

    def add_word(self, word: Word):
        self.list.append(word)
