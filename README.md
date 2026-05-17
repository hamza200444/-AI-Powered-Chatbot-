# 🎓 University ML Chatbot

An intent-based University AI Chatbot developed using **Python, NLTK, TF-IDF, and Logistic Regression** to answer student queries related to admissions, fees, scholarships, exams, departments, hostel, transport, and more.

The chatbot supports:
- 💬 CLI Chat
- 🖥 GUI Interface (Tkinter)
- 🌍 Multilingual Translation
- 🎤 Speech-to-Text
- 🔊 Text-to-Speech
- 🤖 Confidence-based fallback responses

---

## 🚀 Features

- Intent classification using TF-IDF + Logistic Regression
- NLP preprocessing with NLTK
- Multilingual translation support
- Speech-enabled interaction
- GUI and terminal-based chat modes
- Structured training dataset using `intents.json`
- Fallback responses for low-confidence predictions

---

## 🛠 Tech Stack

- Python
- NLTK
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Tkinter
- SpeechRecognition
- pyttsx3

---

## 📂 Project Structure

```text
AI testing/
├── intents.json
├── run_cli.py
├── run_gui.py
├── run_translator.py
├── chatbot/main/
│   ├── model.py
│   ├── response.py
│   ├── text_processing.py
│   ├── train.py
│   └── index.py
```

---

## ⚙️ Installation

```powershell
python -m pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

---

## ▶️ Run Project

| Command | Description |
|----------|-------------|
| `python run_cli.py` | Run terminal chatbot |
| `python run_gui.py` | Launch GUI chatbot |
| `python run_translator.py` | Run multilingual chatbot |

---

## 🧠 Machine Learning Workflow

User Input → NLP Preprocessing → TF-IDF Vectorization → Logistic Regression → Intent Prediction → Response Generation

---

## 📸 Screenshots

(Add your screenshots here)

---

## 💡 Sample Questions

- How do I apply for admission?
- Tell me about scholarships
- What is the fee structure?
- Library timing?
- How was this chatbot built?

---

## 🔮 Future Improvements

- Web-based deployment
- Database integration
- Deep learning intent classification
- Voice assistant enhancement
- Real university API integration

---

## 👨‍💻 Author

Muhammad Hamza Shahzad
