""" Tests for the dirty/cleaning functionality

"""
import shutil
from test import TestEvaluationUtils
import parsimony

_mock = None


def setup_function(function):
    global _mock
    _mock = TestEvaluationUtils.MockGenerationProcess()
    parsimony.configuration.reset()


def teardown_function(function):
    TestEvaluationUtils.reset()


def test_generate_dirty():
    global _mock
    result = parsimony.generate('test_result', _mock, key_param=TestEvaluationUtils.STRING1)
    assert TestEvaluationUtils.RESULT1 == result
    assert 1 == _mock.get_call_count()

    parsimony.mark_dirty('test_result')
    result = parsimony.generate('test_result', _mock, key_param=TestEvaluationUtils.STRING1)
    assert TestEvaluationUtils.RESULT1 == result
    assert 2 == _mock.get_call_count()

    result = parsimony.generate('test_result', _mock, key_param=TestEvaluationUtils.STRING1)
    assert TestEvaluationUtils.RESULT1 == result
    assert 2 == _mock.get_call_count()
