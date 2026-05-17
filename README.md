# University ML Chatbot

Intent-based university assistant built for a **Machine Learning** course project. User messages are classified with **TF-IDF + Logistic Regression**, then answered from `intents.json`.

## Setup

```powershell

python -m pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

## Run

| Command | Purpose |
|---------|---------|
| `python run_cli.py` | Text chat in terminal (optional voice mode) |
| `python run_gui.py` | Graphical chat window (Tkinter) |
| `python run_translator.py` | Chat in Urdu/other languages via translation |

## Project structure

```
AI testing/
├── intents.json              # Training data: patterns + responses per intent
├── requirements.txt          # Python dependencies
├── run_cli.py                # Starts CLI (imports main.py)
├── run_gui.py                # Starts GUI
├── run_translator.py         # Starts multilingual CLI
├── main.py                   # CLI chat loop
├── speech_input.py           # Microphone → text (SpeechRecognition)
├── speech_output.py          # Text → speech (pyttsx3)
└── chatbot/
    └── main/
        ├── model.py          # Load intents, train classifier
        ├── text_processing.py # NLP preprocessing
        ├── response.py       # Predict intent + pick reply
        ├── train.py          # Pre-train model for CLI/translator
        ├── error.py          # Low-confidence fallback messages
        └── index.py          # Translator mode logic
```

## Adding intents

Edit `intents.json`: add a `tag`, several `patterns` (user phrases), and `responses`. Restart the app to retrain.

## Demo questions

- "How do I apply for admission?"
- "What is the fee structure?"
- "Tell me about scholarships"
- "Library timing?"
- "How was this chatbot built?"
