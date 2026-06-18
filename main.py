from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv()


# loader = PyPDFLoader("research_papers/paper1.pdf")
# docs = loader.load()
# print(f"Total number of pages: {len(docs)}")

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 500,
#     chunk_overlap=100
# )
# chunks = splitter.split_documents(docs)

# print("Total Chunks: ", len(chunks))
# print("First Chunk:\n")
# print(chunks[0].page_content)

# print("\nSecond Chunk:\n")
# print(chunks[1].page_content)

# print('\n\n')
# print(chunks[0].metadata)

embeddings = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-001"
)

vector = embeddings.embed_query(
    "What is Artificial Intelligence?"
)

print("Vector: ", vector[:10])
print(len(vector))
