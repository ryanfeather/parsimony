import pickle
from . import Cache


class MemCache(Cache):
    """Parameter Cache that will bring parameters from a store into local memory if it exists and persist updates to
    the store.
    """

    def __init__(self, store):
        """Initialize by reading from the store

        :param: Store object
        """

        self._store = store
        try:
            self._store_data = self._store.read()
        except IOError:  # the file didn't exist or is otherwise inaccessible, we have no choice to regenerate
            self._store_data = {}

        super().__init__()

    def __contains__(self, key):
        return key in self._store_data

    def __delitem__(self, key):
        del self._store_data[key]
        self._store.write(self._store_data)

    def parameter_keys(self, key):
        if key in list(self._store_data.keys()):
            return self._store_data[key]['parameters']
        return {}

    def compare(self, value, parameter_key):
        return value == self._store_data[parameter_key]['value']

    def update(self, key, value, parameter_keys=None):
        """Update the memory cache and store

        :param key: key of object to store
        :param value: value of object to store
        :param parameter_keys: keys for generator parameters
        """
        self._store_data[key] = {'parameters': parameter_keys, 'value': value}
        self._store.write(self._store_data)