import streamlit as st
import joblib
import re
import nltk

# Download required NLTK resources (for Streamlit Cloud)
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

# Load trained model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_text(text):
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text.lower()

def predict_with_credibility(news):
    news = clean_text(news)
    vec = vectorizer.transform([news])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]

    if pred == 1:
        return "REAL", round(float(prob[1] * 100), 2)
    else:
        return "FAKE", round(float(prob[0] * 100), 2)

def summarize_text(text, max_sentences=2):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:max_sentences])

# ---------- Streamlit UI ----------
st.title("📰 Fake News Detector for Students")

news = st.text_area("Paste news article here")

if st.button("Analyze"):
    if news.strip() == "":
        st.warning("Please paste a news article")
    else:
        label, score = predict_with_credibility(news)
        summary = summarize_text(news)

        st.write("Prediction:", label)
        st.write("Credibility Score:", score, "%")

        st.subheader("Summary")
        st.write(summary)
