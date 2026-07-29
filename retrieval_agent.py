from vectorstore import collection
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class RetrievalAgent:

    def run(self, query):

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        )

        embedding = response.data[0].embedding

        result = collection.query(
            query_embeddings=[embedding],
            n_results=3
        )

        return {
            "context": result["documents"][0],
            "sources": result["metadatas"][0]
        }