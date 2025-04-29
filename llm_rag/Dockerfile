FROM python:3

WORKDIR /app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir chromadb
RUN pip install --no-cache-dir langchain_community
RUN pip install --no-cache-dir langchain_text_splitters
RUN pip install --no-cache-dir sentence-transformers
RUN pip install --no-cache-dir openai
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir ollama
RUN pip install --no-cache-dir pypdf

COPY . .

RUN python rag.py

CMD [ "python", "./rag_query.py" ]