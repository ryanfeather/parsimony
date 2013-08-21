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
import os
STRING1 = "A STRING ONE"
STRING2 = "TWO DUCKS WALK INTO A BAR"
PARAM_VAL1 = 5
PARAM_VAL2 = 6
DATA_FILE_NAME_1 = 'datafile1.txt'
RESULT1 = 'FOO'
RESULT2 = 'BAR'
RESULT3 = 'BAZ'
RESULT4 = 'BIF'
RESULT5 = 'DUCK'

def createDataFile(filename,content):
    with open(filename,'w') as  fileToCreate:
        fileToCreate.write(content)

def readDataFile(filename):
    with open(filename,'r') as  fileToRead:
        content = fileToRead.readlines()
    return content


def destroyDataFile(filename):
    os.remove(filename)

_call_count = 0
def reset():
    global _call_count
    _call_count = 0
          
class MockGenerationProcess(object):
    
    def __init__(self):
        pass
    
    def get_call_count(self):
        global _call_count
        return _call_count
    
    def __call__(self,key_param,param = None):
        
        if key_param == STRING1 and param is None:
            value = RESULT1
        elif key_param == STRING2 and param is None:
            value = RESULT2
        elif key_param == STRING1 and param == PARAM_VAL1:
            value = RESULT3
        elif key_param == STRING2 and param == PARAM_VAL1:
            value = RESULT4
        elif key_param == STRING2 and param == PARAM_VAL2:
            value = RESULT5
        else:
            raise Exception('Invalid key_param to MockGenerationProcess functor '+str(key_param))  
        global _call_count
    
        _call_count += 1
        
        return value
        
       
    