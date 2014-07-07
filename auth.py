"""Handles login info and session"""

class Auth(object):
    """Handles login info and session"""
    """TODO: Add user/pass support"""

    def __init__(self, session_id):
        self.session = session_id
        self.email = 0
        self.password = 0
        self.cookie = {'PHPSESSID': session}

    def get_cookies(self):
        """Returns cookie including current PHPSESSID"""
        return self.cookie

