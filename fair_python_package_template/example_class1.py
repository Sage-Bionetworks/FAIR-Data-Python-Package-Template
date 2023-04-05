"""Example Class 1"""


class ExampleClass1:
    """Example Class 1"""

    def __init__(self, attribute1: str, attribute2: int) -> None:
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self) -> str:
        """Returns attribute1

        Returns:
            str: attribute1
        """
        return self.attribute1

    def method2(self) -> int:
        """Returns attribute2

        Returns:
            int: attribute2
        """
        return self.attribute2
