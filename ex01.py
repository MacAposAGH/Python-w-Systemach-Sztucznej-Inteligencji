"""
Exercise 01: running a Python program from the command line
"""
import platform
import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> int:
    print(f"Python {platform.python_version()} [{sys.executable}]")
    print(f"{sys.argv = }")

    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))

    return 0  # the exit code of the program


if __name__ == "__main__":
    sys.exit(main())
