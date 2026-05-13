import fitz
import pytesseract
from PIL import Image
import io

# Windows Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(uploaded_file):
    text = ""

    file_bytes = uploaded_file.read()
    doc = fitz.open(stream=file_bytes, filetype="pdf")

    # First try normal PDF text extraction
    for page in doc:
        text += page.get_text()

    # If text PDF nahi hai, then OCR use karo
    if text.strip():
        return text

    ocr_text = ""

    for page in doc:
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))
        ocr_text += pytesseract.image_to_string(image)

    return ocr_text


def extract_text_from_image(uploaded_file):
    image = Image.open(uploaded_file)
    text = pytesseract.image_to_string(image)
    return text


def extract_text(uploaded_file):
    file_type = uploaded_file.type

    if file_type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)

    elif file_type in ["image/png", "image/jpeg", "image/jpg"]:
        return extract_text_from_image(uploaded_file)

    else:
        return ""