from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vectorstore import collection

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

loader = PyPDFLoader(
    "data/hr_policy.pdf"
)

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

for i, chunk in enumerate(chunks):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk.page_content
    )

    embedding = response.data[0].embedding

    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[chunk.page_content],
        metadatas=[
            {
                "document": "hr_policy.pdf",
                "page": chunk.metadata.get(
                    "page",
                    0
                )
            }
        ]
    )

print("✅ ChromaDB Updated")