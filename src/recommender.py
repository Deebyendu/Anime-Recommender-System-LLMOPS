from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self,retriever,api_key,model_name:str):
        self.retriever = retriever
        self.llm=ChatGroq(api_key=api_key,model=model_name,temperature=0)
        self.prompt= get_anime_prompt()
        
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        self.chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
)

    def get_recommendation(self, query: str):
        result = self.chain.invoke(query)
        return result
    
