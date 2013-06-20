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
            
class MockGenerationProcess(object):
    
    def __init__(self):
        self.call_count = 0
        
    
    def __call__(self,key,param = None):
        if key == STRING1 and param is None:
            value = RESULT1
        elif key == STRING2 and param is None:
            value = RESULT2
        elif key == STRING1 and param == PARAM_VAL1:
            value = RESULT3
        elif key == STRING2 and param == PARAM_VAL1:
            value = RESULT4
        elif key == STRING2 and param == PARAM_VAL2:
            value = RESULT5
        else:
            raise Exception('Invalid key to MockGenerationProcess functor '+str(key))  
        self.call_count += 1
        
        return value
        
       
    