# 📰 Fake News Detector for Students

Misinformation spreads quickly through online news and social media.
This project is an AI-based solution that helps students identify fake news
by analyzing articles, providing a credibility score, and generating a
concise and trustworthy summary.

---

## 🚀 Features
- Fake / Real news classification
- Credibility (confidence) score
- Automatic news summarization
- Simple and user-friendly interface
- Built for students and beginners

---

## 🛠️ Tech Stack
- Python
- Machine Learning (Logistic Regression)
- Natural Language Processing (TF-IDF, NLTK)
- Streamlit
- Google Colab (for model training)

---

## 📂 Project Structure
Fake-News-Detector/
│
├── app.py
├── fake_news_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md


---

## ▶️ How to Run the Project Locally
1. Download or clone this repository
2. Install required libraries:


pip install -r requirements.txt

3. Download NLTK data:


python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

4. Run the application:


streamlit run app.py


---

## 📊 Output
- Predicts whether the news is Fake or Real
- Shows a credibility score (percentage)
- Generates a concise summary of the news article

---

## 🎓 Use Case
This project helps students and general users avoid the spread of
misinformation by providing an easy-to-use fake news detection system.

---

## 👨‍💻 Author
**Vivek Kumar**
