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
import pickle
from .ObfuscatedParameterStore import ObfuscatedParameterStore

class PickledParameterStore(ObfuscatedParameterStore):
    '''
    classdocs
    '''


    def __init__(self,file_name):
        '''
        Constructor
        '''
        self._file_name = file_name
        try:
            with open(self._file_name,'r') as pickle_file:
                self._store_data = pickle.load(pickle_file)
        except IOError:  #the file didn't exist or is otherwise inaccessible, we have no choice to regenerate
            self._store_data = {}
        super(PickledParameterStore, self).__init__()

    def __contains__(self,key):
        return key in self._store_data
      
    def get_parameter_keys(self,key):
        if key in list(self._store_data.keys()):
            return self._store_data[key]['parameters']
        return {}
    
    def _obfuscated_compare(self,value,parameter_key):
        return value == self._store_data[parameter_key]['value'] 
    
    def _obfuscated_update(self,key,value,parameter_keys=None):
        self._store_data[key] =  {'parameters':parameter_keys,'value':value}
        with open(self._file_name,'wb') as pickle_file:
            pickle.dump(self._store_data, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
        
    
    
    
    
    