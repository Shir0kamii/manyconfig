from manyconfig import Config


def test_schema_loading(schema):
    """Test that schema.load is used

    See the bar string become an integer
    """
    class TestConfig(Config):
        def _load(self):
            return {"foo": "wow", "bar": "42"}

    metaconfig = TestConfig(schema=schema())
    config = metaconfig.load()
    assert config.get("bar") == 42
