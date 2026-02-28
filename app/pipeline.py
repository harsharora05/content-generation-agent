from Agents.router_agent import route_agent
from Agents.classification_agent import classify_agent
from Agents.reviewer_agent import review_agent

async def run_pipeline(query):

    intent = await classify_agent(query)

    temp_response = await route_agent(query,intent)

    final_response = await review_agent(query,temp_response)

    return final_response

    