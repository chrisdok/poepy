"""Handles a league"""

class League(object):
    """Handles a single league and its data"""
    def __init__(self, league):
        self.ladder = league['ladder']
        self.rules = league['rules']
        self.name = league('id')
        self.start = league['registerAt']
        self.end = league['endAt']

