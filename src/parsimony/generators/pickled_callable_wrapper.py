from parsimony.generators import Generator
import pickle
import os
import string


class PickledCallableWrapper(Generator):
    """ Generator for callables using pickle as the underlying storage mechanism

    """
    def __init__(self, directory, key, function, **parameters):
        """The PickledCallableWrapper is a simple way to cache arbitrary function results.

        :param directory: directory to cache in
        :param key: generator key string
        :param function: callable handle
        :param parameters: key-value parameters for the callable function
        """
        self._function = function  # keep separate references to avoid copying later
        self._param_keys = list(parameters.keys())
        if not os.path.exists(directory):
            os.makedirs(directory)
        self._store_location = self._generate_store_location(directory, key)
        super(PickledCallableWrapper, self).__init__(key, function=function, **parameters)

    def up_to_date(self):
        """ Returns true since the framework will always take care of updates to arguments or the callable.

        :return: True
        """
        return True

    def rebuild(self):
        """ Call the callable with parameters to generate the value

        :return: generated value
        """
        params = {key: self.get_parameter(key) for key in self._param_keys}
        return self._function(**params)

    def load(self):
        """Retrieves the value from the pickle store

        :return: loaded generated value
        """
        with open(self._store_location, 'rb') as result_file:
            result = pickle.load(result_file)
        return result

    def store(self, value):
        """Dump the value to the pickle store

        :param value: value to dump
        """
        with open(self._store_location, 'wb') as result_file:
            pickle.dump(value, result_file)


    # noinspection PyMethodMayBeStatic
    def _generate_store_location(self, directory, key):
        """Generates a location in the pickle directory to store to

        :param directory: base directory
        :param key: value key, necessary because this is called in the constructor
        """
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        file_name = ''.join(c if c in valid_chars else '_' for c in key)
        return os.path.join(directory, file_name)