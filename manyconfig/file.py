import json
try:
    from configparser import ConfigParser
except ImportError:  # pragma: no cover
    from ConfigParser import ConfigParser

from manyconfig import MetaConfig


class InvalidFormatError(ValueError):
    pass


class DecoratorDict(dict):
    def add(self, key):
        def decorator(f):
            self[key] = f
            return f
        return decorator


format_parsers = DecoratorDict({"json": json.load})


class FileMetaConfig(MetaConfig):
    """Pull configuration from a file.

    :param filepath: the path of the configuration file.
    :param bool binary: Open the file in binary mode.
    """

    def __init__(self, format, filepath, binary=False, **kwargs):
        if format not in format_parsers.keys():
            raise InvalidFormatError("format not supported")
        self.format = format
        self.filepath = filepath
        self.mode = 'rb' if binary else 'r'
        super(FileMetaConfig, self).__init__(**kwargs)

    def _load(self):
        """Open the given file and call the adapted parser."""
        parser = format_parsers.get(self.format)
        with open(self.filepath, mode=self.mode) as file_object:
            config = parser(file_object)
        return config


@format_parsers.add("ini")
def parse_ini(file_object):
    """Parse the INI in the file."""
    config_parser = ConfigParser()
    config_parser.readfp(file_object)
    return {section: dict(config_parser.items(section))
            for section in config_parser.sections()}
