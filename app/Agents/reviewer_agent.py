from llm.llms import get_review_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

async def review_agent(query,temp_response):

    llm = get_review_llm()

    prompt = ChatPromptTemplate.from_template("""
        Your are a powerfull reviewing agent. you will review and refactor (if required) the response returned by the previous agents and will make sure that correct response is returned to the user with minimal or no errors
                                              
        Query:{query}   
        Response : {temp_response}             
        RULES:
        you will return only the final response required nothing else no reviews from your side, only refactor if required and return.          
    """)

    chain = prompt | llm | StrOutputParser()

    response = await chain.ainvoke({"query":query,"temp_response":temp_response})
    return response