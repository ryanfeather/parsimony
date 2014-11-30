import pickle
from . import ParameterStore


class PickledParameterStore(ParameterStore):
    """ParameterStore that stores values in pickled format.
    """

    def __init__(self, file_name):
        """
        Constructor
        """
        self._file_name = file_name
        try:
            with open(self._file_name, 'rb') as pickle_file:
                self._store_data = pickle.load(pickle_file)
        except IOError:  # the file didn't exist or is otherwise inaccessible, we have no choice to regenerate
            self._store_data = {}
        super(PickledParameterStore, self).__init__()

    def __contains__(self, key):
        return key in self._store_data

    def parameter_keys(self, key):
        if key in list(self._store_data.keys()):
            return self._store_data[key]['parameters']
        return {}

    def compare(self, value, parameter_key):
        return value == self._store_data[parameter_key]['value']

    def update(self, key, value, parameter_keys=None):
        self._store_data[key] = {'parameters': parameter_keys, 'value': value}
        with open(self._file_name, 'wb') as pickle_file:
            pickle.dump(self._store_data, pickle_file,protocol=pickle.HIGHEST_PROTOCOL)
