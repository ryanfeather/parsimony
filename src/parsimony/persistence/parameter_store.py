from abc import ABCMeta, abstractmethod


class ParameterStore(metaclass=ABCMeta):
    """
    classdocs
    """

    @abstractmethod
    def parameter_keys(self, key):
        pass

    @abstractmethod
    def compare(self, value, parameter_key):
        pass

    @abstractmethod
    def update(self, key, value, parameter_keys=None):
        pass

