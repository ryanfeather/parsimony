from abc import ABCMeta, abstractmethod


class Store(metaclass=ABCMeta):
    """A store is an object that implements read and write capabilities for key-ed values

    """
    def __init__(self, key):
        self.key = key

    @abstractmethod
    def read(self):
        """Method to retrieve the persisted value of this store.

        Must be overridden by subclasses.

        :return: the saved value from this store
        """
        pass

    @abstractmethod
    def write(self, value):
        """Method to persist a value in this store

        Must be overridden by subclasses.
        """
        pass