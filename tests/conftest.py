import contextlib
import os
import sys

import pytest

from marshmallow import Schema as _Schema
from marshmallow.fields import String, Integer

sys.path.insert(0, os.curdir)


@pytest.fixture(scope="session")
def Schema():
    class schema(_Schema):
        foo = String(required=True)
        bar = Integer()

    return schema


@contextlib.contextmanager
def tmp_env(**env):
    old = {key: os.environ[key] for key in env.keys() if key in os.environ}
    to_remove = [key for key in env.keys() if key not in os.environ]
    os.environ.update(env)
    yield os.environ
    os.environ.update(old)
    for key in to_remove:
        os.environ.pop(key)
