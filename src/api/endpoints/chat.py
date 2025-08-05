# API /chat endpoint 
from fastapi import APIRouter, HTTPException, status, Depends
from src.models.schema import ChatRequest, ChatResponse, ChatInfoResponse
from src.core.dependencies import get_gemini_client
from src.core.llm.gemini_classifier import GeminiService
import uuid

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def user_chat(request: ChatRequest, client: GeminiService = Depends(get_gemini_client)):

    # Generate IDs
    conversation_id = request.conversation_id or f"conv_{uuid.uuid4().hex[:8]}" # take first 8 char
    assistant_message_id = f"assist_msg_{uuid.uuid4().hex[:8]}"
    user_message_id = f"user_msg_{uuid.uuid4().hex[:8]}"
    
    # call llm
    assistant_response, is_important = await client.important_response(request.user_message)
    
    # full response info saved to database
    response_info = ChatInfoResponse(
        assistant_response=assistant_response,
        user_message_id=user_message_id,
        assistant_message_id=assistant_message_id,
        is_important=is_important,
        conversation_id=conversation_id,
        user_id=request.user_id
    )
    print(f"Message is important: {is_important}")
    # save_conversation_to_db (request and response info)
    # if important -> embed user message -> 
    # return only response from system
    return ChatResponse(
        assistant_response=assistant_response
    )
    

