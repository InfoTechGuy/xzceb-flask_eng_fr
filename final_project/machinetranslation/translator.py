from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French using the deep_translator package.
    
    Args:
        english_text (str): Text in English to be translated.

    Returns:
        str: Translated text in French, or None if translation failed.
    """
    try:
        french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    except Exception as e:
        print(f"An error occurred during translation: {str(e)}")
        return None
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English using the deep_translator package.
    
    Args:
        french_text (str): Text in French to be translated.

    Returns:
        str: Translated text in English, or None if translation failed.
    """
    try:
        english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    except Exception as e:
        print(f"An error occurred during translation: {str(e)}")
        return None
    return english_text