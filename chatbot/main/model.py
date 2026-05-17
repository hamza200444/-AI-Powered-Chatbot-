"""Load intents, prepare training data, and train the classifier."""

import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from .text_processing import preprocess

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INTENTS_PATH = _PROJECT_ROOT / "intents.json"


def load_intents(path=None):
    intents_path = Path(path) if path else DEFAULT_INTENTS_PATH
    with open(intents_path, encoding="utf-8") as file:
        return json.load(file)


def prepare_data(intents):
    corpus = []
    labels = []
    responses = {}

    for intent in intents["intents"]:
        tag = intent["tag"]
        responses[tag] = intent["responses"]
        for pattern in intent["patterns"]:
            corpus.append(preprocess(pattern))
            labels.append(tag)

    return corpus, labels, responses


def train_model(corpus, labels):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(corpus)
    classifier = LogisticRegression(max_iter=1000)
    classifier.fit(features, labels)
    return classifier, vectorizer
