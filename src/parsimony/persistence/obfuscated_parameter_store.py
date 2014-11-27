from abc import ABCMeta,abstractmethod

import parsimony
from .parameter_store import ParameterStore


class ObfuscatedParameterStore(ParameterStore, metaclass=ABCMeta):
    """
    classdocs
    """

    def __init__(self):
        """
        Constructor
        """
        self._obfuscator = parsimony.configuration.obfuscator()
        super(ObfuscatedParameterStore, self).__init__()

    def compare(self, value, parameter_key):
        obfuscated_value = self._obfuscator.obfuscate(value)
        return self._obfuscated_compare(obfuscated_value, parameter_key)

    def update(self, key, value, parameter_keys=None):
        obfuscated_value = self._obfuscator.obfuscate(value)
        return self._obfuscated_update(key, obfuscated_value, parameter_keys)

