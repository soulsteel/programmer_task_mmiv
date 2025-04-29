# Part 1
import langchain_community
import langchain_text_splitters
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter

# load the document and split it into pages
loader = PyPDFLoader("fiona_faq.pdf")
pages = loader.load_and_split()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(pages)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

##############################################################################
# Part2
# Chroma DB client
# create the chroma client
import uuid
import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(host='host.docker.internal', port=8000,settings=Settings(allow_reset=True))
client.reset()  # resets the database
collection = client.create_collection("my_collection")
for doc in docs:
    collection.add(
        ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
    )

# tell LangChain to use our client and collection name
db = Chroma(
    client=client,
    collection_name="my_collection",
    embedding_function=embedding_function,
)
query = "What training does the model have?"
docs = db.similarity_search(query)
print(docs[0].page_content)
