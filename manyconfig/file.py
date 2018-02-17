import json

from manyconfig import Config


class FileConfig(Config):

    def __init__(self, filepath, binary=False, **kwargs):
        self.filepath = filepath
        self.mode = 'rb' if binary else 'r'
        super(FileConfig, self).__init__(**kwargs)

    def _load(self):
        with open(self.filepath, mode=self.mode) as file_object:
            return self.parse(file_object)

    def parse(self, file_object):  # pragma: no cover
        pass


class JSONConfig(FileConfig):

    def parse(self, file_object):
        return json.load(file_object)
