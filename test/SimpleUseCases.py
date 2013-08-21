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
import os
import time
import shutil

class SimpleUseCasesTest(unittest.TestCase):
    
    def setUp(self):
        self.mock = TestEvaluationUtils.MockGenerationProcess()
        TestEvaluationUtils.createDataFile(TestEvaluationUtils.DATA_FILE_NAME_1,TestEvaluationUtils.STRING1)
        
    def tearDown(self):
        TestEvaluationUtils.destroyDataFile(TestEvaluationUtils.DATA_FILE_NAME_1)
        try:
            shutil.rmtree('.parsimony')
        except:
            #do nothing, file might not have been created
            pass
        TestEvaluationUtils.reset()
        
    def test_generate_from_file(self):
        access_time0 = os.stat(TestEvaluationUtils.DATA_FILE_NAME_1).st_atime
        source_file = parsimony.generators.TextFile('text',TestEvaluationUtils.DATA_FILE_NAME_1)
        time.sleep(0.01)# sleep to make sure there is some measureable time between accesses - computers are fast
        result = source_file.generate()
        access_time1 = os.stat(TestEvaluationUtils.DATA_FILE_NAME_1).st_atime
        self.assertGreater(access_time1, access_time0)
        self.assertEqual(TestEvaluationUtils.STRING1, result)
        time.sleep(0.01)
        result = source_file.generate()
        access_time2 = os.stat(TestEvaluationUtils.DATA_FILE_NAME_1).st_atime
        self.assertEqual(access_time1, access_time2)
          
        self.assertEqual(TestEvaluationUtils.STRING1, result)
  
        TestEvaluationUtils.createDataFile(TestEvaluationUtils.DATA_FILE_NAME_1,TestEvaluationUtils.STRING2)
        time.sleep(0.01)
        result = source_file.generate()
        access_time3 = os.stat(TestEvaluationUtils.DATA_FILE_NAME_1).st_atime
        self.assertGreater(access_time3, access_time2)
          
        self.assertEqual(TestEvaluationUtils.STRING2, result)
        
        
    
    def test_generate_from_parameters(self):
        result = parsimony.generate('test_result',self.mock,key_param=TestEvaluationUtils.STRING1)
        self.assertEqual(TestEvaluationUtils.RESULT1, result)
        self.assertEqual(1, self.mock.get_call_count())
        result = parsimony.generate('test_result',self.mock,key_param=TestEvaluationUtils.STRING1)
        self.assertEqual(TestEvaluationUtils.RESULT1, result)
        self.assertEqual(1, self.mock.get_call_count())
         
        result = parsimony.generate('test_result',self.mock,key_param=TestEvaluationUtils.STRING2)
        self.assertEqual(TestEvaluationUtils.RESULT2, result)
        self.assertEqual(2, self.mock.get_call_count())
        #make sure that the state has been updated to expect result2
        result = parsimony.generate('test_result',self.mock,key_param=TestEvaluationUtils.STRING2)
        self.assertEqual(TestEvaluationUtils.RESULT2, result)
        self.assertEqual(2, self.mock.get_call_count())
#     
    def test_generate_from_file_and_parameters(self):
        sourceFile = parsimony.generators.TextFile('text',TestEvaluationUtils.DATA_FILE_NAME_1)
        result = parsimony.generate('test_result_mixed',self.mock,key_param=sourceFile,param=TestEvaluationUtils.PARAM_VAL1)
        self.assertEqual(TestEvaluationUtils.RESULT3, result)
        self.assertEqual(1, self.mock.get_call_count())
        result = parsimony.generate('test_result_mixed',self.mock,key_param=sourceFile,param=TestEvaluationUtils.PARAM_VAL1)
        self.assertEqual(TestEvaluationUtils.RESULT3, result)
        self.assertEqual(1, self.mock.get_call_count())
        time.sleep(0.01)# sleep to make sure there is some measureable time between accesses - computers are fast
        TestEvaluationUtils.createDataFile(TestEvaluationUtils.DATA_FILE_NAME_1,TestEvaluationUtils.STRING2)
        result = parsimony.generate('test_result_mixed',self.mock,key_param=sourceFile,param=TestEvaluationUtils.PARAM_VAL1)
        self.assertEqual(TestEvaluationUtils.RESULT4, result)
        self.assertEqual(2, self.mock.get_call_count())
        #make sure we update on a change of parameters
        result = parsimony.generate('test_result_mixed',self.mock,key_param=sourceFile)
        self.assertEqual(TestEvaluationUtils.RESULT2, result)
        self.assertEqual(3, self.mock.get_call_count())
        
        result = parsimony.generate('test_result_mixed',self.mock,key_param=sourceFile,param=TestEvaluationUtils.PARAM_VAL2)
        self.assertEqual(TestEvaluationUtils.RESULT5, result)
        self.assertEqual(4, self.mock.get_call_count())
        
    
    
if __name__ == '__main__':
    unittest.main()