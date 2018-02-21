import os

from manyconfig import MetaConfig


class EnvironmentMetaConfig(MetaConfig):
    """Pull configuration from environment

    An environment variable is considered to be in a namespace if it begins by
    it. That is, FOO_BAR is part of the FOO_ namespace.

    All environment variables of the given namespace will be collected, and the
    namespace removed from its beginning. It is then inserted in the
    configuration with its value.

    :param namespace: The namespace to pull from
    """

    def __init__(self, namespace, **kwargs):
        self.namespace = namespace
        super(EnvironmentMetaConfig, self).__init__(**kwargs)

    def _load(self):
        ns_len = len(self.namespace)
        return {key[ns_len:].lower(): value
                for key, value in os.environ.items()
                if key.startswith(self.namespace)}
