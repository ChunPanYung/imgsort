from util import sizeof_fmt
import os
import subprocess
import pytest

@pytest.fixture(autouse=True)
def before_tests():
    return True

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_size_of_fmt():
    file_path: str = '/tmp/RAM/tests.1M'
    subprocess.run(["fallocate", "--length", "1M", file_path])
    assert sizeof_fmt(os.path.getsize(file_path)) == '1.0MB'

@pytest.fixture(autouse=True)
def after_tests():
    return True
