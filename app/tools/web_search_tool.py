from langchain.tools import tool
from serpapi import GoogleSearch
import os

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

@tool
async def search_content(query: str) -> str:
    """search web and return  content snippet."""
    try:
        print("tool called")
        params = {
            "engine": "google",
            "q": query,
            "api_key": SERPAPI_KEY,
        }
        search = await GoogleSearch(params)
        results = search.get_dict()
        snippets = []

        for item in results.get("organic_results", []):
            title = item.get("title")
            snippet = item.get("snippet")
            if title and snippet:
                snippets.append(f"{title}: {snippet}")

        return "\n\n".join(snippets)
    except Exception as e:
        return f"Error: {str(e)}"