from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("research_papers/paper1.pdf")
docs = loader.load()
print(f"Total number of pages: {len(docs)}")
print('First Page: \n\n')
print(docs[0].page_content[:1000])