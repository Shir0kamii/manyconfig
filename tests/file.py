import json

from manyconfig import JSONMetaConfig


def test_json(tmpdir):
    d = {"foo": 42, "bar": "Olive&Tom"}
    f = tmpdir.join("foo.json")
    s = json.dumps(d)
    f.write(s)
    metaconfig = JSONMetaConfig(str(f))
    assert metaconfig.load() == d
