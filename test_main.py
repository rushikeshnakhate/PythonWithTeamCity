import pytest

from main import increment_by_one


def test_increment_by_one():
    assert increment_by_one(1) == 2
