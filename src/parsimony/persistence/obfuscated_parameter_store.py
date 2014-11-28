from abc import ABCMeta,abstractmethod

import parsimony
from .parameter_store import ParameterStore


class ObfuscatedParameterStore(ParameterStore, metaclass=ABCMeta):
    """Parameter Store that obfuscates values.

    """

    def __init__(self):
        self._obfuscator = parsimony.configuration.obfuscator()
        super(ObfuscatedParameterStore, self).__init__()

    def compare(self, value, parameter_key):
        """Compare the obfuscated representation of the value to the current parameter obfuscated value.

        :param value:
        :param parameter_key:
        :return: If there is a match
        """
        obfuscated_value = self._obfuscator.obfuscate(value)
        return self._obfuscated_compare(obfuscated_value, parameter_key)

    def update(self, key, value, parameter_keys=None):
        """Set the current obfuscated value.

        :param key:
        :param value:
        :param parameter_keys:
        :return:
        """
        obfuscated_value = self._obfuscator.obfuscate(value)
        return self._obfuscated_update(key, obfuscated_value, parameter_keys)

