import pytest

from marshmallow import Schema

from manyconfig import Config, InvalidConfigException


@pytest.fixture
def config_dict():
    return {"foo": "wow", "bar": "42"}


@pytest.fixture()
def TestConfig(Schema, config_dict):

    class TestConfig(Config):
        schema = Schema()

        def _load(self):
            return config_dict

    return TestConfig


def test_schema_loading(TestConfig):
    """Test that schema.load is used

    See the bar string become an integer
    """
    metaconfig = TestConfig()
    config = metaconfig._load()
    assert not isinstance(config["bar"], int)
    config = metaconfig.load()
    assert isinstance(config["bar"], int)


def test_schema_overide(TestConfig):
    class OtherSchema(Schema):
        pass

    schema = OtherSchema()
    metaconfig = TestConfig(schema=schema)
    assert metaconfig.schema is schema


@pytest.mark.parametrize("config_dict", [{"foo": 4}])
def test_schema_loading_error(TestConfig):
    """Test that schema.load raise an error if the config is not valid"""
    metaconfig = TestConfig()
    with pytest.raises(InvalidConfigException):
        metaconfig.load()


@pytest.mark.parametrize("config_dict", [{"foo": 4}])
def test_schema_loading_silent_error(TestConfig):
    """Test that schema.load raise an error if the config is not valid"""
    metaconfig = TestConfig(silent=True)
    config = metaconfig.load()
    assert config == {}
