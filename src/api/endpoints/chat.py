# API /chat endpoint 
from fastapi import APIRouter, HTTPException, status
from src.models.schema import ChatRequest, ChatResponse
from src.core.llm.gemini_classifier import GeminiService
import uuid

router = APIRouter()

client = GeminiService()

@router.post("/chat", response_model=ChatResponse)
async def user_chat(request: ChatRequest):

    try:
        # Generate IDs
        conversation_id = request.conversation_id or f"conv_{uuid.uuid4().hex[:8]}" # take first 8 char
        assistant_message_id = f"assist_msg_{uuid.uuid4().hex[:8]}"
        user_message_id = f"user_msg_{uuid.uuid4().hex[:8]}"
        
        # call llm
        assistant_response, is_important = await client.parse_response(request.user_message)
        
        return ChatResponse(
            assistant_response=assistant_response,
            user_message_id=user_message_id,
            assistant_message_id=assistant_message_id,
            is_important=is_important,
            conversation_id=conversation_id,
            user_id=request.user_id
        )
        
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error: {str(e)}")