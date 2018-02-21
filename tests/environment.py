from manyconfig import EnvironmentMetaConfig

from tests.conftest import tmp_env


class test_namespace():
    metaconfig = EnvironmentMetaConfig("FOO_")
    with tmp_env(**{"FOO_FOO": "1", "FOO_BAR": "2", "FOO_BAZ": "3"}):
        config = metaconfig.load()
    assert config == {"foo": "1", "bar": "2", "baz": "3"}
