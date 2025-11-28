import json

import streamlit as st

from parser import extract_text_from_pdf_file
from rewrite_engine import analyze_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🧠",
    layout="centered",
)


st.title("🧠 AI Resume Analyzer & Rewriter")
st.write(
    "Upload your resume as a PDF and let AI analyze strengths, weaknesses, "
    "suggest missing skills, and rewrite your professional summary."
)

with st.sidebar:
    st.header("How it works")
    st.markdown(
        """
1. Upload your resume (PDF)  
2. Click **Analyze Resume**  
3. Review AI insights + ATS score  
4. Download the JSON report  
        """
    )
    st.caption("Make sure your `OPENAI_API_KEY` environment variable is set.")


uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    if st.button("🔍 Analyze Resume"):
        try:
            with st.spinner("Extracting text from your resume..."):
                text = extract_text_from_pdf_file(uploaded_file)

            if not text.strip():
                st.error("Could not extract any text from the PDF. Is it a scanned image?")
            else:
                with st.spinner("Analyzing with AI..."):
                    insights = analyze_resume(text)

                st.success("Analysis complete! 🎉")

                ats_score = insights.get("ats_score", "N/A")
                st.subheader("ATS Optimization Score")
                st.metric("Score", f"{ats_score}")

                strengths = insights.get("strengths", [])
                weaknesses = insights.get("weaknesses", [])
                recommended_skills = insights.get("recommended_skills", [])
                rewritten_summary = insights.get("rewritten_summary", "")

                if strengths:
                    st.subheader("💪 Strengths")
                    for s in strengths:
                        st.markdown(f"- {s}")

                if weaknesses:
                    st.subheader("⚠️ Weaknesses / Gaps")
                    for w in weaknesses:
                        st.markdown(f"- {w}")

                if recommended_skills:
                    st.subheader("📌 Recommended Skills to Add")
                    for skill in recommended_skills:
                        st.markdown(f"- {skill}")

                if rewritten_summary:
                    st.subheader("📝 Rewritten Summary")
                    st.write(rewritten_summary)

                st.subheader("📦 Raw JSON Output")
                st.code(json.dumps(insights, indent=2), language="json")

                st.download_button(
                    label="⬇️ Download JSON report",
                    data=json.dumps(insights, indent=2),
                    file_name="resume_ai_analysis.json",
                    mime="application/json",
                )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
else:
    st.info("Upload a PDF resume to get started.")

