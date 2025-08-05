# FastAPI dependencies, include creating db session, ...
from src.core.llm.gemini_classifier import GeminiService

gemini_client = GeminiService()

def get_gemini_client():
    """ Dependency to init gemini service instance once """
    return gemini_client