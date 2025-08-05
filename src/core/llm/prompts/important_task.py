import json 

def parse_important_response(response):
    """ 
    Parse llm response to split answer and decision to save or not 
    Args:
        message(str): message from user
    Returns:
        llm_response(str): answer from llm
        is_important(bool): deciding whether the message is important or not
    """
    
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


def generate_important_prompt(message):
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
    return prompt