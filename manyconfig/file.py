import json
try:
    from configparser import ConfigParser
except ImportError:  # pragma: no cover
    from ConfigParser import ConfigParser

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


class INIMetaConfig(FileMetaConfig):
    """Pull configuration from an INI file."""

    def __init__(self, *args, **kwargs):
        config_parser = kwargs.pop("config_parser", None)
        if not config_parser:
            config_parser = ConfigParser()
        self.config_parser = config_parser
        super(INIMetaConfig, self).__init__(*args, **kwargs)

    def parse(self, file_object):
        """Parse the INI in the file."""
        self.config_parser.readfp(file_object)
        return {section: dict(self.config_parser.items(section))
                for section in self.config_parser.sections()}
