# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:51:19 2015

@author: rfeather
"""

import parsimony


class MockCache(parsimony.persistence.MemCache):
    pass

class MockStore(parsimony.persistence.PickleStore):
    pass


def setup_function(function):
    parsimony.configuration.reset()

def teardown_function(function):
    parsimony.configuration.reset()
    parsimony.set_defaults()

def test_update():
    parsimony.configuration.update_configuration(**{parsimony.configuration.DIRECTORY:'foo'})
    assert(parsimony.configuration.parsimony_directory()=='foo')
    parsimony.configuration.update_configuration(**{parsimony.configuration.CONTEXT_NAME:'goo'})
    assert(parsimony.configuration.context_name()=='goo')
    parsimony.configuration.update_configuration(**{parsimony.configuration.CACHE:MockCache})
    assert(isinstance(parsimony.configuration.cache(),MockCache))