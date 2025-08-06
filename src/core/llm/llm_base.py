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
        pass
    
    @abstractmethod
    def get_response(self):
        """
        Calling LLM for response and deciding message important or not
        
        Returns:
            True of False
        """
        
        pass
    