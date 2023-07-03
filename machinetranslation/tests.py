import unittest
from translator import french_to_english, english_to_french


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            french_to_english("Comment vas-tu mon frère ?"), "How are you, brother?"
        )


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello my friend"), "Bonjour mon ami")


unittest.main()
