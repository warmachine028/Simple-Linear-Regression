from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    a: float = 0.0
    b: float = 0.0


# Class for Global Boolean Vars
@dataclass
class BooleanVar:
    value: bool = False

    def set(self, value: bool) -> None:
        """Set the variable to VALUE"""
        self.value = value

    def get(self) -> bool:
        """Retrieve VALUE from the variable"""
        return self.value

    def switch(self) -> None:
        self.value = not self.value
