from abc import ABC, abstractmethod

class BasePrompt(ABC):
    registry = {} # {taskname: taskclass}
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        try:
            instance = cls()
            BasePrompt.registry[instance.name] = instance
        except Exception as e:
            pass  

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