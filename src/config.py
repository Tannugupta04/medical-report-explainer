import os
from dotenv import load_dotenv

load_dotenv()

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
APP_NAME = "AI Medical Report Explainer"
OUTPUT_DIR = "outputs"
KNOWLEDGE_DIR = "data/medical_knowledge"
