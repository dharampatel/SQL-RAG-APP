import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"  # your FastAPI backend

st.set_page_config(page_title="RAG Demo", page_icon="📘", layout="centered")

st.title("📘 Async RAG Demo")
st.write("Ask questions from your knowledge base and get AI-generated answers with sources.")

# Sidebar
st.sidebar.header("📂 Manage Documents")
title = st.sidebar.text_input("Title")
content = st.sidebar.text_area("Content")
source = st.sidebar.text_input("Source (optional)")

if st.sidebar.button("Add Document"):
    if title and content:
        resp = requests.post(f"{API_BASE}/docs", json={"title": title, "content": content, "source": source})
        if resp.status_code == 200:
            st.sidebar.success("✅ Document added successfully!")
        else:
            st.sidebar.error(f"❌ Error: {resp.text}")
    else:
        st.sidebar.warning("Please provide title and content.")

if st.sidebar.button("List Documents"):
    resp = requests.get(f"{API_BASE}/documents?limit=20")
    if resp.status_code == 200:
        docs = resp.json()
        st.sidebar.write(docs)
    else:
        st.sidebar.error("❌ Failed to fetch documents.")


# Main QA Section
st.subheader("💬 Ask a Question")

query = st.text_input("Your question", placeholder="e.g., What is the return policy?")

top_k = st.slider("Number of results (top_k)", min_value=1, max_value=10, value=5)

if st.button("Get Answer"):
    if query.strip():
        with st.spinner("Thinking..."):
            resp = requests.post(f"{API_BASE}/query", json={"query": query, "top_k": top_k})
            if resp.status_code == 200:
                result = resp.json()
                st.markdown(f"**Answer:** {result['answer']}")
                if "sources" in result and result["sources"]:
                    st.markdown("**Sources:**")
                    for src in result["sources"]:
                        st.markdown(f"- {src}")
            else:
                st.error(f"❌ Error: {resp.text}")
    else:
        st.warning("Please enter a question.")
