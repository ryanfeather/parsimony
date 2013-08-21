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
from parsimony.generators.Generator import Generator
import cPickle
import os
import string

class PickledCallableWrapper(Generator):
    
    def __init__(self,directory,key,function,**parameters):
        self._function = function #keep separate references to avoid copying later
        self._param_keys = parameters.keys() 
        self._store_location = self._generate_store_location(directory, key)
        super(PickledCallableWrapper, self).__init__(key,function=function,**parameters)

    def up_to_date(self):
        #always return True - the framework will take care of updates due to parameter or function changes
        return True  
    
    def rebuild(self):
        #retrieve generated parameters
        params = {key: self.get_parameter(key) for key in self._param_keys}
        return self._function(**params)
            
    def load(self):
        
        with open(self._store_location,'r') as result_file:
            result = cPickle.load(result_file)
        return result
    
    def store(self,value):
        
        with open(self._store_location,'w') as result_file:
            cPickle.dump(value,result_file)
        
    
    def _generate_store_location(self,directory,key):
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        file_name = ''.join(c if c in valid_chars else '_' for c in key)
        return os.path.join(directory,file_name)