def split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""]
    )
    return splitter.split_text(text)

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

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
    return "hi-IN", "Hindi"  # Default to Hindi if not found