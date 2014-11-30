"""
This module contains routines to fetch the default or configured implementations of
various parsimony base objects. Currently, these objects are all singletons and lazily initialized.
"""
import parsimony
import os

__store = None
# TODO, move any directory creation or other initialization into the configurable objects


def store():
    """Gets the configured parameter store. Currently, a default of PickledParameterStore is chosen.

    :return store: ParameterStore object
    """
    global __store
    if not os.path.exists('.parsimony'):
        os.makedirs('.parsimony')
    if __store is None:
        __store = parsimony.persistence.PickledParameterStore('.parsimony/p_store')
    return __store


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

    return parsimony.generators.PickledCallableWrapper(key, function, **parameters)