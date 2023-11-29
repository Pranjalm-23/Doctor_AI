# src/services/analyze_service.py

from src.services.chatgpt_service import generate_chat_response

def analyze_user_input(user_input):
    # Initial analysis logic (you can modify this based on your needs)
    analysis_result = f"Analysis completed for: {user_input}"

    # Enhance analysis using ChatGPT
    chatgpt_response = generate_chat_response(user_input)
    enhanced_analysis_result = f"{analysis_result}\n\nChatGPT Response: {chatgpt_response}"

    # Basic health assessment logic (you can modify and extend this)
    health_assessment = assess_health(user_input, chatgpt_response)
    enhanced_analysis_result += f"\n\nHealth Assessment: {health_assessment}"

    return enhanced_analysis_result

def assess_health(user_input, chatgpt_response):
    # Placeholder logic for health assessment



    # Replace it with a more sophisticated health assessment model
    if "severe pain" in user_input.lower() or "emergency" in chatgpt_response.lower():
        return "Emergency! Seek immediate medical attention."
    elif "pain" in user_input.lower() or "discomfort" in chatgpt_response.lower():
        return "Consult a doctor for further evaluation."
    else:
        return "No immediate health concerns detected. Monitor your symptoms and consult a doctor if needed."
