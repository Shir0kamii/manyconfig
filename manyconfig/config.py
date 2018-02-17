class InvalidConfigException(Exception):

    def __init__(self, message, errors):
        super(InvalidConfigException, self).__init__(message)
        self.errors = errors


class Config:
    schema = None

    def __init__(self, silent=True, schema=None):
        self.silent = True
        if schema:
            self.schema = schema

    def load(self):
        data = self._load()
        if self.schema:
            data, errors = self.schema.load(data)
            if errors and self.silent:
                return {}
            elif errors:
                raise InvalidConfigException("Invalid configuration", errors)
        return data

    def _load(self):
        pass
