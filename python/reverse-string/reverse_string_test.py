import unittest
from reverse_string import reverse


class ReverseStringTest(unittest.TestCase):
    def test_an_empty_string(self):
        given = ""
        actual = reverse(given)
        self.assertEqual(actual, "")

    def test_a_word(self):
        given = "robot"
        actual = reverse(given)
        self.assertEqual(actual, "tobor")

    def test_a_capitalized_word(self):
        given = "Ramen"
        actual = reverse(given)
        self.assertEqual(actual, "nemaR")

    def test_a_sentence_with_punctuation(self):
        given = "I'm hungry!"
        actual = reverse(given)
        self.assertEqual(actual, "!yrgnuh m'I")

    def test_a_palindrome(self):
        given = "racecar"
        actual = reverse(given)
        self.assertEqual(actual, "racecar")

    def test_an_even_sized_word(self):
        given = "drawer"
        actual = reverse(given)
        self.assertEqual(actual, "reward")


if __name__ == "__main__":
    unittest.main()
