from langchain_openai import ChatOpenAI;
from dotenv import load_dotenv

load_dotenv()

def get_classification_llm():
    classifier_llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    return classifier_llm

def get_generation_llm():
    generative_llm = ChatOpenAI(
        model="gpt-5",
        temperature=0.2
    )
    return generative_llm

def get_review_llm():
    review_llm = ChatOpenAI(
        model="gpt-5.2",
        temperature=0
    )
    return review_llm