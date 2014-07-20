"""Handles data transfers between PoE servers and the API"""

import urllib
import requests
import auth
import constants as c
import json
from data.leagues import League

class DataTransfer(object):
    """Handles data transfers between PoE servers and the API,
    like characters and items"""

    def __init__(self, session_id):
        """Sets up a sessions and loads all current leagues."""
        self.auth = auth.Auth(session_id)
        self.session = requests.Session()
        self.leagues = self.get_leagues()

    def send_post(self, url, payload=0):
        """Does a POST request to PoE servers"""

        return session.post(url, headers=c.HEADERS, data=payload,
                            cookies=self.auth.get_cookies())

    def send_get(self, url):
        """Does a GET request to PoE servers"""

        return self.session.get(url)

    def get_leagues(self):
        """Saves all current leagues in the DataTransfer object"""

        league_list = []

        leagues = self.send_get(c.LEAGUES_URL)


        for league in leagues.json():
            league_list.append(League(league))

        return league_list

    def get_league_names(self):
        """Returns a list containing all current league names"""

        league_names = []

        for league in self.leagues:
            league_names.append(league.name)

        return league_names
