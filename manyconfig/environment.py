import os

from manyconfig import Config


class EnvironmentConfig(Config):

    def __init__(self, namespace, **kwargs):
        self.namespace = namespace
        super(EnvironmentConfig, self).__init__(**kwargs)

    def _load(self):
        ns_len = len(self.namespace)
        return {key[ns_len:].lower(): value
                for key, value in os.environ.items()
                if key.startswith(self.namespace)}
