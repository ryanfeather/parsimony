"""
This module contains routines to fetch the default or configured implementations of
various parsimony base objects. Currently, these objects are all singletons and lazily initialized.
"""
import os
import importlib

STORE  = 'store' #key for store class 
CACHE  = 'cache' #key for cache class
CACHE_STORE = 'cache_store' #key for cache store class
CACHE_KEY = 'cache_key' #key for cache key
OBFUSCATOR = 'obfuscator' #key for obfuscator instance
DIRECTORY = 'directory' #key for parsimony directory
CONTEXT_NAME = 'context' #key for context name
CALLABLE_WRAPPER = 'callable_wrapper' #key for callable wrapper class

__configuration = {}
__stores = {}


def set_configuration_file(config_file):
    """ Extract a config based on the contents of a python file. The file should contain a dict named
    parsimony_configuration with keys from this module.
    
    :param config_file:  path to this module
    """
    
    module_name, extension = os.path.splitext(config_file)
    
    config_module = importlib.import_module(module_name)
    
    update_configuration(**config_module.parsimony_configuration)
    
def update_key(key,config_dict):
    #update a single key
    global __configuration
    if key in config_dict:
        __configuration[key] = config_dict[key]
        
def update_configuration(**config_dict):
    """Update the configuration based on key values.  See this module's documentation for appropriate key values."""
    global __configuration
    update_key(DIRECTORY,config_dict) #order matters
    update_key(CONTEXT_NAME,config_dict)
    update_key(OBFUSCATOR,config_dict)
    update_key(STORE,config_dict)
    update_key(CACHE_KEY,config_dict)    
    update_key(CACHE_STORE,config_dict)
    update_key(CACHE,config_dict)
    update_key(CALLABLE_WRAPPER,config_dict)

def store(key):
    """Gets the configured default store. The default is PickleStore

    :return store: Store object
    """
    global __stores
    if __stores is None:
        __stores = {}

    if key not in __stores:
        __stores[key] = __configuration[STORE](key)

    return __stores[key]

__cache_instance  = None
def cache():
    """Returns the configured cache.  Currently, a default of MemCache is returned

    :return:
    """
    
    global __cache_instance
    if __cache_instance is None:
        cache_key = __configuration[CACHE_KEY]
        if CACHE_STORE in __configuration:
            store = __configuration[CACHE_STORE]
        else:
            store = __configuration[STORE]
        __cache_instance = __configuration[CACHE](store(cache_key))
            
    return __cache_instance

__obfuscator = None

def obfuscator():
    """Gets the configured obfuscator. Currently, a default of SHA512Obfuscator is chosen.

    :return obfuscator: Obfuscator object
    """
    
    global __obfuscator
    if __obfuscator is None:
        __obfuscator = __configuration[OBFUSCATOR]() 
    return __obfuscator


def parsimony_directory():
    """Return the directory to store parsimony data in.

    :return: .parsimony
    """
    directory_path = __configuration[DIRECTORY]
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    return directory_path

def context_name():
    """Get the context name

    :return: Current context name
    """
    return __configuration[CONTEXT_NAME]


def set_context(new_context_name):
    """Set the context name. This should be something that can be a directory name.
    """
    update_configuration(**{CONTEXT_NAME:new_context_name})

def callable_wrapper(key, function, **parameters):
    """Gets the configured call wrapper. Currently, a default of PickledCallableWrapper is chosen.

    :return callable_wrapper: CallableWrapper Generator object
    """

    return __configuration[CALLABLE_WRAPPER](key, function, **parameters)

def reset():
    """Set the configuration back to the default state. Useful for testing."""
    global __stores
    global __cache_instance
    global __obfuscator
    __stores = None
    __cache_instance = None
    __obfuscator = None