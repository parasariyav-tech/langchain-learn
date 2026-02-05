from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader,TextLoader


loader = TextLoader('viremder.txt', encoding='utf-8')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0].page_content)