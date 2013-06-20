'''
Copyright (c) 2013 Ryan Feather

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
#tests to run
#1. Based on some data file, generate some result.  Verify expected result.
#2. Perform step 1 again.  Verify that intermediate result was not regenerated. Verify result is the same.
#3. Perform step 1.  Change the file. Verify result is regenerated and correct.
# Repeat these steps, but change a parameter instead.

import unittest
import TestEvaluationUtils
import parsimony

class SimpleUseCasesTest(unittest.TestCase):
    
    def setUp(self):
        self.mock = TestEvaluationUtils.MockGenerationProcess()
        TestEvaluationUtils.createDataFile(TestEvaluationUtils.DATA_FILE_NAME_1,TestEvaluationUtils.STRING1)
    
    def tearDown(self):
        TestEvaluationUtils.destroyDataFile(TestEvaluationUtils.DATA_FILE_NAME_1)
        
    def test_generate_from_file(self):
        sourceFile = parsimony.TextFile(TestEvaluationUtils.DATA_FILE_NAME_1)
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile})
        self.assertEqual(TestEvaluationUtils.RESULT1, result)
        self.assertEqual(1, self.mock.call_count)
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile})
        self.assertEqual(TestEvaluationUtils.RESULT1, result)
        self.assertEqual(1, self.mock.call_count)
        
        TestEvaluationUtils.createDataFile(TestEvaluationUtils.DATA_FILE_NAME_1,TestEvaluationUtils.STRING2)
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile})
        self.assertEqual(TestEvaluationUtils.RESULT2, result)
        self.assertEqual(2, self.mock.call_count)
        #the intention is to make sure that the state has been in fact updated to 'expect' the file's second contents
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile})
        self.assertEqual(TestEvaluationUtils.RESULT2, result)
        self.assertEqual(2, self.mock.call_count)
        
    
    def test_generate_from_parameters(self):
        result = parsimony.generate('test_result',self.mock,{'key':TestEvaluationUtils.STRING1})
        self.assertEqual(TestEvaluationUtils.RESULT1, result)
        self.assertEqual(1, self.mock.call_count)
        result = parsimony.generate('test_result',self.mock,{'key':TestEvaluationUtils.STRING1})
        self.assertEqual(TestEvaluationUtils.RESULT1, result)
        self.assertEqual(1, self.mock.call_count)
        
        result = parsimony.generate('test_result',self.mock,{'key':TestEvaluationUtils.STRING2})
        self.assertEqual(TestEvaluationUtils.RESULT2, result)
        self.assertEqual(2, self.mock.call_count)
        #make sure that the state has been updated to expect result2
        result = parsimony.generate('test_result',self.mock,{'key':TestEvaluationUtils.STRING2})
        self.assertEqual(TestEvaluationUtils.RESULT2, result)
        self.assertEqual(2, self.mock.call_count)
    
    def test_generate_from_file_and_parameters(self):
        sourceFile = parsimony.TextFile(TestEvaluationUtils.DATA_FILE_NAME_1)
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile,'param':TestEvaluationUtils.PARAM_VAL1})
        self.assertEqual(TestEvaluationUtils.RESULT3, result)
        self.assertEqual(1, self.mock.call_count)
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile,'param':TestEvaluationUtils.PARAM_VAL1})
        self.assertEqual(TestEvaluationUtils.RESULT3, result)
        self.assertEqual(1, self.mock.call_count)
        
        TestEvaluationUtils.createDataFile(TestEvaluationUtils.DATA_FILE_NAME_1,TestEvaluationUtils.STRING2)
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile,'param':TestEvaluationUtils.PARAM_VAL1})
        self.assertEqual(TestEvaluationUtils.RESULT4, result)
        self.assertEqual(2, self.mock.call_count)
        #the intention is to make sure that the state has been in fact updated to 'expect' the file's second contents
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile})
        self.assertEqual(TestEvaluationUtils.RESULT4, result)
        self.assertEqual(2, self.mock.call_count)
        
        result = parsimony.generate('test_result',self.mock,{'key':sourceFile,'param':TestEvaluationUtils.PARAM_VAL2})
        self.assertEqual(TestEvaluationUtils.RESULT5, result)
        self.assertEqual(3, self.mock.call_count)
        
    
    
if __name__ == '__main__':
    unittest.main()