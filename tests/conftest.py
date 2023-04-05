"""Put pytest fixtures here to be used by multiple test files"""
from typing import Generator
import pytest
from fair_python_package_template.example_class1 import ExampleClass1


@pytest.fixture(scope="session", name="example_class1")
def fixture_example_class1() -> Generator:
    """
    Yields an ExampleClass1
    """
    obj = ExampleClass1("string1", 1)
    yield obj
