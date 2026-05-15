import streamlit as st
import PyPDF2
from textblob import TextBlob
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume & Interview Preparation Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #4facfe, #8e44ad);
    color: white;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #f1f1f1;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background-color: rgba(255,255,255,0.12);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    background-color: white;
    color: #4facfe;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
}

/* Download Buttons */
.stDownloadButton>button {
    background-color: white;
    color: #8e44ad;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 15px;
    border: none;
    margin-bottom: 15px;
}

/* Text Input */
textarea {
    color: black !important;
}

/* Headers */
h1, h2, h3, h4 {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    '<div class="main-title">AI Resume & Interview Preparation Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI-Powered Resume Analysis & Mock Interview System</div>',
    unsafe_allow_html=True
)

# =====================================================
# SAMPLE RESUME SECTION
# =====================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📄 Resume Templates")

resume_files = {
    "Data Scientist Resume": "Sample_Resume\data_scientist_sample.pdf",
    "Data Analyst Resume": "Sample_Resume\data_analyst_sample.pdf",
    "HR Resume": "Sample_Resume\HR_resume_sample.pdf",
    "ML Engineer Resume": "Sample_Resume\machine_learning_sample.pdf",
    "Web Developer Resume": "Sample_Resume\web_developer_sample.pdf"
}

for resume_name, file_path in resume_files.items():

    st.subheader(resume_name)

    try:
        with open(file_path, "rb") as pdf_file:

            st.download_button(
                label=f"⬇ Download {resume_name}",
                data=pdf_file,
                file_name=file_path.split("/")[-1],
                mime="application/pdf"
            )

    except:
        st.warning(f"{resume_name} file not found.")

st.info(
    "Download and edit these resume templates before uploading your own resume."
)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# RESUME UPLOAD
# =====================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📤 Upload Your Resume PDF",
    type=["pdf"]
)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# MAIN PROCESS
# =====================================================

if uploaded_file is not None:

    # ---------------- EXTRACT TEXT ----------------

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    resume_lower = resume_text.lower()

    # ---------------- SKILLS DATABASE ----------------

    skills_db = [
        "python",
        "machine learning",
        "deep learning",
        "data analysis",
        "sql",
        "java",
        "c++",
        "streamlit",
        "tensorflow",
        "pandas",
        "numpy",
        "web development",
        "html",
        "css",
        "javascript",
        "power bi",
        "communication",
        "leadership"
    ]

    # ---------------- DETECT SKILLS ----------------

    detected_skills = []

    for skill in skills_db:

        if skill in resume_lower:
            detected_skills.append(skill)

    # ---------------- ATS SCORE ----------------

    resume_score = len(detected_skills) * 10

    if resume_score > 100:
        resume_score = 100

    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("✅ Detected Skills")

    st.write(detected_skills)

    st.subheader(f"⭐ ATS Resume Score: {resume_score}/100")

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # MISSING SKILLS
    # =====================================================

    important_skills = [
        "python",
        "sql",
        "communication",
        "machine learning",
        "data analysis"
    ]

    missing_skills = []

    for skill in important_skills:

        if skill not in detected_skills:
            missing_skills.append(skill)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("📌 Suggested Skills")

    for skill in missing_skills:
        st.write("✔", skill)

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # GENERATE QUESTIONS
    # =====================================================

    questions = []

    # Python
    if "python" in detected_skills:

        questions.extend([
            "Explain the advantages of Python.",
            "What are Python lists and tuples?",
            "Explain object-oriented programming in Python."
        ])

    # Machine Learning
    if "machine learning" in detected_skills:

        questions.extend([
            "What is Machine Learning?",
            "Explain supervised and unsupervised learning.",
            "What is Random Forest Algorithm?",
            "Explain the train-test split concept."
        ])

    # Web Development
    if "web development" in detected_skills:

        questions.extend([
            "Explain frontend and backend development.",
            "What is responsive web design?",
            "Explain API integration."
        ])

    # Data Analysis
    if "data analysis" in detected_skills:

        questions.extend([
            "What is data analysis?",
            "Explain data preprocessing.",
            "What is data visualization?"
        ])

    # Power BI
    if "power bi" in detected_skills:

        questions.extend([
            "What is Power BI?",
            "Explain DAX functions."
        ])

    # HR Questions
    if "communication" in detected_skills:

        questions.extend([
            "Tell me about yourself.",
            "Why should we hire you?",
            "How do you handle teamwork?"
        ])

    # Data Scientist Role
    if (
        "machine learning" in detected_skills and
        "python" in detected_skills and
        "data analysis" in detected_skills
    ):

        questions.extend([
            "Explain the role of a Data Scientist.",
            "Explain bias and variance.",
            "What is feature engineering?"
        ])

    # AI/ML Engineer
    if (
        "tensorflow" in detected_skills or
        "deep learning" in detected_skills
    ):

        questions.extend([
            "What is Deep Learning?",
            "Difference between CNN and ANN?",
            "Explain activation functions."
        ])

    # =====================================================
    # RANDOM MOCK INTERVIEW
    # =====================================================

    selected_questions = random.sample(
        questions,
        min(5, len(questions))
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("🎤 Mock Interview Round")

    answers = []

    for i, question in enumerate(selected_questions, 1):

        st.subheader(f"Question {i}")

        st.write(question)

        ans = st.text_area(
            f"Your Answer {i}",
            key=i
        )

        answers.append(ans)

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # ANALYZE INTERVIEW
    # =====================================================

    if st.button("Analyze Interview"):

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("🧠 Emotion Analysis & AI Feedback")

        total_polarity = 0

        for i, ans in enumerate(answers, 1):

            analysis = TextBlob(ans)

            polarity = analysis.sentiment.polarity

            total_polarity += polarity

            st.subheader(f"Answer {i}")

            st.write(f"Sentiment Score: {polarity}")

            if polarity > 0:
                st.success("Confident / Positive")

            elif polarity < 0:
                st.error("Nervous / Negative")

            else:
                st.warning("Neutral")

            # Feedback
            answer_length = len(ans.split())

            if answer_length > 20:
                st.info("Good detailed answer.")

            else:
                st.warning("Try to explain your answer in more detail.")

        # Overall Confidence Score
        average_polarity = total_polarity / len(answers)

        confidence_score = max(
            0,
            min(100, (average_polarity + 1) * 50)
        )

        st.subheader(
            f"⭐ Overall Confidence Score: {confidence_score:.2f}%"
        )

        st.markdown('</div>', unsafe_allow_html=True)