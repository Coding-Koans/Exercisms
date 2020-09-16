import unittest
from reverse_string import reverse


class ReverseStringTest(unittest.TestCase):
    def test_an_empty_string(self):
        given = ""
        actual = reverse(given)
        expected = ""
        self.assertEqual(actual, expected)

    def test_a_word(self):
        given = "robot"
        actual = reverse(given)
        expected = "tobor"
        self.assertEqual(actual, expected)

    def test_a_capitalized_word(self):
        given = "Ramen"
        actual = reverse(given)
        expected = "nemaR"
        self.assertEqual(actual, expected)

    def test_a_sentence_with_punctuation(self):
        given = "I'm hungry!"
        actual = reverse(given)
        expected = "!yrgnuh m'I"
        self.assertEqual(actual, expected)

    def test_a_palindrome(self):
        given = "racecar"
        actual = reverse(given)
        expected = "racecar"
        self.assertEqual(actual, expected)

    def test_an_even_sized_word(self):
        given = "drawer"
        actual = reverse(given)
        expected = "reward"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
