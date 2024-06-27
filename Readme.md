# Flask REST API for CV Description Suggestions

This Simple Flask-based REST API empowers you to create impactful CV descriptions by suggesting verbs or complete sentences. It leverages the powerful OpenAI GPT-3 model (Llama-3) to generate suggestions tailored to your input.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/lolvOid/python-resume-description-suggestion-llama3
cd python-resume-description-suggestion-llama3
```
Install dependencies:
```bash
pip install -r requirements.txt
```

2. **Set up OpenAI API key:**

Obtain an API key from OpenAI (if you haven't already).
Set it as an environment variable securely:
```bash
export OPENAI_API_KEY=<your_openai_api_key>
```

3. **Run the Flask application:**

```bash
python run.py
```

By default, the API is accessible on http://localhost:5000.

## API Endpoints
### POST /suggest-verbs

Generates suggestions based on the provided parameters in the request body.
Request Body (JSON):

```JSON
{
  "current_role": "Web Developer" (Optional),
  "sentence": "Proficient in Go programming language" (Optional),
  "keywords": ["software development", "AI", "cloud computing"] (Optional)
}
```

current_role (Optional): The specific role for which you require suggestions.
sentence (Optional): A starting sentence to generate additional sentences or verb suggestions.

Response (JSON):

```JSON
{
  "suggestions": [
    "Developed scalable web applications using cloud-based technologies.",
    "Integrated AI-driven analytics tools with web applications.",
    "Designed and implemented high-performance web services.",
    "Deployed cloud-based web applications using DevOps practices.",
    "Built reliable backend systems with robust third-party packages."
  ]
}
```

### GET /

Returns a simple welcome message or API documentation.
Usage
Using POST /suggest-verbs:

Provide current_role and either sentence or keywords in the request body.
The API responds with up to 5 suggestions formatted as a JSON array.
Example usage in Python:

```Python
import requests

url = 'http://localhost:5000/suggest-verbs'
data = {
  "current_role": "Web Developer",
  "sentence": "Proficient in Go programming language",
  "keywords": ["software development", "AI", "cloud computing"]
}

response = requests.post(url, json=data)
print(response.json())
```

## Error Handling
The API will return an error response with informative messages if it encounters issues (e.g., invalid JSON format, server problems).

## Notes
Ensure your OpenAI API key (OPENAI_API_KEY) is securely stored and accessed through environment variables.
The suggest_verbs function's prompt templates and response handling can be adjusted to meet your specific requirements or for further enhancements.
