import dill

from abc import ABCMeta, abstractmethod


class DataObfuscator(metaclass=ABCMeta):
    """Interface for data hashers

    Obfuscation is the method to make easily comparable, storage efficent, potentially secure versions of the data.
    """
    @staticmethod
    def _hashable_representation(data):
        """Generate a hashable representation of the data. Current implentation is pickle based.
        """
        # in the future, a "library" of representation generators could be usable
        # for efficiency gains
        return dill.dumps(data)

    @abstractmethod
    def obfuscate(self, data):
        """Create the hashed data representation

        This is method must be overridden by subclasses.

        :param data: data to obfuscate

        :return: obfuscated representation such as a hash
        """
        pass