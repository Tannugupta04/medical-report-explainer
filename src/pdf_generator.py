import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from src.config import OUTPUT_DIR


def generate_pdf_report(explanation: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "medical_report_explanation.pdf")

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("AI Medical Report Explanation", styles["Title"]))
    story.append(Spacer(1, 12))

    for line in explanation.split("\n"):
        if line.strip():
            story.append(Paragraph(line.strip(), styles["BodyText"]))
            story.append(Spacer(1, 8))

    doc.build(story)
    return output_path
