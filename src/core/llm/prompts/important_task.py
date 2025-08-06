from pydantic import BaseModel, Field
from src.core.llm.prompts.base_prompt import BasePrompt

class ImportantOutput(BaseModel):
    answer: str = Field(description="Answer from LLM, not including decision about importance")
    is_important: bool = Field(description="Message from user is important to be saved or not")
    reason: str = Field(description="Reason why the message is worth to be saved")

class ImportantTask(BasePrompt):
    @property
    def name(self):
        return "important"
    
    @classmethod
    def generate_prompt(self, message):
        prompt = f"""
            You are a friendly chatbot assistant. Your task is to answer the user's question.
            After providing your answer, you must evaluate whether the user's message contains important or valuable information 
            worth storing embedding for long-term use (e.g., a request for a summary, an explanation of a concept, a significant question, 
            or an idea that needs to be remembered).
            Here is the user's message:
            {message}
        """
        return prompt

    @classmethod
    def output_model(self):
        return ImportantOutput
