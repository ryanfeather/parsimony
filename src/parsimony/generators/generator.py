"""
Created on Jun 30, 2013

@author: rfeather
"""
import parsimony
from abc import ABCMeta, abstractmethod

GENERATOR_DEFAULT_STORE_VALUE = True


class Generator(metaclass=ABCMeta):
    """Generator abstract base class. This is the core object for cached generation.

    """

    def __init__(self, key, **parameters):
        """Generate an object.

        A generator performs parameter sensitive caching.

        :param key: string key to use when referencing the cached object
        :param parameters: parameters used to monitor the object. Parameters can be other generators, in which case recursive
        checks and generation occur as necessary.
        """
        self._key = key
        self._current_parameters = parameters
        self._generated_value = None
        self._generated = False
        self._store_keys = self._generate_store_keys()

    def generate(self):
        """Generate the object referred to by the key.

        If the object has never been generated before, the necessary work to create it is performed and the object is
        cached in a ParameterStore.

        If the object has been generated and the parameters have not been changed, the Generator checks for an in memory
         version of the object first and returns it.  If not in memory, the generated object is retrieved from a
         ParameterStore and cached in memory, then returned.

        If the object has been generated, but the parameters have changed, the object is regenerated and the ParameterStore
        is overwritten.

        :return generated_value: The value for this generator's key.
        """
        # regenerate if#
        # parameters have changed

        # did not exist in keys
        # generator parameters needed updated
        parameters_store = parsimony.configuration.store()
        obfuscator = parsimony.configuration.obfuscator()
        
        if (self._key in parameters_store) and self._parameters_up_to_date(parameters_store,obfuscator) and self.up_to_date():
            if self._generated:
                return self._generated_value
            else:
                self._generated_value = self.load()
                self._generated = True
                return self._generated_value
        else:
            for parameter, value in self._current_parameters.items():
                if not isinstance(value, parsimony.generators.Generator):
                    parameters_store.update(self._store_keys[parameter], obfuscator.obfuscate(value))
            self._update_parameters()  # parameters update needs to happen after storage since Generators get replaced

            self._generated_value = self.rebuild()
            
            parameters_store.update(self._key, obfuscator.obfuscate(GENERATOR_DEFAULT_STORE_VALUE), list(self._store_keys.values()))
            self.store(self._generated_value)
            self._generated = True
            return self._generated_value

    def _mangled_parameter_key(self, parameter_key):
        """
        Create the mapping key from this generator to sub keys
        :param parameter_key:
        :return: combined self key and parameter key
        """
        return self.key() + ':' + parameter_key

    def _generate_store_keys(self):
        """Get store keys from this objects current parameters.

        If the parameter is a generator, the key() method is used. Otherwise, the parameter key is generated in mangled
        fashion.
        :return: dict of parameter_key to key mappings
        """
        store_keys = {}
        for parameter_key, parameter in self._current_parameters.items():
            if isinstance(parameter, parsimony.generators.Generator):
                store_keys[parameter_key] = parameter.key()
            else:
                store_keys[parameter_key] = self._mangled_parameter_key(parameter_key)

        return store_keys

    @abstractmethod
    def up_to_date(self):
        """Indicate if the generated value is fresh or stale with respect to non-parmeter changes. In the case
        of completely parameter driven values this will always be true. In the case of external objects or persisted
        data, it must be checked appropriately.

        This must be overridden in subclasses.
        :return: True if the value is fresh.
        """
        pass

    @abstractmethod
    def rebuild(self):
        """Internal method to regenerate the value based on current parameters.

        This method must be overriden in subclasses. Do not use externally.

        :return: generated value
        """
        pass

    @abstractmethod
    def load(self):
        """Internal method to load the value from storage.

        This method must be overriden in subclasses. Do not use externally.

        :return: generated value
        """
        pass

    @abstractmethod
    def store(self, value):
        """Internal method to store the value in storage.

        This method must be overriden in subclasses. Do not use externally.

        :return: generated value
        """
        pass

    def _store_matches_current(self, parameters_store,obfuscator):
        """Compares the parameter_store values to the current parameters.

        Checks store key equality and value equality of non-Generator parameters. Generator parameters
        are handled separately.
        :param parameters_store:
        :return: exact match or not of parameter store key-values
        """
        # same keys
        store_parameters_keys = parameters_store.parameter_keys(self._key)
        if store_parameters_keys is None:
            return self._store_keys.values is None
        store_keys = set(store_parameters_keys)
        current_keys = set(self._store_keys.values())
        if store_keys != current_keys:
            return False

        all_values_equal = True
        # compare values and types
        for parameter_key, value in self._current_parameters.items():
            if not isinstance(value, parsimony.generators.Generator):
                all_values_equal &= parameters_store.compare(obfuscator.obfuscate(value), self._store_keys[parameter_key])

        return all_values_equal

    def key(self):
        """Get the key of this Generator

        :return key: string
        """
        return self._key

    def get_parameter(self, parameter_key):
        """Return a parameter based on key.

        :param parameter_key:
        :return: parameter matching the parameter key
        """
        return self._current_parameters[parameter_key]

    def _parameters_up_to_date(self, parameters_store,obfuscator):
        """ Internal method that checks generator and non-generator parameters for being up-to-date.

        :param parameters_store:
        :return: True if no update is needed, otherwise False
        """
        needs_update = not self._store_matches_current(parameters_store,obfuscator)
        if not needs_update:
            for parameter in self._current_parameters.values():
                if isinstance(parameter, parsimony.generators.Generator):
                    needs_update |= not parameter.up_to_date()

        return not needs_update

    def _update_parameters(self):
        """Update generator parameters.
        """
        for parameter_key, parameter in self._current_parameters.items():
            if isinstance(parameter, parsimony.generators.Generator):
                self._current_parameters[parameter_key] = parameter.generate()
