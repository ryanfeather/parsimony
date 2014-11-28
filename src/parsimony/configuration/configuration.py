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


def callable_wrapper(key, function, **parameters):
    """Gets the configured call wrapper. Currently, a default of PickledCallableWrapper is chosen.

    :return callable_wrapper: CallableWrapper Generator object
    """
    if not os.path.exists('.parsimony/wrapped_results'):
        os.makedirs('.parsimony/wrapped_results')

    return parsimony.generators.PickledCallableWrapper('.parsimony/wrapped_results', key, function, **parameters)