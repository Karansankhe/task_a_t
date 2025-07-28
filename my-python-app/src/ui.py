import streamlit as st

def display_header():
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 1rem;">
            <span style="font-size:2.2rem;">📚</span>
            <span style="font-size:2rem; font-weight:600;">Smart Document QA Assistant</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='font-size:1.1rem; color:#555;'>Upload your policy documents, ask questions, and get clear answers in your preferred language.</p>",
        unsafe_allow_html=True,
    )

def display_sidebar(supported_languages, chunks_with_sources):
    with st.sidebar:
        st.header("Settings")
        selected_language = st.selectbox(
            "Select Language for Translation:",
            options=list(supported_languages.keys()),
            index=0
        )
        if chunks_with_sources:
            st.subheader("Document Stats")
            st.metric("Processed Chunks", len(chunks_with_sources))
            sources = list(set(chunk.source for chunk in chunks_with_sources))
            st.metric("Documents", len(sources))
            with st.expander("View Sources"):
                for source in sources:
                    st.write(f"• {source}")
    return selected_language

def display_tabs():
    return st.tabs([
        "📁 Upload Documents", 
        "❓ Ask Questions", 
        "💬 Conversation History"
    ])