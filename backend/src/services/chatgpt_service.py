# src/services/chatgpt_service.py

import openai

def initialize_chatgpt(api_key):
    openai.api_key = api_key

def generate_chat_response(user_input, model="gpt-3.5-turbo", max_tokens=100):
    try:
        prompt = f"User: {user_input}\nDoctor AI:"
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.7,
            stop=None  # Let the model generate a response without a specific stopping condition
        )
        return response.choices[0].text.strip()
    except Exception as e:
        # Log the error (you can enhance logging based on your needs)
        print(f"Error in generate_chat_response: {e}")
        
        # Return a placeholder text in case of an error
        return "Apologies, but there was an error generating a response. Please try again later."
