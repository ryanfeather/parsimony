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

    def __init__(self, key, obfuscator=None, cache=None, store=None, **parameters):
        """Generate an object.

        A generator performs parameter sensitive caching.

        :param key: string key to use when referencing the cached object
        :param obfuscator: Obfuscator object used to make parameters cacheable. If None is given, the obfuscator will be
        created from configuration
        :param cache: cache object for parameter access and persistence. If None is given, the cache will be created from configuration
        :param store: store object for local persistence. If None is given, the store will be created from configuration
        :param parameters: parameters used to monitor the object. Parameters can be other generators, in which case recursive
        checks and generation occur as necessary.
        """
        self._key = key
        self._current_parameters = parameters
        self._generated_value = None
        self._generated = False
        self._cache_keys = self._generate_cache_keys()

        if obfuscator is None:
            self._obfuscator = parsimony.configuration.obfuscator()
        else:
            self._obfuscator = obfuscator

        if store is None:
            self._store = parsimony.configuration.store(key)
        else:
            self._store = store

        if cache is None:
            self._cache = parsimony.configuration.cache()
        else:
            self._cache = cache

    def generate(self):
        """Generate the object referred to by the key.

        If the object has never been generated before, the necessary work to create it is performed and the object is
        cached in a ParameterStore.

        If the object has been generated and the parameters have not been changed, the Generator checks for an in memory
         version of the object first and returns it.  If not in memory, the generated object is retrieved from a
         ParameterStore and cached in memory, then returned.

        If the object has been generated, but the parameters have changed, the object is regenerated and the
        ParameterStore is overwritten.

        :return generated_value: The value for this generator's key.
        """
        # regenerate if#
        # parameters have changed

        # did not exist in keys
        # generator parameters needed updated

        dirty = parsimony.dirty(self._key)
        if dirty:
            self._generated = False
            self._generated_value = None
            try:
                del self._cache[self._key]
            except KeyError:
                pass # throw all other errors, but a key error just means we weren't cached yet

        if (self._key in self._cache) and self._parameters_up_to_date() and self.up_to_date() and not dirty:
            if not self._generated:
                self._generated_value = self.load()
                self._generated = True
        else:
            for parameter, value in self._current_parameters.items():
                if not isinstance(value, parsimony.generators.Generator):
                    self._cache.update(self._cache_keys[parameter], self._obfuscator.obfuscate(value))
            self._update_parameters()  # parameters update needs to happen after storage since Generators get replaced
            self._generated_value = self.rebuild()       
            self.dump(self._generated_value)
            self._generated = True
            self._cache.update(self._key, self._obfuscator.obfuscate(GENERATOR_DEFAULT_STORE_VALUE),
                               list(self._cache_keys.values()))
            parsimony.clean(self._key)

        return self._generated_value

    def _mangled_parameter_key(self, parameter_key):
        """
        Create the mapping key from this generator to sub keys
        :param parameter_key:
        :return: combined self key and parameter key
        """
        return self.key() + ':' + parameter_key

    def _generate_cache_keys(self):
        """Get store keys from this objects current parameters.

        If the parameter is a generator, the key() method is used. Otherwise, the parameter key is generated in mangled
        fashion.
        :return: dict of parameter_key to key mappings
        """
        cache_keys = {}
        for parameter_key, parameter in self._current_parameters.items():
            if isinstance(parameter, parsimony.generators.Generator):
                cache_keys[parameter_key] = parameter.key()
            else:
                cache_keys[parameter_key] = self._mangled_parameter_key(parameter_key)

        return cache_keys

    def up_to_date(self):
        """Indicate if the generated value is fresh or stale with respect to non-parmeter changes. In the case
        of completely parameter driven values this will always be true. In the case of external objects or persisted
        data, it must be checked appropriately.

        This may be overridden in subclasses.
        :return: True if the value is fresh.
        """
        return True

    @abstractmethod
    def rebuild(self):
        """Internal method to regenerate the value based on current parameters.

        This method must be overriden in subclasses. Do not use externally.

        :return: generated value
        """
        pass

    def load(self):
        """Internal method to load the value from storage.

        This method may be overriden in subclasses. Do not use externally.

        :return: generated value
        """
        return self._store.read()

    def dump(self, value):
        """Internal method to store the value in storage.

        This method may be overriden in subclasses. Do not use externally.

        :return: generated value
        """
        self._store.write(value)

    def _cache_matches_current(self):
        """Compares the parameters_cache values to the current parameters.

        Checks store key equality and value equality of non-Generator parameters. Generator parameters
        are handled separately.
        :return: exact match or not of parameter store key-values
        """
        # same keys
        cache_parameters_keys = self._cache.parameter_keys(self._key)
        if cache_parameters_keys is None:
            return self._cache_keys.values is None
        cache_keys = set(cache_parameters_keys)
        current_keys = set(self._cache_keys.values())
        if cache_keys != current_keys:
            return False

        all_values_equal = True
        # compare values and types
        for parameter_key, value in self._current_parameters.items():
            if not isinstance(value, parsimony.generators.Generator):
                all_values_equal &= self._cache.compare(self._obfuscator.obfuscate(value), self._cache_keys[parameter_key])
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

    def _parameters_up_to_date(self):
        """ Internal method that checks generator and non-generator parameters for being up-to-date.

        :return: True if no update is needed, otherwise False
        """
        needs_update = not self._cache_matches_current()
        if not needs_update:
            for parameter in self._current_parameters.values():
                if isinstance(parameter, parsimony.generators.Generator):
                    needs_update |= not parameter.up_to_date() or parsimony.dirty(parameter.key())

        return not needs_update

    def _update_parameters(self):
        """Update generator parameters.
        """
        for parameter_key, parameter in self._current_parameters.items():
            if isinstance(parameter, parsimony.generators.Generator):
                self._current_parameters[parameter_key] = parameter.generate()
