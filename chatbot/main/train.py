from .model import load_intents, prepare_data, train_model
from .response import get_bot_response

_intents = load_intents()
_corpus, _labels, _responses = prepare_data(_intents)
_classifier, _vectorizer = train_model(_corpus, _labels)


def get_ai_response(user_input: str) -> str:
    return get_bot_response(user_input, _classifier, _vectorizer, _responses)
