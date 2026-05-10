# Automatic Resume Screening Tool

## Overview

The **Automatic Resume Screening Tool** is an AI-powered web application designed to simplify and speed up the recruitment process. The system analyzes uploaded resumes, extracts important information, compares candidate profiles, and ranks resumes based on relevance.

This project helps recruiters and HR teams quickly identify suitable candidates while reducing manual effort.

---

## Features

* Upload and analyze resumes
* Extract candidate information automatically
* Resume ranking based on matching criteria
* Candidate score generation
* FastAPI backend for API handling
* Next.js frontend for user interaction
* Data processing using Pandas
* Real-time server execution with Uvicorn

---

## Technologies Used

* **Python**
* **FastAPI**
* **Next.js**
* **Pandas**
* **Uvicorn**
* **VS Code**

---

## Project Structure

```bash
resume-screening-tool/
│
├── backend/
│   ├── main.py
│   ├── screening.py
│   ├── requirements.txt
│
├── frontend/
│   ├── pages/
│   ├── components/
│
├── resumes/
├── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <your-github-repo-link>
cd resume-screening-tool
```

### Backend Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup

```bash
npm install
npm run dev
```

---

## How It Works

1. User uploads resumes through the frontend.
2. Backend processes the resumes using Python and Pandas.
3. Candidate details and keywords are extracted.
4. Resumes are scored and ranked automatically.
5. Results are displayed on the dashboard.

---

## Objectives

* Automate resume shortlisting
* Reduce recruitment time
* Improve candidate filtering accuracy
* Provide an efficient screening workflow

---

## Future Enhancements

* AI-based skill matching
* NLP-powered resume analysis
* PDF report generation
* Database integration
* Admin dashboard analytics

---

## Author

**Thirumalini E**

---

## Acknowledgement

Special thanks to mentors for their support and guidance throughout the project development.

---

## License

This project is developed for educational and learning purposes.
