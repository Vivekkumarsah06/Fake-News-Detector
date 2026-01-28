import streamlit as st
import joblib
import re
from nltk.tokenize import sent_tokenize

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

st.title("📰 Fake News Detector for Students")

news = st.text_area("Paste news article here")

if st.button("Analyze"):
    label, score = predict_with_credibility(news)
    summary = summarize_text(news)

    st.write("Prediction:", label)
    st.write("Credibility Score:", score, "%")
    st.subheader("Summary")
    st.write(summary)
