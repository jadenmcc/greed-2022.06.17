from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to hold and provide information
    about itself, most noteably its _game_point value.

    Attributes:
        _message (string): A short description about the artifact.
        # JADEN ADDED BELOW:
        _game_point (int): The numerical point value (+ or -) of the artifact.
            (Whether you score points from it or lose points from it.)
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._game_point = 0
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message

# JADEN WROTE THIS FUNCTION:
    def get_game_point(self):
        return self._game_point
    
    def set_message(self, text):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        # JADEN WROTE BELOW:
        if self._text == chr(42):
            self._message = "+100"
        else:
            self._message = "-100"
        
# JADEN WROTE THIS FUNCTION:
    def set_game_point(self):
        if self._text == chr(42):
            self._game_point = 100
        else:
            self._game_point = -100