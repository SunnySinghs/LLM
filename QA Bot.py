
### Installing Library
"""

!pip install langchain
!pip install pypdf
!pip install faiss-cpu

"""### Importing the LLM Model"""

# Import Ollama module from Langchain
from langchain.llms import Ollama

# Initialize an instance of the Ollama model
llm = Ollama(model="llama2")

# Invoke the model to generate responses
response = llm.invoke("Who is Elon Musk?")
print(response)

"""### Loading the Document"""

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader('/content/Assignment Support Document.pdf')
docs = loader.load()
docs

"""### Creating Chunk of Document Data"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunk_documents = text_splitter.split_documents(docs)
chunk_documents

"""### Creating Embeddings from Chunk data and Storing in FAISS (Facebook AI Similarity Search) vector database"""

# Vector Embedding and Vector Store
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS

embedding_model = OllamaEmbeddings();
vectordb = FAISS.from_documents(chunk_documents, embedding_model)
vectordb

"""### Performing the Similarity Search on Vector DB


"""

query = "ASHA workers"
result = vectordb.similarity_search(query)
result[0].page_content

"""### Creating Retriever"""

"""
Retrievers: A retriever is an interface that returns documents given an unstructured query. It is more general than a vector store.
  A retriever does not need to be able to store documents, only to return (or retrieve) them. Vector stores can be used as the backbone
  of a retriever
"""
retriever = vectordb.as_retriever()
retriever

"""### Importing and Intializing Conversation Memory with window size 5"""

"""
ConversationBufferWindowMemory keeps a list of the interactions of the conversation over time. It only uses the last K interactions.
This can be useful for keeping a sliding window of the most recent interactions, so the buffer does not get too large.
"""
from langchain.memory import ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(k=5,
            memory_key="chat_history",
            return_messages=True,  output_key='answer')

"""### Importing and Creating a Chain"""

"""
Retrieval chain: This chain can be used to have conversations with a document.
  It takes in a question and (optional) previous conversation history. If there is a previous conversation history,
  it uses an LLM to rewrite the conversation into a query to send to a retriever (otherwise it just uses the newest user input).
  It then fetches those documents and passes them (along with the conversation) to an LLM to respond.
"""
from langchain.chains import ConversationalRetrievalChain
convo_chain = ConversationalRetrievalChain.from_llm(
    llm = llm, retriever = retriever, memory = memory
)

"""### Querying the LLM Model"""

response = convo_chain.invoke({"question":"What is this document about?", "chat_history": []})
print(response['answer'])

response = convo_chain.invoke({"question":"What is direct taxes?", "chat_history": []})
print(response['answer'])

response = convo_chain.invoke({"question":"What is Amrit Kaal as Kartavya Kaal?", "chat_history": []})
print(response['answer'])

response = convo_chain.invoke({"question":"What are Budget Estimates 2024-25?", "chat_history": []})
print(response['answer'])

response = convo_chain.invoke({"question":"Who is Nirmala Sitharaman?", "chat_history": []})
print(response['answer'])

response = convo_chain.invoke({"question":"What is PM Awas Yojana?", "chat_history": []})
print(response['answer'])

"""### Last 5 Chat History"""

print(response['chat_history'])