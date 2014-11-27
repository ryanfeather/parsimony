"""
Created on Jun 30, 2013

@author: rfeather
"""
import parsimony
from abc import ABCMeta, abstractmethod

GENERATOR_DEFAULT_STORE_VALUE = True


class Generator(metaclass=ABCMeta):
    """
    classdoc
    """

    def __init__(self, key, **parameters):
        self._key = key
        self._current_parameters = parameters
        self._generated_value = None
        self._generated = False
        self._store_keys = self._generate_store_keys()

    def generate(self):
        # regenerate if#
        # parameters have changed

        # did not exist in keys
        # generator parameters needed updated
        parameters_store = parsimony.configuration.store()

        if (self._key in parameters_store) and self._parameters_up_to_date(parameters_store) and self.up_to_date():
            if self._generated:
                return self._generated_value
            else:
                self._generated_value = self.load()
                self._generated = True
                return self._generated_value
        else:
            for parameter, value in self._current_parameters.items():
                if not isinstance(value, parsimony.generators.Generator):
                    parameters_store.update(self._store_keys[parameter], value)
            self._update_parameters()  # parameters update needs to happen after storage since Generators get replaced

            self._generated_value = self.rebuild()
            parameters_store.update(self._key, GENERATOR_DEFAULT_STORE_VALUE, list(self._store_keys.values()))
            self.store(self._generated_value)
            self._generated = True
            return self._generated_value

    def _mangled_parameter_key(self, parameter_key):
        return self.key() + ':' + parameter_key

    def _generate_store_keys(self):
        store_keys = {}
        for parameter_key, parameter in self._current_parameters.items():
            if isinstance(parameter, parsimony.generators.Generator):
                store_keys[parameter_key] = parameter.key()
            else:
                store_keys[parameter_key] = self._mangled_parameter_key(parameter_key)

        return store_keys

    # noinspection PyMethodMayBeStatic
    @abstractmethod
    def up_to_date(self):
        return True

    @abstractmethod
    def rebuild(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def store(self, value):
        pass

    def _store_matches_current(self, parameters_store):
        # same keys
        store_parameters_keys = parameters_store.parameter_keys(self._key)
        store_keys = set(store_parameters_keys)
        current_keys = set(self._store_keys.values())
        if store_keys != current_keys:
            return False

        all_values_equal = True
        # compare values and types
        for parameter_key, value in self._current_parameters.items():
            if not isinstance(value, parsimony.generators.Generator):
                all_values_equal &= parameters_store.compare(value, self._store_keys[parameter_key])

        return all_values_equal

    def key(self):
        return self._key

    def get_parameter(self, key):
        return self._current_parameters[key]

    def _parameters_up_to_date(self, parameters_store):
        needs_update = not self._store_matches_current(parameters_store)
        if not needs_update:
            for parameter in self._current_parameters.values():
                if isinstance(parameter, parsimony.generators.Generator):
                    needs_update |= not parameter.up_to_date()

        return not needs_update

    def _update_parameters(self):
        for parameter_key, parameter in self._current_parameters.items():
            if isinstance(parameter, parsimony.generators.Generator):
                self._current_parameters[parameter_key] = parameter.generate()
