# src/api/analyze.py

from flask import Blueprint, request
from src.services.analyze_service import analyze_user_input

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/api/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        user_input = request.json.get('user_input')
        analysis_result = analyze_user_input(user_input)
        return {'result': analysis_result}
    else:
        return 'Analysis route expects a POST request.'
