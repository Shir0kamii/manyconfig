import os

from manyconfig import EnvironmentConfig


class test_namespace():
    os.environ.update({"FOO_FOO": "1", "FOO_BAR": "2", "FOO_BAZ": "3"})
    metaconfig = EnvironmentConfig("FOO_")
    config = metaconfig.load()
    assert config == {"foo": "1", "bar": "2", "baz": "3"}
