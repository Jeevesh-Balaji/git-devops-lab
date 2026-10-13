
"""A small Python application for Git and Docker practice."""


def greet(name: str = "Jeevesh") -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(greet())
    print(f"2 + 3 = {add(2, 3)}")
