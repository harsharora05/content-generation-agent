from Agents.code_agent import code_agent
from Agents.content_creation_agent import content_creation_agent
from Agents.math_agent import math_agent

async def route_agent(query:str,intent:str):
    print(intent)
    if intent == 'code_agent':
        return  await code_agent(query)
    elif intent == 'content_creation_agent':
        return  await content_creation_agent(query)
    elif intent == 'math_agent':
        return  await math_agent(query)
    else :
        return "Currently I dont have power to execute your query"