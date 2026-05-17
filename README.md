<img width="486" height="289" alt="Screenshot 2026-05-17 115012" src="https://github.com/user-attachments/assets/d1059465-e5ce-4f0c-bfe0-6d4f1211ba78" />
<img width="485" height="504" alt="Screenshot 2026-05-17 114925" src="https://github.com/user-attachments/assets/46789433-6a7d-41c8-b962-2c87dc0e432b" />
<img width="463" height="407" alt="Screenshot 2026-05-17 114953" src="https://github.com/user-attachments/assets/32379f0d-db4b-400e-9b9a-6000fa0ff961" />
<img width="744" height="185" alt="Screenshot 2026-05-17 115127" src="https://github.com/user-attachments/assets/5c7831ee-8b01-4c45-868f-979058fcf2df" />
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
