import os
from typing import List
from src.config import KNOWLEDGE_DIR


def load_knowledge_files() -> str:
    all_text = ""

    if not os.path.exists(KNOWLEDGE_DIR):
        return ""

    for filename in os.listdir(KNOWLEDGE_DIR):
        if filename.endswith(".txt"):
            file_path = os.path.join(KNOWLEDGE_DIR, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                all_text += f"\n\n--- {filename} ---\n"
                all_text += f.read()

    return all_text


def retrieve_medical_context(query_terms: List[str], k: int = 4) -> str:
    knowledge_text = load_knowledge_files()

    if not knowledge_text:
        return "No medical knowledge files found."

    if not query_terms:
        return "No abnormal tests found. Give general wellness explanation only."

    matched_context = ""

    for term in query_terms:
        term_lower = term.lower()

        for paragraph in knowledge_text.split("\n\n"):
            if term_lower in paragraph.lower():
                matched_context += paragraph + "\n\n"

    if matched_context.strip():
        return matched_context[:3000]

    return knowledge_text[:3000]