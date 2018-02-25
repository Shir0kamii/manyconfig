class InvalidConfigException(Exception):
    """Exception raises when a configuration is invalid."""

    def __init__(self, message, errors):
        super(InvalidConfigException, self).__init__(message)
        self.errors = errors


class MetaConfig:
    """Base class for metaconfigurations.

    A schema passed at instantiation override any schema set at level class.

    :param bool silent: Don't raise exceptions on invalid configurations
    :param schema: A marshmallow schema to validate loaded configuration
    """

    #: A marshmallow schema to validate loaded configuration
    schema = None

    def __init__(self, silent=False, schema=None):
        self.silent = silent
        if schema:
            self.schema = schema

    def load(self):
        """Load the configuration

        :return dict: Dict representing the configuration
        """
        data = self._load()
        if self.schema:
            data, errors = self.schema.load(data)
            if errors and self.silent:
                return {}
            elif errors:
                raise InvalidConfigException("Invalid configuration", errors)
        return data

    def _load(self):  # pragma: no cover
        """Method to override to implement actual loading behaviour"""
        pass
