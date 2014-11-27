from parsimony.generators import Generator
import pickle
import os
import string


class PickledCallableWrapper(Generator):
    def __init__(self, directory, key, function, **parameters):
        self._function = function  # keep separate references to avoid copying later
        self._param_keys = list(parameters.keys())
        self._store_location = self._generate_store_location(directory, key)
        super(PickledCallableWrapper, self).__init__(key, function=function, **parameters)

    def up_to_date(self):
        # always return True - the framework will take care of updates due to parameter or function changes
        return True

    def rebuild(self):
        # retrieve generated parameters
        params = {key: self.get_parameter(key) for key in self._param_keys}
        return self._function(**params)

    def load(self):
        with open(self._store_location, 'rb') as result_file:
            result = pickle.load(result_file)
        return result

    def store(self, value):
        with open(self._store_location, 'wb') as result_file:
            pickle.dump(value, result_file)


    # noinspection PyMethodMayBeStatic
    def _generate_store_location(self, directory, key):
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        file_name = ''.join(c if c in valid_chars else '_' for c in key)
        return os.path.join(directory, file_name)