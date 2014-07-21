"""Handles the character class"""

class Character(object):
    """Handles a character and its inventory"""

    def __init__(self, character):
        """Takes a dict containing character data and saves in object"""
        self.name = character['name']
        self.character_class = character['class']
        self.level = character['level']
        self.league = character['league']

    def print_character(self):
        """Prints an string containing character info"""

        print("{} is a level {} {} in the {} league" .format(self.name,
            self.level, self.character_class, self.league)
        )

