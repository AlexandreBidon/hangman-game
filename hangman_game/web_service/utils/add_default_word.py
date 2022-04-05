import json
from web_service.objects.word_model import Word


def add_default_word(word_list):
    default_word_file = open(
        "hangman_game/web_service/objects/default_words.json")
    default_world = json.load(default_word_file)
    for word in default_world:
        new_word = Word(id=word["id"], letters=word["letters"])
        word_list.add_word(new_word)
    return(word_list)