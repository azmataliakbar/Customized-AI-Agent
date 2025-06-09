from deep_translator import GoogleTranslator

async def translate_text(text, target_language_code, target_language_name):
    translated = GoogleTranslator(target=target_language_code).translate(text)
    return f"AI Agent, Translating your text...\n\nTranslated to {target_language_name} language: {translated}"



