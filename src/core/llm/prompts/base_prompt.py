from abc import ABC, abstractmethod

class BasePrompt(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
    
    @property
    @abstractmethod
    def generate_prompt(self, message):
        pass
    
    @property
    @abstractmethod
    def output_model(self):
        pass