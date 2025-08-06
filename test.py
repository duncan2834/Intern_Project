import json

text = """
Response from LLM: Artificial intelligence (AI) involves creating computer systems capable of performing tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. It encompasses a wide range of techniques, including machine learning and deep learning, to enable computers to analyze data, identify patterns, and make predictions or take actions.
```json
{
    "is_important": "true",
    "reason": "The user asked for a definition of AI, which is a valuable piece of information to store for future use."
}
"""
text_parts = text.split("```json")
print(text_parts[1])
data = json.loads(text_parts[1])
is_important = data.get("is_important", False)
print(is_important)