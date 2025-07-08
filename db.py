from langchain_community.document_loaders import GutenbergLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import uuid
from langchain_chroma import Chroma
from topic_modelling import get_metadata_for_chunk
from langchain_core.documents import Document

#chroma_client = chromadb.Client()

##Change this to PDF Loader

loader = PyPDFLoader("sample-local-pdf.pdf")

book = loader.load()

text_spitter = CharacterTextSplitter(chunk_size = 800, chunk_overlap =100)
docs = text_spitter.split_documents(book)

chunk_texts = [doc.page_content for doc in docs]
metadata_list = [get_metadata_for_chunk(text) for text in chunk_texts]



docs_with_metadata = [
    Document(page_content=text, metadata=metadata)
    for text, metadata in zip(chunk_texts, metadata_list)
]

embeddings = HuggingFaceEmbeddings()

vector_store = Chroma(
    collection_name="collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  
)



ids = [str(uuid.uuid4()) for _ in chunk_texts]

vector_store.add_documents(ids= ids, documents = docs_with_metadata)









