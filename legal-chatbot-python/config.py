import os
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_RESOURCE_NAME = os.getenv("AZURE_RESOURCE_NAME")
AZURE_API_VERSION = "2023-12-01-preview"

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-for-legal-chatbot")

required_vars = [
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_ENDPOINT", 
    "AZURE_OPENAI_DEPLOYMENT"
]

missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

print("Configuration loaded:")
print(f"- AZURE_OPENAI_ENDPOINT: {AZURE_OPENAI_ENDPOINT}")
print(f"- AZURE_OPENAI_DEPLOYMENT: {AZURE_OPENAI_DEPLOYMENT}")
print(f"- AZURE_RESOURCE_NAME: {AZURE_RESOURCE_NAME}")
print(f"- API Key loaded: {'Yes' if AZURE_OPENAI_API_KEY else 'No'}")