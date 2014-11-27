import pickle

from abc import ABCMeta, abstractmethod


class DataObfuscator(metaclass=ABCMeta):

    @staticmethod
    def _hashable_representation(data):
        # in the future, a "library" of representation generators could be usable
        # for efficiency gains
        return pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)

    @abstractmethod
    def obfuscate(self,data):
        pass