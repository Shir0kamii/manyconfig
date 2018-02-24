import json

import pytest

from manyconfig import FileMetaConfig
from manyconfig.file import InvalidFormatError


def test_invalid_format():
    with pytest.raises(InvalidFormatError):
        FileMetaConfig("foo", str())


def test_json(tmpdir):
    d = {"foo": 42, "bar": "Olive&Tom"}
    f = tmpdir.join("foo.json")
    s = json.dumps(d)
    f.write(s)
    metaconfig = FileMetaConfig("json", str(f))
    assert metaconfig.load() == d


ini_text = """[foo]
bar = baz
foo = bar
baz = foo
"""


def test_ini(tmpdir):
    f = tmpdir.join("foo.ini")
    f.write(ini_text)
    metaconfig = FileMetaConfig("ini", str(f))
    assert metaconfig.load() == {"foo": {"bar": "baz", "foo": "bar",
                                         "baz": "foo"}}
