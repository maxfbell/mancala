from marble import Marble


class Pot:
    """Mancala Pot."""

    def __init__(self, position):
        """Initialise pot with 4 marbles unless position 6 or 13.

        Args:
            position : int of pot index, 6 or 13 initialise empty.

        """
        self.position = position
        # Generate marbles
        if position in [6, 13]:
            self.marbles = []
        else:
            self.marbles = [Marble() for _ in range(4)]

    def empty(self):
        """Empty pot for move and return marbles."""
        marbles = self.marbles.copy()
        self.marbles.clear()
        return marbles

    def add(self, marble):
        """Add marble to the pot."""
        self.marbles.append(marble)

    @property
    def count(self):
        """The number of marbles in the pot."""
        return len(self.marbles)