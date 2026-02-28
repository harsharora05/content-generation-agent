from llm.llms import get_classification_llm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

async def classify_agent(query:str):
    llm = get_classification_llm()
    prompt =  ChatPromptTemplate.from_template(""" 
    You are a classification agent. Your one and only task is to select one of the agents which will be most
    suitable to solve the user query.
    AGENTS:
    - code_agent : it can code in any programming language 
    - content_creation_agent: it can create content on any latest topics for blogs,linkedin posts, Instagram captions/post, twitter posts etc.
    - math_agent : it can solve mathematical equations

    RULES:
    - return only agent name
    - if something like image generation and other operations that are not possible by our agents return "Not Possible"

    QUERY : {query}

    """)

    chain = prompt | llm | StrOutputParser()
    
    intent = chain.ainvoke(query)
    return intent