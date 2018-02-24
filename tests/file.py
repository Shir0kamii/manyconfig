import json

from manyconfig import INIMetaConfig, JSONMetaConfig


def test_json(tmpdir):
    d = {"foo": 42, "bar": "Olive&Tom"}
    f = tmpdir.join("foo.json")
    s = json.dumps(d)
    f.write(s)
    metaconfig = JSONMetaConfig(str(f))
    assert metaconfig.load() == d


ini_text = """[foo]
bar = baz
foo = bar
baz = foo
"""


def test_ini(tmpdir):
    f = tmpdir.join("foo.ini")
    f.write(ini_text)
    metaconfig = INIMetaConfig(str(f))
    assert metaconfig.load() == {"foo": {"bar": "baz", "foo": "bar",
                                         "baz": "foo"}}
