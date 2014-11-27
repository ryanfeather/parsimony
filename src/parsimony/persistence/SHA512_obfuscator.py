import hashlib
from .data_obfuscator import DataObfuscator


class SHA512Obfuscator(DataObfuscator):
    """
    classdocs
    """

    def __init__(self):
        """
        Constructor
        """
        super(SHA512Obfuscator, self).__init__()

    def obfuscate(self, data):
        hashable_representation = self._hashable_representation(data)
        hasher = hashlib.sha512()
        hasher.update(hashable_representation)
        return hasher.digest()