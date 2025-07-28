def validate_language(language_name, supported_languages):
    if not language_name:
        return "hi-IN", "Hindi"
    if language_name in supported_languages.values():
        for name, code in supported_languages.items():
            if code == language_name:
                return code, name
    if language_name in supported_languages:
        return supported_languages[language_name], language_name
    for name, code in supported_languages.items():
        if name.lower() == language_name.lower():
            return code, name
    return "hi-IN", "Hindi"

def translate_text(text, target_language, sarvam_client):
    if not text:
        raise ValueError("No text provided for translation.")
    language_code, language_name = validate_language(target_language, SARVAM_LANGUAGES)
    translation = sarvam_client.text.translate(
        input=text,
        source_language_code="en-IN",
        target_language_code=language_code,
        speaker_gender="Male",
        mode="formal",
        model="sarvam-translate:v1",
        enable_preprocessing=False
    )
    return translation.translated_text

SARVAM_LANGUAGES = {
    "Hindi": "hi-IN",
    "Marathi": "mr-IN", 
    "Gujarati": "gu-IN",
    "Punjabi": "pa-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "Odia": "or-IN",
    "Bengali": "bn-IN",
    "Assamese": "as-IN",
    "Sanskrit": "sa-IN",
    "Nepali": "ne-IN",
    "Konkani": "kok-IN",
    "Maithili": "mai-IN",
    "Manipuri": "mni-IN",
    "Urdu": "ur-IN",
    "Sindhi": "sd-IN",
    "Dogri": "doi-IN",
    "Bodo": "brx-IN"
}