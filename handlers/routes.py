from flask import request, jsonify
from modules.openai_client import generate_cv_description, suggest_verbs

def configure_routes(app):
    @app.route('/', methods=['GET'])
    def index():
        return 'Welcome!'

    # Post routes
    @app.route('/generate-cv', methods=['POST'])
    def generate_cv():
        data = request.json
        current_role = data.get('current_role', 'Senior Software Engineer')
        current_company = data.get('current_company', 'Tech Corp')
        start_date = data.get('start_date', '2020-01-01')
        is_present = data.get('is_present', True)
        end_date = data.get('end_date', '')
        skills = data.get('skills', [])
        keywords = data.get('keywords', [])

        cv_description = generate_cv_description(current_role, current_company, start_date, is_present, end_date, skills, keywords)

        return jsonify(cv_description)

    @app.route('/suggest', methods=['POST'])
    def suggest_verbs_endpoint():
        data = request.json
        current_role = data.get('current_role')
        sentence = data.get('sentence')

        suggestions = suggest_verbs(current_role=current_role, sentence=sentence)

        return jsonify(suggestions)

    # Get routes
    @app.route('/generate-cv', methods=['GET'])
    def generate_cv_get():
        return 'Use POST method to generate CV.'

    @app.route('/suggest', methods=['GET'])
    def suggest_verbs_get():
        return 'Use POST method to suggest verbs or keywords.'
