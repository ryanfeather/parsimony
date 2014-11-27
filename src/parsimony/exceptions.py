__author__ = 'rfeather'


class ParsimonyException(Exception):
    """ Base exception for parsimony.

    Extend this for defining exceptions.
    """

    def __init__(self, message):
        self.message = message

    def ___str__(self):
        return self.message
