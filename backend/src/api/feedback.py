# src/api/feedback.py

from flask import Blueprint, request
from src.services.feedback_service import handle_user_feedback

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/api/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        user_feedback = request.json.get('feedback')
        feedback_response = handle_user_feedback(user_feedback)
        return {'response': feedback_response}
    else:
        return 'Feedback route expects a POST request.'
