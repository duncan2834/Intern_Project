from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv

load_dotenv()

class BaseLLM(ABC):
    """
    Abstract class for LLM 
    """
    
    @abstractmethod
    def __init__(self, api_key, model):
        """
        Initialize model with api key, model_nam

        Args:
            api_key (str): api key 
            model (str): model name
        """
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.model = model
    
    @abstractmethod
    def get_response_and_important_message(self):
        """
        Calling LLM for response and deciding message important or not
        
        Returns:
            True of False
        """
        
        pass
    
    @abstractmethod 
    def parse_response(self, message):
        """
        Split the response into 2 parts: llm response and json text containing "is important"
        Args:
            message(str): message from user
        Returns:
            llm_response(str): answer from llm
            is_important(bool): deciding whether the message is important or not
        """
        pass