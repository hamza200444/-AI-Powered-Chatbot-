import pyttsx3

_engine = pyttsx3.init()
_engine.setProperty("rate", 150)
_engine.setProperty("volume", 1.0)


def speak(text: str, verbose: bool = False) -> None:
    """Speak text aloud. Set verbose=True only if the caller does not print the reply."""
    if verbose:
        print(f"Bot: {text}")
    _engine.say(text)
    _engine.runAndWait()
