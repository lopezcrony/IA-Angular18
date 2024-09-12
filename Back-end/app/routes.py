from flask import Blueprint, request, jsonify
from .gemini_ai import generate_prompt

main = Blueprint('main', __name__)

@main.route("/chat", methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')
    print('Mensaje recibido:', prompt)
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400    

    response = generate_prompt(prompt)
    return jsonify({'response': response})
