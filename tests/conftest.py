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
