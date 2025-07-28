def generate_voice_output(target_language, speaker, pitch, pace, loudness, sarvam_client, translated_text):
    """Generate voice output for the translated text."""
    if not translated_text:
        raise ValueError("No translated text available for voice generation!")
    
    language_code, language_name = validate_language(target_language)
    with st.spinner(f"Generating voice in {language_name}..."):
        tts_response = sarvam_client.text_to_speech.convert(
            text=translated_text,
            target_language_code=language_code,
            speaker=speaker,
            pitch=pitch,
            pace=pace,
            loudness=loudness,
            speech_sample_rate=22050,
            enable_preprocessing=True,
            model="bulbul:v1"
        )
        return tts_response

def save_audio(tts_response):
    """Save the audio response to a temporary file."""
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    try:
        save(tts_response, temp_file.name)
        with open(temp_file.name, "rb") as f:
            audio_bytes = f.read()
    finally:
        os.unlink(temp_file.name)  # Clean up the temporary file
    return audio_bytes

def play_audio(audio_bytes):
    """Play the generated audio using Streamlit."""
    st.audio(audio_bytes, format='audio/wav')
    st.success("Voice generated successfully!")

def validate_language(language_name):
    """Validate and return the language code and name."""
    if not language_name:
        return "hi-IN", "Hindi"
    if language_name in SARVAM_LANGUAGES.values():
        for name, code in SARVAM_LANGUAGES.items():
            if code == language_name:
                return code, name
    if language_name in SARVAM_LANGUAGES:
        return SARVAM_LANGUAGES[language_name], language_name
    for name, code in SARVAM_LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code, name
    st.warning(f"Language '{language_name}' not found, defaulting to Hindi")
    return "hi-IN", "Hindi"