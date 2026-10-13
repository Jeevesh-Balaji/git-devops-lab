
"""Unit tests for the Python application."""

import unittest

from app import add, greet


class TestApp(unittest.TestCase):

    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, Jeevesh!")

    def test_custom_greeting(self):
        self.assertEqual(greet("Git"), "Hello, Git!")

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
