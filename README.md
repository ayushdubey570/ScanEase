# Scan Ease

**Scan Ease** is a web application built using Python and Streamlit that scans resumes to determine their ATS (Applicant Tracking System) score and provides insights. Users can also ask for suggestions on how to improve their resumes. The application leverages the Google Gemini API to fetch all the requests and provide personalized suggestions.

## Table of Contents
1. [Why Do We Need This?](#why-do-we-need-this)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Prerequisites](#prerequisites)
5. [Installation Guide](#installation-guide)
6. [Acknowledgments](#acknowledgments)
7. [Contact Information](#contact-information)
8. [Future Improvements](#future-improvements)


## Why Do We Need This?
In today's competitive job market, ensuring that your resume stands out and passes through Applicant Tracking Systems (ATS) is crucial. Many companies use ATS to filter resumes, and a significant number of resumes are rejected due to poor formatting or lack of relevant keywords. **Scan Ease** addresses this issue by analyzing resumes, providing an ATS score, and offering actionable insights to enhance the chances of getting noticed by recruiters.

## Features
- **Resume Scanning**: Upload a resume and receive an ATS score.
- **Insights**: Get detailed insights into the strengths and weaknesses of your resume.
- **Improvement Suggestions**: Ask for suggestions on how to improve your resume.
- **Google Gemini API Integration**: Utilizes the Google Gemini API to fetch requests and provide personalized suggestions.
- **User-Friendly Interface**: Interactive and intuitive interface built with Streamlit.

## Technologies Used
- **Python**: The core programming language used for building the application.
- **Streamlit**: Framework for creating the interactive web application.
- **Google Gemini API**: API used to fetch requests and provide suggestions.


## Prerequisites
Before you begin, ensure you have met the following requirements:
- **Python 3.10 or higher**: Make sure you have Python installed.
- **pip**: Python package installer should be available.

## Installation Guide
1. **Clone the repository**:
    ```sh
    git clone https://github.com/ayushdubey570/scanease.git
    cd scanease
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Streamlit application**:
    ```sh
    streamlit run app.py
    ```

4. **Access the application**:
    Open your web browser and navigate to `http://localhost:8501`

## Acknowledgments
Special thanks to:
- **Google** for providing the Google Gemini API.
- **Streamlit** for the excellent framework that made building the web application easier.
- **The open-source community** for their invaluable resources and support.

## Contact Information
If you have any questions, suggestions, or feedback, feel free to reach out:
- **Email**: ayushdubey570@gmail.com
- **GitHub**: [ayushdubey570](https://github.com/ayushdubey570)
- **LinkedIn**: [Ayush Dubey](https://www.linkedin.com/in/ayushdubey570/)

## Future Improvements
- **Enhanced Analysis**: Incorporate more metrics for a comprehensive resume analysis.
- **Multiple File Formats**: Support additional file formats like TXT.
- **Language Support**: Add support for resumes in different languages.
- **User Accounts**: Allow users to create accounts and save their resume analysis history.


