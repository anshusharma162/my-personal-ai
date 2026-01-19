from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("AVAILABLE MODELS:\n")

models = client.models.list()

found = False
for model in models:
    print(model.name)
    found = True

if not found:
    print("❌ No models available for this API key")
