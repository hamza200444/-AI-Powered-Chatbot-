import string

import nltk
from nltk.corpus import stopwords

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

_STOP_WORDS = set(stopwords.words("english"))
_PUNCTUATION = set(string.punctuation)


def preprocess(text: str) -> str:
    text = text.lower()
    text = "".join(ch for ch in text if ch not in _PUNCTUATION)
    tokens = [word for word in text.split() if word not in _STOP_WORDS]
    return " ".join(tokens)
