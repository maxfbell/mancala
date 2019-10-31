# Mancala Simulator
Written in Python 3.6

Run `mancala.py` for default game logic.

To implement custom player logic subclass `Player` and overwrite `Player.play()`. See the class for documentation. Then pass the player subclass to the `Mancala` class when initialising the game `Mancala(player=PlayerSubClass)`.