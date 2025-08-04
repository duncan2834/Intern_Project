# Call LLM for message classification, important or not
from google import genai
from google.genai import types
from src.core.llm.llm_base import BaseLLM
import json

class InvalidAPIKeyError(Exception):
    pass

class GeminiAPIError(Exception):
    pass

class GeminiService(BaseLLM):
    def __init__(self, api_key=None, model="gemini-2.0-flash"):
        super().__init__(api_key, model)
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
        
    async def get_response_and_important_message(self, message):
        """
        Calling LLM to decide if message is important
        
        Returns:
            Response + decision to save or not
        """
        prompt = f"""
            You are a friendly chatbot assistant. Your task is to answer the user's question.
            After providing your answer, you must evaluate whether the user's message contains important or valuable information 
            worth storing embedding for long-term use (e.g., a request for a summary, an explanation of a concept, a significant question, 
            or an idea that needs to be remembered).
            Here are some guidelines to help you make the decision:
                'is_important': true if the message has high informational value. false if it’s just small talk or trivial.\
                    
            Your output format must be as follows:
            [Your answer]
            ```json
            {{
                "is_important": "[true/false]"
            }}
            Here is the user's message:
            {message}
        """
        if not message or not message.strip():
            raise ValueError("Message can not be empty")
        
        content = [
            types.Content(
                role='user',
                parts=[types.Part(text=prompt)]
            )
        ]
        try:
            response = await self.client.aio.models.generate_content(
                model=self.model,
                contents=content,
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
            raise GeminiAPIError(f"Gemini api error: {str(e)}")
    
    async def parse_response(self, message):
        response = await self.get_response_and_important_message(message)
        response_parts = response.split("```json")
        
        llm_response = response_parts[0].strip() # answer from llm
        # sometimes no json replied, in that case set is_important to False
        if len(response_parts) > 1:
            json_text = response_parts[1].strip() # json define whether important or not
            json_text = json_text[:-3] # delete ``` at the end of text so json can load
            data = json.loads(json_text)
            is_important = data.get("is_important", False)
        else:
            is_important = False
        return llm_response, is_important
