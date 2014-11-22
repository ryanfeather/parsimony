"""
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
"""
import parsimony
from .parameter_store import ParameterStore


class ObfuscatedParameterStore(ParameterStore):
    """
    classdocs
    """


    def __init__(self):
        """
        Constructor
        """
        self._obfuscator = parsimony.configuration.get_obfuscator()
        super(ObfuscatedParameterStore, self).__init__()

    def compare(self, value, parameter_key):
        obfuscated_value = self._obfuscator.obfuscate(value)
        return self._obfuscated_compare(obfuscated_value, parameter_key)

    def update(self, key, value, parameter_keys=None):
        obfuscated_value = self._obfuscator.obfuscate(value)
        return self._obfuscated_update(key, obfuscated_value, parameter_keys)
