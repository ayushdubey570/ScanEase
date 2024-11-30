from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ScanEase")
st.header("ScanEase:Optimize Today, Achieve Tomorrow")
input_text=st.text_area("Enter Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF):",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume..!!")

submit2 = st.button("How Can I Improvise my Skills ?")

submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager. Your task is to conduct a thorough review of the provided resume against the specific job description. Please provide a detailed professional evaluation of the candidate's alignment with the role.

Specifically:

Evaluation - Assess how well the candidate's profile matches the job requirements.

Strengths - Highlight the key strengths of the applicant in relation to the job.

Weaknesses - Identify any weaknesses or gaps in the candidate's qualifications.

Your insights will help determine the suitability of the candidate for the role.
"""

input_prompt2 = """
You are an expert in career development and skills enhancement. Your task is to provide actionable advice on how an individual can improvise and improve their skills in their professional field. Please include the following in your response:

Skill Assessment- Provide methods for individuals to evaluate their current skill levels and identify areas for improvement.

Learning Resources- Suggest reliable resources, such as online courses, books, or workshops, that can help them develop these skills.

Practical Application- Offer strategies for applying new skills in real-world scenarios to enhance learning and retention.

Professional Development- Recommend ways to stay updated with industry trends and continue professional growth.

Networking- Highlight the importance of networking and building connections to support skill development.

Your comprehensive guidance will empower individuals to achieve their career goals.
"""

input_prompt3 = """
You are an expert ATS (Applicant Tracking System) scanner with a comprehensive knowledge of data science and ATS functionality. Your task is to evaluate the resume against the provided job description. First, provide the percentage of the match between the resume and the job description. Next, list the missing keywords. Finally, offer your overall assessment.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Generated Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Generated Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Generated Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")