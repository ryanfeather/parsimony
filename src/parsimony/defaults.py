from parsimony import configuration,persistence,generators

def set_defaults():
    """Set the default configuartion"""
    
    configuration.update_configuration(**{configuration.STORE:persistence.PickleStore,\
        configuration.CACHE:persistence.MemCache,\
        configuration.CACHE_KEY:'p_store',\
        configuration.OBFUSCATOR:persistence.SHA512Obfuscator,\
        configuration.DIRECTORY:'.parsimony',\
        configuration.CONTEXT_NAME:'Default',\
        configuration.CALLABLE_WRAPPER:generators.StoredCallableWrapper})