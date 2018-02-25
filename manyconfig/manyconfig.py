from .config import MetaConfig, InvalidConfigException


def merge(*configs):
    """Merge several dicts to produce one.

    If a key is present in two or more dicts, the value of the lattest
    occurence is took.
    """
    d = {}
    for conf in configs:
        d.update(conf)
    return d


class ManyConfig(MetaConfig):
    """Pull configuration from many others.

    This class is the real plus-value of ManyConfig. It takes some
    configuration sources, load them and merge them in a single configuration.

    Configurations are loaded in the given order, and new values for the same
    configuration key overrides older ones.

    This allow implementation of Bash-like configurations, where multiple files
    are read and each one take precedence over the last one.

    :param metaconfigs: A list of configurations to pull values from
    """

    def __init__(self, *metaconfigs, **kwargs):
        self.metaconfigs = metaconfigs
        super(ManyConfig, self).__init__(**kwargs)

    def _load(self):
        return merge(*[mc.load() for mc in self.metaconfigs])


class AnyConfig(ManyConfig):
    """Pull configuration from the first existing source

    It will iter through the different MetaConfig given and yield the first
    non-empty valid configuration.

    :param metaconfigs: A list of configurations to pull values from
    """

    def _load(self):
        for metaconfig in self.metaconfigs:
            config = metaconfig.load()
            if config:
                return config
