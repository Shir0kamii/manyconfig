import json

from manyconfig import MetaConfig


class FileMetaConfig(MetaConfig):
    """Pull configuration from a file.

    :param filepath: the path of the configuration file.
    :param bool binary: Open the file in binary mode.
    """

    def __init__(self, filepath, binary=False, **kwargs):
        self.filepath = filepath
        self.mode = 'rb' if binary else 'r'
        super(FileMetaConfig, self).__init__(**kwargs)

    def _load(self):
        """Open the given file and call the parse abstract method."""
        with open(self.filepath, mode=self.mode) as file_object:
            return self.parse(file_object)

    def parse(self, file_object):  # pragma: no cover
        """Method to implement to parse the file object."""
        pass


class JSONMetaConfig(FileMetaConfig):
    """Pull configuration from a JSON file."""

    def parse(self, file_object):
        """Parse the JSON in the file."""
        return json.load(file_object)
