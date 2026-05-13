# 🩺 AI Medical Report Explainer

An AI-powered healthcare support application that helps users understand blood test reports in simple and user-friendly language. The system extracts important medical values from uploaded reports, identifies abnormal parameters, and generates simplified AI-based explanations along with precautions, diet suggestions, downloadable summaries, and voice explanations.

> ⚠️ Disclaimer: This project is built for educational and informational purposes only. It does not diagnose diseases, prescribe medicines, or replace professional medical advice from a qualified doctor.

---

# 🚀 Features

- Upload medical reports in:
  - PDF
  - PNG
  - JPG / JPEG

- Extract report text automatically
- Detect common blood test values
- Identify Low / Normal / High values
- Generate simplified AI explanations
- Voice summary generation
- Downloadable PDF summary
- AI-generated precautions and diet suggestions
- Retrieval-based medical context support

---

# 🧠 Problem Statement

Medical reports often contain complex medical terminology that many users find difficult to understand. People usually:
- Search medical terms manually online
- Depend entirely on doctors for basic interpretation
- Get confused by technical blood report values

This project aims to simplify that process using AI by converting technical medical reports into easy-to-understand summaries within seconds.

---

# 💡 How the Project Works

1. User uploads a medical report
2. The application extracts text from the report
3. Blood test values are identified automatically
4. Values are checked against predefined reference ranges
5. Abnormal values are highlighted
6. AI generates simplified explanations
7. General precautions and diet suggestions are provided
8. Voice summary and downloadable PDF are generated

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI / NLP
- Groq API / Gemini API
- Prompt Engineering

## OCR & PDF Processing
- pytesseract

## Voice Generation
- gTTS
- pyttsx3

## Data Processing
- Pandas

## PDF Export
- ReportLab

---

# 📂 Project Structure

```text
medical-report-explainer/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── src/
│   ├── extract_text.py
│   ├── parse_report.py
│   ├── abnormal_checker.py
│   ├── rag_pipeline.py
│   ├── llm_explainer.py
│   ├── voice_generator.py
│   └── pdf_generator.py
│
├── data/
│   └── medical_knowledge/
│
└── outputs/

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone <your-repository-link>

cd medical-report-explainer

### Create virtual environment

python -m venv venv


# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone <your-repository-link>
cd medical-report-explainer
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

or

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 5. Run Application

```bash
python -m streamlit run app.py
```

---

# 📊 Current Capabilities

✅ Blood report text extraction  
✅ Abnormal value detection  
✅ AI-generated explanation  
✅ Voice summary generation  
✅ Downloadable PDF summary  
✅ Hindi/English support  

---

# ⚠️ Current Limitations

- OCR accuracy may vary for scanned reports
- Different lab formats may affect extraction
- Not all blood tests are currently supported
- AI explanations are informational only
- Explanation is only limited to one language(English)

---

# 🔮 Future Improvements

- Better OCR accuracy
- Support for more medical tests
- Better table extraction from reports
- User profile support (age/gender)
- Multilingual chatbot
- Authentication system
- Docker deployment
- Encrypted report storage
- Multilanguage explanation

---

# 📈 Impact & Improvement

Although the project is still in the experimental and improvement stage, it successfully demonstrates how AI can simplify healthcare-related information.

## Improvements Achieved

- Reduced manual effort required to understand reports
- Automated report extraction and explanation generation
- Combined AI explanation, PDF export, and voice accessibility into one workflow
- Improved accessibility through Hindi/English explanations and audio summaries

---

### Explanation

This project solves a real-world problem where people receive medical reports but struggle to understand technical medical terminology. I built an AI-powered Medical Report Explainer that extracts text from uploaded reports, detects important blood test values, identifies abnormal parameters using rule-based logic, and generates simplified explanations using Generative AI.

The application also provides precautions, diet suggestions, downloadable PDF summaries, and Hindi/English voice explanations to improve accessibility. While the project is still experimental and requires further improvements in OCR accuracy and report handling, it successfully demonstrates how AI can automate and simplify healthcare-related information in a user-friendly way.

---

# 👩‍💻 Author

**Tannu Gupta**  
B.Tech CSE | Data Science & Generative AI Enthusiast
``
