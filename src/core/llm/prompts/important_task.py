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
    def generate_prompt(self, user_message):
        prompt = f"""
        You are part of a chat system that stores all messages, but only embeds and indexes important ones for retrieval.

        Your job is to:
        1. Answer the user message, if it contains a question or statement that requires a response.
        2. Decide whether the message is important enough to be embedded (for future semantic search).
        3. Explain your reasoning briefly.

        ### Guidelines:
        Messages that are considered important typically include:
        - Questions that carry specific intent or domain knowledge.
        - Informative or detailed statements.
        - Decisions, insights, instructions, summaries, or anything with semantic weight.

        Messages that are NOT important include:
        - Short greetings, small talk, emotional reactions.
        - Acknowledgements, short follow-ups like “okay”, “thanks”, “yes”, “no”.

        ### Message:
        "{user_message}"
        """
        return prompt

    @classmethod
    def output_model(self):
        return ImportantOutput
