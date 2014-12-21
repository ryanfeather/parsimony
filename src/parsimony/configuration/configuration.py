"""
This module contains routines to fetch the default or configured implementations of
various parsimony base objects. Currently, these objects are all singletons and lazily initialized.
"""
import parsimony
import os


__stores = {}


def store(key):
    """Gets the configured default store. Currently, a default of PickledStore is chosen.

    :return store: Store object
    """
    global __stores
    if __stores is None:
        __stores = {}

    if key not in __stores:
        __stores[key] = parsimony.persistence.PickleStore(key)

    return __stores[key]


__cache = None


def cache():
    """Returns the configured cache.  Currently, a default of MemCache is returned

    :return:
    """
    global __cache
    if __cache is None:
        __cache = parsimony.persistence.MemCache(parsimony.persistence.PickleStore('p_store'))
    return __cache


__obfuscator = None


def obfuscator():
    """Gets the configured obfuscator. Currently, a default of SHA512Obfuscator is chosen.

    :return obfuscator: Obfuscator object
    """

    global __obfuscator
    if __obfuscator is None:
        __obfuscator = parsimony.persistence.SHA512Obfuscator()
    return __obfuscator


def parsimony_directory():
    """Return the directory to store parsimony data in.

    :return: .parsimony
    """
    directory_path = '.parsimony'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    return directory_path

__context_name = 'Default'


def context_name():
    """Get the context name

    :return: Current context name
    """
    global __context_name
    return __context_name


def set_context(new_context_name):
    """Set the context name. This should be something that can be a directory name.
    """
    global __context_name
    __context_name = new_context_name


def callable_wrapper(key, function, **parameters):
    """Gets the configured call wrapper. Currently, a default of PickledCallableWrapper is chosen.

    :return callable_wrapper: CallableWrapper Generator object
    """

    return parsimony.generators.StoredCallableWrapper(key, function, **parameters)

def reset():
    """Set the configuration back to the default state. Useful for testing."""
    global __context_name
    global __stores
    global __cache
    global __obfuscator
    __context_name = "Default"
    __stores = None
    __cache = None
    __obfuscator = None