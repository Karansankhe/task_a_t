import os
import streamlit as st
from config import setup_environment, load_models
from ui import initialize_ui, display_sidebar, display_tabs
from document_processing import process_documents
from qa import answer_question
from translation import translate_answer
from tts import generate_voice_output
from utils import initialize_session_state

def main():
    google_key, sarvam_key = setup_environment()
    gemini_model, encoder_model, sarvam_client = load_models(google_key, sarvam_key)
    initialize_session_state()
    
    initialize_ui()
    
    with st.sidebar:
        display_sidebar()
    
    tab1, tab2, tab3 = display_tabs()
    
    with tab1:
        st.header("Upload Your Documents")
        uploaded_files = st.file_uploader("Choose files to upload:", type=['pdf', 'jpg', 'jpeg', 'png', 'gif', 'webp'], accept_multiple_files=True)
        if uploaded_files and st.button("🚀 Process Documents"):
            process_documents(uploaded_files, gemini_model, encoder_model)
    
    with tab2:
        st.header("Ask Questions About Your Documents")
        query = st.text_input("Enter your question:")
        if st.button("🔍 Ask Question") and query:
            answer_question(query, gemini_model, encoder_model)
    
    with tab3:
        st.header("Conversation History")
        # Display conversation history logic here

if __name__ == "__main__":
    main()