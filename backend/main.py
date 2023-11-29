import logging
import os
from flask import Flask
from src.api.analyze import analyze_bp
from src.api.feedback import feedback_bp
from src.services.chatgpt_service import initialize_chatgpt

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize ChatGPT service with API key from environment variable
chatgpt_api_key = os.environ.get("CHATGPT_API_KEY")
if not chatgpt_api_key:
    raise ValueError("ChatGPT API key not set. Please set the CHATGPT_API_KEY environment variable.")

initialize_chatgpt(chatgpt_api_key)

# Dummy route for home
@app.route('/')
def home():
    logger.info('Home route accessed.')
    return 'Doctor AI Backend is up and running!'

# Include API blueprints
app.register_blueprint(analyze_bp)
app.register_blueprint(feedback_bp)

if __name__ == '__main__':
    app.run(debug=True)
