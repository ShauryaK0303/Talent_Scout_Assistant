from config import GEMINI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE, END_KEYWORDS
from .prompts_utils import SYSTEM_PROMPT
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel(MODEL_NAME)
def get_llm_response(messages, model=MODEL_NAME, max_tokens=MAX_TOKENS, temperature=TEMPERATURE):
    try:
        system_message = None
        conversation_text = ""
        
        for message in messages:
            if message["role"] == "system":
                system_message = message["content"]
            elif message["role"] == "user":
                conversation_text += f"User: {message['content']}\n"
            elif message["role"] == "assistant":
                conversation_text += f"Assistant: {message['content']}\n"
        
        prompt = ""
        if system_message:
            prompt += f"System instructions: {system_message}\n\n"
        
        prompt += f"Conversation history:\n{conversation_text}\n"
        prompt += "Assistant: "

        response = gemini_model.generate_content(prompt)
        
        if hasattr(response, 'text'):
            return response.text
        else:
            return response.parts[0].text
        
    except Exception as e:
        print(f"Error getting LLM response: {e}")
        print(f"Messages were: {messages}")
        return "I'm sorry, I'm having trouble responding right now. Please try again later."


def is_conversation_end(user_input, end_keywords=END_KEYWORDS):
     return any(keyword in user_input.lower() for keyword in end_keywords)
    