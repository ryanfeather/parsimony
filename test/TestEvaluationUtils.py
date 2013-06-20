import os
STRING1 = "A STRING ONE"
STRING2 = "TWO DUCKS WALK INTO A BAR"

def createDataFile(filename,content):
    with open(filename,'w') as  fileToCreate:
        fileToCreate.write(content)

def readDataFile(filename):
    with open(filename,'r') as  fileToRead:
        content = fileToRead.readlines()
    return content

def destroyDataFile(filename):
    os.remove(filename)
            
class CacheToolMockProcess(object):
    
    def __init__(self):
        self.callCount = 0
        
    
    def __call__(self,key):
        if key == STRING1:
            value = 'FOO'
        if key == STRING2:
            value =  'BAR'
        self.callCount += 1
        
        return value
        
        
        
    