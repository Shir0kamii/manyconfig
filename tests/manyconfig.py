from manyconfig import EnvironmentMetaConfig
from manyconfig.manyconfig import merge, ManyConfig, AnyConfig

from tests.conftest import tmp_env


def test_merge():
    d1 = {"foo": 1, "bar": 1}
    d2 = {"foo": 2}
    assert merge(d1, d2) == {"foo": 2, "bar": 1}


def test_ManyConfig():
    env1 = EnvironmentMetaConfig("FOO_")
    env2 = EnvironmentMetaConfig("BAR_")
    metaconfig = ManyConfig(env1, env2)
    with tmp_env(FOO_FOO="1", FOO_BAR="1", BAR_FOO="2", BAR_BAZ="2"):
        assert metaconfig.load() == {"foo": "2", "bar": "1", "baz": "2"}


def test_AnyConfig():
    env1 = EnvironmentMetaConfig("FOO_")
    env2 = EnvironmentMetaConfig("BAR_")
    env3 = EnvironmentMetaConfig("BAZ_")
    metaconfig = AnyConfig(env1, env2, env3)
    with tmp_env(BAR_FOO="2", BAZ_BAR="3"):
        assert metaconfig.load() == {"foo": "2"}
