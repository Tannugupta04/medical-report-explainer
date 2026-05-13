# import google.generativeai as genai
# from src.config import GEMINI_API_KEY


# def generate_explanation(analyzed_results, medical_context: str, language: str = "English") -> str:

#     if not GEMINI_API_KEY:
#         return "Gemini API key is missing. Please add GEMINI_API_KEY in your .env file."

#     genai.configure(api_key=GEMINI_API_KEY)

#     model = genai.GenerativeModel("models/gemini-1.5-pro")

#     prompt = f"""
# You are an AI medical report explainer.

# Your job is to explain blood report values in simple language.

# Important safety rules:
# - Do NOT diagnose disease.
# - Do NOT prescribe medicines.
# - Do NOT replace a doctor.
# - Give general educational explanation only.
# - Tell user to consult a qualified doctor for abnormal or serious results.
# - Keep language simple and beginner-friendly.

# Output language: {language}

# Analyzed report values:
# {analyzed_results}

# Trusted medical context:
# {medical_context}

# Generate output in this format:

# 1. Overall Summary
# 2. Normal Values
# 3. Abnormal Values
# 4. What Abnormal Values May Generally Indicate
# 5. General Precautions
# 6. Diet and Lifestyle Suggestions
# 7. When to Consult a Doctor
# 8. Disclaimer
# """

#     try:
#         response = model.generate_content(prompt)
#         return response.text

#     except Exception as e:

#         return f"""
# AI explanation could not be generated right now.

# Reason:
# Gemini API quota/rate limit issue.

# Basic Report Summary:
# Your report values were extracted and analyzed successfully.
# Please check the abnormal values table above.

# General Advice:
# - Do not panic based only on one report.
# - Consult a doctor for proper diagnosis.
# - Maintain a balanced diet, hydration, sleep, and regular checkups.

# Technical Error:
# {str(e)}
# """

from groq import Groq
from src.config import GROQ_API_KEY


def generate_explanation(analyzed_results, medical_context, language="English"):

    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
Explain this medical report in simple language.

Report:
{analyzed_results}

Medical Context:
{medical_context}

Give:
1. Summary
2. Abnormal values
3. Possible indications
4. Precautions
5. Diet suggestions
6. Disclaimer
"""

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"