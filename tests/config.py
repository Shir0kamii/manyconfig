import pytest

from marshmallow import Schema

from manyconfig import MetaConfig, InvalidConfigException


@pytest.fixture
def config_dict():
    return {"foo": "wow", "bar": "42"}


@pytest.fixture()
def TestMetaConfig(Schema, config_dict):

    class TestMetaConfig(MetaConfig):
        schema = Schema()

        def _load(self):
            return config_dict

    return TestMetaConfig


def test_schema_loading(TestMetaConfig):
    """Test that schema.load is used

    See the bar string become an integer
    """
    metaconfig = TestMetaConfig()
    config = metaconfig._load()
    assert not isinstance(config["bar"], int)
    config = metaconfig.load()
    assert isinstance(config["bar"], int)


def test_schema_overide(TestMetaConfig):
    class OtherSchema(Schema):
        pass

    schema = OtherSchema()
    metaconfig = TestMetaConfig(schema=schema)
    assert metaconfig.schema is schema


@pytest.mark.parametrize("config_dict", [{"foo": 4}])
def test_schema_loading_error(TestMetaConfig):
    """Test that schema.load raise an error if the config is not valid"""
    metaconfig = TestMetaConfig()
    with pytest.raises(InvalidConfigException):
        metaconfig.load()


@pytest.mark.parametrize("config_dict", [{"foo": 4}])
def test_schema_loading_silent_error(TestMetaConfig):
    """Test that schema.load raise an error if the config is not valid"""
    metaconfig = TestMetaConfig(silent=True)
    config = metaconfig.load()
    assert config == {}
