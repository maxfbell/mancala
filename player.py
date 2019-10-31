class Player:
    """Mancala player."""
    
    def __init__(self, player, pots):
        """Initialise player.

        Args:
            player : int - player 0 or 1 to define which pots can be emptied.
            pots : list of the index's of the players pots. 
                From furthest from their mancala to the closest.

        """
        self.player = player
        self.pots = pots

    def play(self, state):
        """Default player logic.
        
        Override and pass derived player class to the Mancala class on 
        initialsation.
        
        Args:
            state : board state
            
        Return:
            int : index of pot to empty
        
        """
        # Check pots from closest to mancala to furthest.
        pot_indexs_backward = list(range(6))[::-1]
        for i in pot_indexs_backward:
            # Check if when emptied the pot will not spill into other 
            # player's pots.
            if state[self.pots[i]] >= 6 - i:
                # Return pot to be emptied.
                return self.pots[i]
        # Move any.
        for i in pot_indexs_backward:
            if state[self.pots[i]] > 0:
                return self.pots[i]
        # No move.
        raise NoMoveError(self.player, state)


class NoMoveError(Exception):
    """Raise when their is no move to make.
    
    Because I haven't implemented a solution because ot shouldn't happen...

    """
    
    def __init__(self, player, state, *args, **kwargs):
        print("Player", player)
        print("State:", state)
        super().__init__(*args, **kwargs)