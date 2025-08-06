# Call LLM for message classification, important or not
from google import genai
from google.genai import types
from src.core.llm.llm_base import BaseLLM
import os
from src.core.llm.prompts.prompt_registry import TaskRegistry
from src.core.llm.prompts.important_task import ImportantTask
class InvalidAPIKeyError(Exception):
    pass

class GeminiAPIError(Exception):
    pass

class GeminiService(BaseLLM):
    def __init__(self, api_key=None, model="gemini-2.0-flash"):
        super().__init__(api_key, model)
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.model = model
        
        # init task registry
        self.task_registry = TaskRegistry()
        
        if not self.api_key or not self.api_key.strip():
            raise InvalidAPIKeyError("Set api key in .env file of pass an valid api key")
        
        try:
            self.client = genai.Client(api_key=self.api_key)

        except Exception as e:
            # import error, server error
            raise GeminiAPIError(f"Failed to connect to Gemini: {str(e)}")
        
        try: 
            # check if api key is valid by calling light request
            _ = self.client.models.list()
        
        except Exception as e:
            raise InvalidAPIKeyError(f"Invalid api key: {str(e)}")
        
    async def get_response(self, message, task_name):
        """
        Calling LLM to get response
        
        Returns:
            Response from LLM
        """

        if not message or not message.strip():
            raise ValueError("Message can not be empty")
        
        try:
            task = self.task_registry.get_task(task_name)
            prompt = task.generate_prompt(message)
            config = types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=task.output_model()
            )
            content = [
            types.Content(
                role='user',
                parts=[types.Part(text=prompt)]
                )
            ]
            
            response = await self.client.aio.models.generate_content(
                model=self.model,
                contents=content,
                config=config
            )
            
            # check if text in response format
            if hasattr(response, "text"):
                return response.text
            
            # check if candidate in response format
            elif hasattr(response, "candidate") and response.candidates():
                return response.candidates[0].content.parts[0].text
            
            else:
                raise GeminiAPIError("No valid response from Gemini")
            
        except Exception as e:
            # server error, rate limit, ...
            raise GeminiAPIError(f"Error: {str(e)}")
    