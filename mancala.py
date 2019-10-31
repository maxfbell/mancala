from board import Board, board_format
from player import Player


class Mancala:
    """The game Mancala."""
    board = Board()
    players_pots = [
        [0, 1, 2, 3, 4, 5],
        [7, 8, 9, 10, 11, 12]
    ]
    
    def __init__(self, player=Player):
        """Initialise mancala.

        Args:
            player : derived player class with custom play logic

        """
        self.players = [player(i, self.players_pots[i]) for i in range(2)]

    def play(self):
        """Let's play mancala. Returns winner or None if draw."""
        player = 0
        self.print()
        while not self.game_over:
            self.move(player, self.players[player].play(self.board.state))
            self.print()
            player = not player
        return self.winner

    def print(self):
        """Simple board print out."""
        print(board_format.format(*self.board.state))

    def move(self, player, pot):
        """Empty and move marbles form the pot.
        
        Args:
            player : int - player number to check if player's pot
            pot : int - pot index to empty
        
        """
        if pot not in self.players_pots[player]:
            raise UnauthorisedPotSelection(player, pot)
        else:
            marbles = self.board.pots[pot].empty()
            for marble in marbles:
                pot += 1
                if pot > 13:
                    pot = 0
                self.board.pots[pot].add(marble)

    @property
    def game_over(self):
        """Boolean of the game's state."""
        pots = self.board.state
        pots.pop(6)
        pots.pop(13)
        if sum(pots) == 0:
            return True
        else:
            return False

    @property
    def winner(self):
        """The winner of the game at any stage.
        
        Returns:
            0 : Player 1
            1 : Player 2
            None : Draw
            
        """
        if self.board.state[6] > self.board.state[13]:
            return 0
        elif self.board.state[6] < self.board.state[13]:
            return 1
        else:
            return None


class UnauthorisedPotSelection(ValueError):
    """Raise when a player's play returns an index of a pot which is not theirs.
    
    Indicates there is an errors in the player play logic.
    
    """
    
    def __init__(self, player, index, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Player", player)
        print("Pot", index)


def main():
    mancala = Mancala()
    result = mancala.play()
    if result is None:
        print("Draw")
    else:
        print("Player", result, "winners.")

if __name__ == "__main__":
    main()