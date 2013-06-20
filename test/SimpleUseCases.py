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
#1. Based on some data file, generate a result based on that file.  Verify expected result.
#2. Perform step 1 again.  Verify that intermediate result was not regenerated. Verify result is the same.
#3. Perform step 1.  Change the file. Verify result is regenerated and correct.
# Repeat these steps, but change a parameter instead.

import unittest
from CacheToolsEvaluationUtils import *

class SimpleUseCasesTest(unittest.TestCase):
    
    def setUp(self):
        self.mock = CacheToolMockProcess()
    
    def testGenerateFromFile(self):
        pass
    
    def testGenerateFromParameters(self):
        pass
    
    def testGenerateFromFileAndParameters(self):
        pass
    
    
if __name__ == '__main__':
    unittest.main()