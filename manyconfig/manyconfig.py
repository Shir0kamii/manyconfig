from manyconfig import Config


def merge(*configs):
    d = {}
    for conf in configs:
        d.update(conf)
    return d


class ManyConfig(Config):

    def __init__(self, *metaconfigs, **kwargs):
        self.metaconfigs = metaconfigs
        super(ManyConfig, self).__init__(**kwargs)

    def _load(self):
        return merge(*[mc.load() for mc in reversed(self.metaconfigs)])
