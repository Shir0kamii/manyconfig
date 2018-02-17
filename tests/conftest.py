import os
import sys

sys.path.insert(0, os.curdir)

import pytest

from marshmallow import Schema
from marshmallow.fields import String, Integer


@pytest.fixture(scope="session")
def schema():
    class schema(Schema):
        foo = String(required=True)
        bar = Integer()

    return schema
