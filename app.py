import streamlit as st
from utils.pdf_loader import extract_text
from utils.vector_store import create_vector_store
from utils.chatbot import get_answer

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄"
)

st.title("📄 AI Document Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Processing PDF..."):

        text = extract_text(uploaded_file)

        st.session_state.vector_store = create_vector_store(text)

    st.success("PDF Processed Successfully!")

st.divider()

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input(
    "Ask a question about your document..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    if st.session_state.vector_store:

        answer = get_answer(
            question,
            st.session_state.vector_store
        )

    else:

        answer = "Please upload a PDF first."

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)
