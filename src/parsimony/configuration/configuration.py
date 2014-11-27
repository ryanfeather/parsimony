import parsimony
import os

__store = None
# TODO, move any directory creation or other initialization into the configurable objects


def store():
    global __store
    if not os.path.exists('.parsimony'):
        os.makedirs('.parsimony')
    if __store is None:
        __store = parsimony.persistence.PickledParameterStore('.parsimony/p_store')
    return __store


__obfuscator = None


def obfuscator():
    global __obfuscator
    if __obfuscator is None:
        __obfuscator = parsimony.persistence.SHA512Obfuscator()
    return __obfuscator


def callable_wrapper(key, function, **parameters):
    if not os.path.exists('.parsimony/wrapped_results'):
        os.makedirs('.parsimony/wrapped_results')

    return parsimony.generators.PickledCallableWrapper('.parsimony/wrapped_results', key, function, **parameters)