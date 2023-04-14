"""Testing for ExampleClass1"""
from typing import Generator
import pytest
from package.module1.example_class1 import ExampleClass1


@pytest.fixture(scope="session", name="example_class2")
def fixture_example_class2() -> Generator:
    """
    Yields an ExampleClass1
    """
    obj = ExampleClass1("string2", 2)
    yield obj


class TestInstance1:
    """Testing for ExampleClass1, instance 1"""

    def test_method1(self, example_class1: ExampleClass1) -> None:
        "Testing for ExampleClass1.method1"
        assert example_class1.method1() == "string1"

    def test_method2(self, example_class1: ExampleClass1) -> None:
        "Testing for ExampleClass1.method2"
        assert example_class1.method2() == 1


class TestInstance2:
    """Testing for ExampleClass1, instance 2"""

    def test_method1(self, example_class2: ExampleClass1) -> None:
        "Testing for ExampleClass1.method1"
        assert example_class2.method1() == "string2"

    def test_method2(self, example_class2: ExampleClass1) -> None:
        "Testing for ExampleClass1.method2"
        assert example_class2.method2() == 2
