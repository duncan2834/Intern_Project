# Pydantic model for request/response, for validation, parse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional


# API CHAT FOR REQUEST/RESPONSE MODEL
class ChatRequest(BaseModel):
    """ Request for API Chat """
    user_id: str = Field(..., min_length=1, description="ID of user")
    user_message: str = Field(..., min_length=1, description="Message from user")
    conversation_id: Optional[str] = Field(None, description="ID of the conversation")
    task: str = Field(..., min_length=1, description="Task name for each purpose of prompt")
    
class ChatResponse(BaseModel):
    """ Response return to user """
    assistant_response: str = Field(..., min_length=1, description="Response from system")
    
class ChatInfoResponse(BaseModel):
    """ Full information of response for saving to database """
    assistant_response: str = Field(..., description="Response from system")
    user_message_id: str = Field(..., min_length=1, description="ID of message from user") 
    assistant_message_id: str = Field(..., min_length=1, description="ID of message from system") 
    is_important: bool = Field(default=False, description="Message is important or not to be embedded and saved to database")
    conversation_id: Optional[str] = Field(None, description="ID of the conversation")
    user_id: str = Field(..., min_length=1, description="ID of user")
    