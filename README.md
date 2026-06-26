# AI Document Assistant

## Overview
AI Document Assistant is a Streamlit-based web application that allows users to upload PDF documents and ask questions about their content using Large Language Models (LLMs). The application processes the document, creates embeddings, and provides context-aware answers.

## Features
- Upload PDF documents
- Extract text from PDFs
- AI-powered question answering
- Fast document search using vector embeddings
- Simple and interactive Streamlit interface

## Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- Groq API
- HuggingFace Embeddings
- PyPDF

## Project Structure

AI-Document-Assistant/
│── app.py
│── requirements.txt
│── README.md
│── .env
│── utils.py (if applicable)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Document-Assistant.git
```

### 2. Navigate to the project

```bash
cd AI-Document-Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```
# 6. Demo Video link

https://1drv.ms/v/c/dc413bd956ade47f/IQD61HU71Z_XRrR0n_6gFuy3AeLi2jE3s0KwUNC1OX6uhKY?e=nAaOwA

## Usage

1. Open the Streamlit app.
2. Upload a PDF file.
3. Wait for processing.
4. Ask questions related to the uploaded document.
5. Receive AI-generated answers.

## Future Improvements

- Support multiple PDFs
- Chat history
- Document summarization
- OCR for scanned PDFs

## Author

Mayuresh Mahajan
