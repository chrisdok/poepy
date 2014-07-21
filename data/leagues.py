"""Handles a league"""

class League(object):
    """Handles a single league and its data"""
    def __init__(self, league):

        self.ladder = league['ladder']
        self.rules = league['rules']
        self.name = league['id']
        self.start = league['registerAt']
        self.end = league['endAt']

    def update_items(self, items):
        """Saves all items in the stashtab of current league"""
        if items is not False:
            tabs = items['numTabs']
            for item in items['items']:
                pass


