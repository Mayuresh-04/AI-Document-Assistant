import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():

    llm = ChatGroq(
        groq_api_key = os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    return llm


def get_answer(question, vector_store):
    docs = vector_store.similarity_search(
        question,
        k=4
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    if context =="":
        return "I couldn't find relevant information in the document."

    prompt = f"""
    You are a document assistant.

    Use ONLY the provided context.

    If answer is unavailable, say:
    "The answer is not available in the document."

    Context:
    {context}

    Question:
    {question}
    """

    llm = get_llm()
    response = llm.invoke(prompt)
    
    return response.content