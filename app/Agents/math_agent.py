from llm.llms import get_generation_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

async def math_agent(query):
    llm = get_generation_llm()

    prompt = ChatPromptTemplate.from_template("""
        Your are an expert mathematics agent. You will help user solve mathematics based equations or problems based on their query
        Query:{query}                          
    """)

    chain = prompt | llm | StrOutputParser()

    response = chain.ainvoke(query)
    return response