import pytest

from pathlib import Path

from {{package_name}}.cli import main

def test_main():
    assert main() == -1
