from llm.llms import get_generation_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

async def code_agent(query):
    llm = get_generation_llm()

    prompt = ChatPromptTemplate.from_template("""
        Your are a programming code assitive agent. You will help user code based on their query
        Query:{query}                          
    """)

    chain = prompt | llm | StrOutputParser()

    response = await chain.ainvoke(query)
    return response

