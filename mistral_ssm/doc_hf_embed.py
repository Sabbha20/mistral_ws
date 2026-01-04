from doc_loaders import extract_text

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def process_docs(file_path):
    text = extract_text(file_path)
    
    if not text:
        print("No text extracted from the document.")
        return None
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_text(text)
    
    return texts

def store_embedings(texts, db_path="chroma.db"):
    vector_store = Chroma(
        collection_name="documents",
        embedding_function=embedding_model,
        persist_directory=db_path
    )
    vector_store.add_texts(texts)
    
    print(f"✅ Stored {len(texts)} text chunks in the vector store at {db_path}.")

if __name__ == "__main__":
    file_path = "resume.pdf"  # Change this to your document path
    texts = process_docs(file_path)
    if texts:
        store_embedings(texts)