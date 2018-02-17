import json

from manyconfig import JSONConfig


def test_json(tmpdir):
    d = {"foo": 42, "bar": "Olive&Tom"}
    f = tmpdir.join("foo.json")
    s = json.dumps(d)
    f.write(s)
    metaconfig = JSONConfig(str(f))
    assert metaconfig.load() == d
