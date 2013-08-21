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
import parsimony
import os

__store = None
#TODO, move any directory creation or other initialization into the configurable objects
def get_store():
    global __store
    if not os.path.exists('.parsimony'):
        os.makedirs('.parsimony')
    if __store is None:
        __store = parsimony.persistence.PickledParameterStore('.parsimony/p_store') 
    return __store

__obfuscator = None
def get_obfuscator():
    
    global __obfuscator
    if __obfuscator is None:
        __obfuscator = parsimony.persistence.SHA512Obfuscator() 
    return __obfuscator

def get_callable_wrapper(key,function,**parameters):
    if not os.path.exists('.parsimony/wrapped_results'):
    
        os.makedirs('.parsimony/wrapped_results')

    return parsimony.generators.PickledCallableWrapper('.parsimony/wrapped_results',key,function,**parameters)