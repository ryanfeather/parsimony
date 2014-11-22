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
from parsimony.generators import Generator

import os.path


class TextFile(Generator):
    """
    classdocs
    """


    def __init__(self, key, file_path):
        """
        Constructor
        """
        self._modtime = None
        super(TextFile, self).__init__(key, file_path=file_path)


    def up_to_date(self):
        new_mod_time = os.path.getmtime(self.get_parameter('file_path'))
        return new_mod_time == self._modtime

    def rebuild(self):
        return self.load()

    def load(self):
        with open(self.get_parameter('file_path'), 'r') as file_handle:
            contents = file_handle.read()
        self._modtime = os.path.getmtime(self.get_parameter('file_path'))

        return contents
