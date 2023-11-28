import logging
from flask import Flask
from src.api.analyze import analyze_bp
from src.api.feedback import feedback_bp

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
