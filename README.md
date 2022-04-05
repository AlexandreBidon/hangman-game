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

## TODO

Add some tests