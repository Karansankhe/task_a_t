def answer_question(query, gemini_model, encoder_model, chunks_with_sources, embeddings):
    """Answer a question using the processed documents and return a plain answer string."""
    try:
        query_vector = sentence_encode([query], encoder_model)[0]
        similarities = [
            (cosine_similarity(chunk_vec, query_vector), idx)
            for idx, chunk_vec in enumerate(embeddings)
        ]
        top_k = sorted(similarities, reverse=True)[:5]
        top_indices = [idx for _, idx in top_k]
        new_context = "\n".join(chunks_with_sources[i].text for i in top_indices)
        sources = list(set(chunks_with_sources[i].source for i in top_indices))
        prompt = CLAUSE_EXTRACTION_PROMPT.format(query=query, context=new_context)
        with st.spinner("Generating answer..."):
            response = gemini_model.generate_content(prompt)
            answer_text = response.text.strip()
        return answer_text, sources
    except Exception as e:
        raise RuntimeError(f"Error generating answer: {str(e)}")


def CLAUSE_EXTRACTION_PROMPT(query, context):
    return f"""
You are an expert insurance document assistant. Given a user query and the context from policy documents, perform the following:
1. Parse the query and extract key details: age, gender, procedure, location, policy duration.
2. Search and retrieve relevant clauses or rules from the provided context using semantic understanding.
3. Evaluate the retrieved information to determine the correct decision (approval status or payout amount) based on the logic defined in the clauses.
4. Return a short, clear, user-friendly answer in plain English (not JSON), e.g., "Yes, knee surgery is covered under the policy." or "No, this procedure is not covered under the policy." Do NOT return JSON or code blocks.
User Query: {query}
Context:
{context}
Return only the answer sentence, nothing else.
"""