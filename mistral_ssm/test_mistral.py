import requests

OLLAMA_URL_API = "http://localhost:11434/api/generate"

payload = {
    "model": "mistral",
    "prompt": "What is AI?",
    "stream": False
}

response = requests.post(OLLAMA_URL_API, json=payload)

print(response.json())