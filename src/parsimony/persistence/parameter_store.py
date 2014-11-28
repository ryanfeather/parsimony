from abc import ABCMeta, abstractmethod


class ParameterStore(metaclass=ABCMeta):
    """Interface of a parameter store object.  ParameterStores are responsible for persisting parameter values
    and determining parameter equality.
    """

    @abstractmethod
    def parameter_keys(self, key):
        """Get the parameter sub-keys for the given generator key

        Must be overridden by subclasses.

        :param key: Generator key
        :return: list of key
        """
        pass

    @abstractmethod
    def compare(self, value, parameter_key):
        """Compare the stored value to the given value

        Must be overridden by subclasses.

        :param value: value comparable to stored value
        :param parameter_key: key of value to compare to
        :return: equality test
        """
        pass

    @abstractmethod
    def update(self, key, value, parameter_keys=None):
        """ Store new value for the paramater.

        Must be overridden by subclasses.

        :param key:key to of object to store
        :param value: value of object to store
        :param parameter_keys: keys of parameters for generator parameter values
        :return:
        """
        pass

