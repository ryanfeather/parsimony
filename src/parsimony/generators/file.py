from parsimony.generators import Generator
from parsimony import ParsimonyException

import os.path


class PathMonitor(Generator):
    """Monitors the path for changes. This is primarily useful as a parameter key

    """
    def __init__(self, key, file_path):
        """

        :param key: generator key
        :param file_path: file to track and generate
        """
        self._modtime = None
        super(PathMonitor, self).__init__(key, file_path=file_path)

    def up_to_date(self):
        """Determines if the file has been modified.

        :return: If file timestamp has changed or not
        """
        new_mod_time = os.path.getmtime(self.get_parameter('file_path'))
        return new_mod_time == self._modtime

    def store(self, value):
        """This is by definition already stored. Do nothing.
        """
        pass

    def rebuild(self):
        """Loads the file data.

        :return: self.load()
        """
        return self.load()

    def load(self):
        """Reads all of the file contents into a string.

        :return: text file contents
        """
        self._modtime = os.path.getmtime(self.get_parameter('file_path'))

        return self.get_parameter('file_path')


class TextFile(Generator):
    """Allows a text file to be treated as a generateable object.

    The mechanism is to load the file once and any time the file has been subsequently modified.
    """

    def __init__(self, key, file_path):
        """

        :param key: generator key
        :param file_path: file to track and generate
        """
        self._file_path_monitor = PathMonitor('text_file_path_monitor', file_path)
        super(TextFile, self).__init__(key, file_path=self._file_path_monitor)

    def up_to_date(self):
        """Determines if the file has been modified.

        :return: If file timestamp has changed or not
        """
        return self._file_path_monitor.up_to_date()

    def rebuild(self):
        """Loads the file data.

        :return: self.load()
        """
        return self.load()

    def load(self):
        """Reads all of the file contents into a string.

        :return: text file contents
        """
        with open(self._file_path_monitor.load(), 'r') as file_handle:
            contents = file_handle.read()

        return contents

    def store(self, value):
        """This is by definition already stored. Do nothing.
        """
        pass




