from abc import ABCMeta, abstractmethod


class Cache(metaclass=ABCMeta):
    """Interface of a Cache object.  Cache's are responsible for persisting parameter values
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
        """ Store new value for the parameter.

        Must be overridden by subclasses.

        :param key: key  of object to store
        :param value: value of object to store
        :param parameter_keys: keys of parameters for generator parameter values
   
        """
        pass

    @abstractmethod
    def __contains__(self, key):
        """Needed for testing via in operator

        :param key:
        :return: if parameter is in this store
        """
        pass

    @abstractmethod
    def __delitem__(self, key):
        """ Used to implement a del index operator.

        Must be overriden by subclasses.
        Example: del mycache['gen_key']
        This removes the item from all levels of the cache.

        :param key: key to clear from the cache
        """