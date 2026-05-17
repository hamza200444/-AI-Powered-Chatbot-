"""Generate chatbot replies from user input using the trained classifier."""

import random

from .error import ERROR_RESPONSES
from .text_processing import preprocess

CONFIDENCE_THRESHOLD = 0.20


def get_bot_response(user_input, classifier, vectorizer, responses):
    parts = [part.strip() for part in user_input.split(" and ") if part.strip()]
    if not parts:
        return random.choice(ERROR_RESPONSES)

    lines = []
    for part in parts:
        processed = preprocess(part)
        features = vectorizer.transform([processed])
        probabilities = classifier.predict_proba(features)[0]
        best_index = probabilities.argmax()
        confidence = float(probabilities[best_index])
        tag = classifier.classes_[best_index]

        if confidence >= CONFIDENCE_THRESHOLD and tag in responses:
            lines.append(random.choice(responses[tag]))
        else:
            lines.append(random.choice(ERROR_RESPONSES))

    return "\n".join(lines) if len(lines) > 1 else lines[0]
