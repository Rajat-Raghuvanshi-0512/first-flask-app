"""
Provides translation from english to french and vice versa
"""
from deep_translator import MyMemoryTranslator

frenchTranslator = MyMemoryTranslator(source="en-IN", target="french")
englishTranslator = MyMemoryTranslator(source="french", target="en-IN")


def english_to_french(english_string):
    """
    Provides translation from english to french
    """
    french_string = frenchTranslator.translate(english_string)
    return french_string


def french_to_english(french_string):
    """
    Provides translation from french to english
    """
    english_string = englishTranslator.translate(french_string)
    return english_string
