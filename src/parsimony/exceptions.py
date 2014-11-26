__author__ = 'rfeather'


class ParsimonyException(Exception):

    def __init__(self, message):
        self.message = message

    def ___str__(self):
        return self.message
