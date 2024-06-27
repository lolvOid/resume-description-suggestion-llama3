from openai import OpenAI
from .config import Config
import json

client = OpenAI(
    api_key=Config.OPENAI_API_KEY,
    base_url=Config.OPENAI_BASE_URL
)

def generate_cv_description(current_role, current_company, start_date, is_present, end_date, skills, keywords):
    # Format end date based on is_present
    end_date_str = "Present" if is_present else end_date
    skills_str = ', '.join(skills)
    keywords_str = ', '.join(keywords)
    
    prompt = f"""
    Generate a structured JSON description for the work experience section of a CV. 
    The JSON should include the following details:
    
    - "current_role": The job title of the individual.
    - "current_company": The company where the individual works or worked.
    - "start_date": The start date of the role in YYYY-MM-DD format.
    - "end_date": The end date of the role in YYYY-MM-DD format or "Present" if the individual is currently in this role.
    - "skills": A list of skills relevant to the role.
    - "keywords": A list of keywords that should be included in the description.

    Example format:
    {{
        "current_role": "Senior Software Engineer",
        "current_company": "Tech Corp",
        "start_date": "2020-01-01",
        "end_date": "Present",
        "skills": ["Python", "Machine Learning", "Data Science", "AI", "NLP", "CV", "Data Mining", "Artificial Intelligence"],
        "description": "Detailed work experience description incorporating keywords."
    }}

    Please ensure the description is relevant to the provided details and incorporates the following keywords: {keywords_str}

    {{
        "current_role": "{current_role}",
        "current_company": "{current_company}",
        "start_date": "{start_date}",
        "end_date": "{end_date_str}",
        "skills": ["{skills_str}"],
        "description": "Generate a detailed work experience description here."
    }}
    """

    response = client.chat.completions.create(
        model="llama-13b-chat",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300  # Adjust this if needed to ensure the response fits within the token limit
    )

    # Extract the JSON content from the response
    try:
        response_content = response.choices[0].message.content.strip()
        # Ensure only the JSON part is extracted
        start_index = response_content.find('{')
        end_index = response_content.rfind('}') + 1
        json_content = response_content[start_index:end_index]
        cv_description = json.loads(json_content)
    except (json.JSONDecodeError, ValueError):
        cv_description = {"error": "Failed to parse response as JSON"}

    return cv_description

def suggest_verbs(current_role=None, sentence=None):
    if current_role and sentence:
        prompt = f"""
        Complete and correct sentences for a CV description based on the sentence "{sentence}".
        Limit to 5 sentences.
        """
    elif current_role:
        prompt = f"""
        Suggest a list of verbs or words that can be used in sentences for a CV description for a {current_role}.
        Limit to 5 suggestions.
        """
    else:
        prompt = """
        Correct the sentence structure or suggest relevant verbs or words for a CV description.
        """

    try:
        response = client.chat.completions.create(
            model="llama-13b-chat",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )

        if response and response.choices:
            response_content = response.choices[0].message.content.strip()
            # Split by new lines and clean up each suggestion
            cleaned_suggestions = [s.strip().strip('"').replace('\\', '') for s in response_content.split('\n') if s.strip()]
            suggestions = cleaned_suggestions[:5]  # Limit to 5 suggestions
        else:
            suggestions = []

    except (json.JSONDecodeError, ValueError) as e:
        suggestions = {"error": f"Failed to parse response as JSON. Error: {str(e)}"}
    except Exception as e:
        suggestions = {"error": f"An error occurred: {str(e)}"}

    return suggestions
