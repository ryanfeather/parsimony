import hashlib
from .data_obfuscator import DataObfuscator


class SHA512Obfuscator(DataObfuscator):
    """DataObfuscator that uses the SHA512 hashing mechanism.

    """

    def __init__(self):
        """
        """
        super(SHA512Obfuscator, self).__init__()

    def obfuscate(self, data):
        """Generate SHA512 of the hashable data representation

        :param data: data to obfuscate
        :return: hash
        """
        hashable_representation = self._hashable_representation(data)
        hasher = hashlib.sha512()
        hasher.update(hashable_representation)
        return hasher.digest()