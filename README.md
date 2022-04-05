# Hangman game

![](https://raw.githubusercontent.com/AlexandreBidon/Funky-Horse/main/out/line.png)

## How to start

### Dependencies
First, make sure to install the dependencies using `pip install -r requirements.txt`.

### Run the project

To run the API you have to run the file `__main__.py` in the web_service folder. You will have the address of the local server.

You can use the file `info.log` to debug.

![](https://raw.githubusercontent.com/AlexandreBidon/Funky-Horse/main/out/line.png)
## How to use

### Setup a new game

You can setup a new game using the POST endpoint `/setup`. You will have to provide a JSON file with the parameters of the game. For now the only parameter is max_error. This endpoint will send back the id of the game.

You can setup a game like this :

```json
{
    "max_error": 10
}
```
### Play a game

You can then use this id to play this specific game. You can guess a letter with the POST endpoint `/id/guess` with id being the id of your game.
You can send a guess like this :

```json
{
  "letter" : "a"
}
```

The server will respond with informations on the game. The answer will look like this :

```json
{
	"status": "playing",
	"word": "p__me",
	"errors": 2,
    "letters tried" : ["p","m","e","a","b"]
}
```

You can try to guess the word by making a new guess after each response.

## TODO

-Add some tests
- Create a client side interface
- Add an authentification system for players
- Add a game cleaner after inactivity