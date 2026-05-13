import os
import streamlit as st
import pandas as pd

from src.extract_text import extract_text
from src.parse_report import parse_report_text
from src.abnormal_checker import analyze_results, get_abnormal_tests
from src.rag_pipeline import retrieve_medical_context
from src.llm_explainer import generate_explanation
from src.voice_generator import generate_voice_summary
from src.pdf_generator import generate_pdf_report


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Medical Report Explainer",
    page_icon="🩺",
    layout="wide"
)


# ---------------- TITLE ---------------- #

st.title("🩺 AI Medical Report Explainer")

st.write(
    "Upload a blood test report and get a simple AI explanation with abnormal values, precautions, diet suggestions, and voice summary."
)

st.warning(
    "Disclaimer: This app is for educational support only. It does not diagnose disease, prescribe medicine, or replace a qualified doctor."
)


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("Settings")

    language = st.selectbox(
        "Choose explanation language",
        ["English", "Hindi"]
    )

    enable_voice = st.checkbox(
        "Generate voice summary",
        value=True
    )

    enable_pdf = st.checkbox(
        "Generate downloadable PDF",
        value=True
    )


# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload medical report PDF/Image",
    type=["pdf", "png", "jpg", "jpeg"]
)


# ---------------- MAIN APP ---------------- #

if uploaded_file:

    st.success(f"Uploaded: {uploaded_file.name}")

    # ---------- TEXT EXTRACTION ---------- #

    with st.spinner("Extracting text from report..."):

        try:
            extracted_text = extract_text(uploaded_file)

        except Exception as e:
            st.error(f"Text extraction failed: {e}")
            st.stop()

    with st.expander("View Extracted Text"):
        st.text_area(
            "Extracted Text",
            extracted_text,
            height=250
        )

    if not extracted_text.strip():

        st.error(
            "No text found. Please upload a proper digital PDF or clear image."
        )

        st.stop()

    # ---------- PARSE REPORT ---------- #

    with st.spinner("Parsing medical values..."):

        parsed_results = parse_report_text(extracted_text)

    if not parsed_results:

        st.error(
            "Could not detect common blood test values. Improve regex patterns in parse_report.py."
        )

        st.stop()

    # ---------- ANALYZE VALUES ---------- #

    analyzed_results = analyze_results(parsed_results)

    st.subheader("Detected Test Values")

    table_data = []

    for test, info in analyzed_results.items():

        table_data.append({
            "Test": test,
            "Value": info["value"],
            "Unit": info["unit"],
            "Reference Range": info["reference_range"],
            "Status": info["status"]
        })

    df = pd.DataFrame(table_data)

    st.dataframe(
        df,
        use_container_width=True
    )

    # ---------- ABNORMAL VALUES ---------- #

    abnormal_tests = get_abnormal_tests(analyzed_results)

    if abnormal_tests:

        st.error(
            "Abnormal values found: " + ", ".join(abnormal_tests)
        )

    else:

        st.success(
            "No abnormal values detected based on the app's basic reference ranges."
        )

    # ---------- GENERATE AI EXPLANATION ---------- #

    if st.button("Generate AI Explanation"):

        # ----- Retrieve Medical Context ----- #

        with st.spinner("Retrieving trusted medical context..."):

            medical_context = retrieve_medical_context(abnormal_tests)

        # ----- Generate AI Explanation ----- #

        with st.spinner("Generating AI explanation..."):

            explanation = generate_explanation(
                analyzed_results,
                medical_context,
                language
            )

        # ----- Display Explanation ----- #

        st.subheader("AI Explanation")

        st.write(explanation)

        # ---------- VOICE SUMMARY ---------- #

        if enable_voice:

            with st.spinner("Generating voice summary..."):

                try:

                    voice_file = generate_voice_summary(
                        explanation,
                        language
                    )

                    if voice_file:

                        st.subheader("Voice Summary")

                        with open(voice_file, "rb") as audio_file:

                            audio_bytes = audio_file.read()

                        st.audio(
                            audio_bytes,
                            format="audio/mp3"
                        )

                        with open(voice_file, "rb") as audio_file:

                            st.download_button(
                                label="Download Voice Summary",
                                data=audio_file,
                                file_name="medical_summary.mp3",
                                mime="audio/mpeg"
                            )

                    else:

                        st.warning(
                            "Voice summary could not be generated."
                        )

                except Exception as e:

                    st.error(
                        f"Voice generation failed: {e}"
                    )

        # ---------- PDF DOWNLOAD ---------- #

        if enable_pdf:

            with st.spinner("Creating PDF report..."):

                try:

                    pdf_path = generate_pdf_report(explanation)

                    with open(pdf_path, "rb") as pdf_file:

                        st.download_button(
                            label="Download Explanation PDF",
                            data=pdf_file,
                            file_name="medical_report_explanation.pdf",
                            mime="application/pdf"
                        )

                except Exception as e:

                    st.error(
                        f"PDF generation failed: {e}"
                    )

else:

    st.info(
        "Please upload a PDF or image report to start."
    )