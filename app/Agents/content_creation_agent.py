from llm.llms import get_generation_llm
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent
from tools.web_search_tool import search_content

async def content_creation_agent(query):
    llm = get_generation_llm()
    tools = [search_content]


    agent = create_agent(model=llm,tools=tools,system_prompt="""You are a content writing agent.

    Rules:
    - always use the web search tool to gather latest information
    - conclude your answer ONLY on the tool results
    - dont rely on your internal knowledge for current events.
    """ )

    response = await agent.ainvoke({
        'messages' : [
            {"role" : "user" , "content": query}
        ]
    })
    return response["messages"][-1].content