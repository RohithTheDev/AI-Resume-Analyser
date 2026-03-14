import streamlit as st
import PyPDF2
import io
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

st.set_page_config(page_title="AI Resume Analyser", page_icon=":page_facing_up:", layout="centered")
st.title("AI Resume Analyser")
st.markdown("Upload your resume in PDF format, and let our AI analyze it for you!")


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf","txt"])
job_role = st.text_input("Enter the job role you are applying for (optional):")


analyse=st.button("Analyse Resume")

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    
    return uploaded_file.read().decode("utf-8")

if analyse and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read. Please upload a valid PDF or text file.")
            st.stop()
        
        prompt = f""" Please analyse this resume and provide constuctive feedback.
        focuse on the following aspects:
        1.Content clarity and impact
        2.Skill Presentation
        3.Experience Description
        4. Specfic improvement for {job_role if job_role else "General Job Application"}
        
        Resume Content:
        {file_content}
        
        Please provide your analysis in a clear, structured format with specfic recommendations for improvement."""

        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        try:
            response = model.generate_content(prompt)
            analysis = response.text
        except Exception as e:
            st.error(f"An error occurred with the AI analysis: {str(e)}")
            st.stop()

        st.markdown("### Analysis Results:")
        st.markdown(analysis)
    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")