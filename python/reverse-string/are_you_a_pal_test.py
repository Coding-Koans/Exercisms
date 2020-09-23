import unittest
from are_you_a_pal import panda_pal


class ReverseStringTest(unittest.TestCase):
    def test_an_empty_string(self):
        given = ""
        actual = panda_pal(given)
        self.assertEqual(actual, True)

    def test_not_a_palendrome(self):
        given = "koan"
        actual = panda_pal(given)
        self.assertEqual(actual, False)

    def test_a_palendrome(self):
        given = "hannah"
        actual = panda_pal(given)
        self.assertEqual(actual, True)

    def test_a_palendrome_with_some_caps(self):
        given = "Hannah"
        actual = panda_pal(given)
        self.assertEqual(actual, True)