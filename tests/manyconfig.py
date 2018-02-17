from manyconfig import EnvironmentConfig
from manyconfig.manyconfig import merge, ManyConfig

from test.conftest import tmp_env


def test_merge():
    d1 = {"foo": 1, "bar": 1}
    d2 = {"foo": 2}
    assert merge(d1, d2) == {"foo": 2, "bar": 1}


def test_ManyConfig():
    env1 = EnvironmentConfig("FOO_")
    env2 = EnvironmentConfig("BAR_")
    with tmp_env(FOO_FOO="1", FOO_BAR="1", BAR_FOO="2", BAR_BAZ="2"):
        metaconfig = ManyConfig(env1, env2)
    assert metaconfig.load() == {"foo": "2", "bar": "1", "baz": "2"}
