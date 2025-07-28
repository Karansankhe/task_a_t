def extract_text_from_pdf(pdf_bytes):
    import pymupdf  # PyMuPDF
    text = ""
    with pymupdf.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def process_image_with_gemini(image_bytes: bytes, filename: str, gemini_model) -> str:
    try:
        ext = filename.split(".")[-1].lower()
        mime_type = f"image/{ext}" if ext in ['jpg', 'jpeg', 'png', 'gif', 'webp'] else "image/jpeg"
        response = gemini_model.generate_content([
            {"mime_type": mime_type, "data": image_bytes},
            "Extract and return all text visible in this image. Format it clearly."
        ])
        return response.text
    except Exception as e:
        raise RuntimeError(f"Error processing image {filename}: {e}")

def split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200):
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""]
    )
    return splitter.split_text(text)