from parsimony.generators import Generator
from parsimony.configuration import context_name, parsimony_directory

import pickle
import os
import string


class StoredCallableWrapper(Generator):
    """ Generator for callables using that stores results.

    """
    def __init__(self, key, function, **parameters):
        """The PickledCallableWrapper is a simple way to cache arbitrary function results.  Results are stored in
        the context subdirectory of the parsimony directory.

        :param key: generator key string
        :param function: callable handle
        :param callable_store: store object used to persist. If None is given, the store will be created from configuration
        :param parameters: key-value parameters for the callable function
        """

        self._function = function  # keep separate references to avoid copying later
        self._param_keys = list(parameters.keys())
        super(StoredCallableWrapper, self).__init__(key, function=function, **parameters)

    def rebuild(self):
        """ Call the callable with parameters to generate the value

        :return: generated value
        """
        params = {key: self.get_parameter(key) for key in self._param_keys}
        return self._function(**params)

