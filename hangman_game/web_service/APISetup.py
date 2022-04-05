from fastapi import FastAPI
from web_service.objects.guess_model import Guess
from web_service.objects.word_model import Word
from web_service.objects.word_list import WordList
from web_service.objects.setup_model import Setup
from web_service.core.game_engine import GameEngine
from web_service.utils.add_default_word import add_default_word
import uuid
import json


class APISetup():
    """
    Setup the API using FastAPI package
    Setup all the endpoints
    """

    def __init__(self):
        self.app = FastAPI()
        self.word_list = add_default_word(WordList())
        self.game_engine_dict = {}

        @self.app.post("/setup")
        async def create_game(setup: Setup):
            id = str(uuid.uuid4().hex)
            self.game_engine_dict[id] = GameEngine(self.word_list, id)
            print(id)
            return self.game_engine_dict[id].new_game(setup)

        @self.app.post("/{id}/guess")
        async def make_guess(guess: Guess, id: str):
            return self.game_engine_dict[id].make_guess(guess)

        @self.app.get("/mots")
        async def word_list():
            return(self.word_list.list)

        @self.app.post("/mot")
        async def create_mot(word: Word):
            self.word_list.add_word(word)
