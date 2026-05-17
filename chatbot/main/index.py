from deep_translator import GoogleTranslator

from chatbot.main.train import get_ai_response
from speech_output import speak


def run_translator_cli():
    print("University Chatbot — Translator Mode")
    print("Enter language code: en, ur, ar, fr, etc. (default: en)")
    chosen_lang = input("Language code: ").strip() or "en"
    print("\nType your message. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            if chosen_lang != "en":
                translated_input = GoogleTranslator(source=chosen_lang, target="en").translate(user_input)
            else:
                translated_input = user_input
        except Exception as exc:
            print("Translation to English failed:", exc)
            continue

        result = get_ai_response(translated_input)

        try:
            if chosen_lang != "en":
                result = GoogleTranslator(source="en", target=chosen_lang).translate(result)
        except Exception as exc:
            print("Translation failed:", exc)

        print("Bot:", result)
        try:
            speak(result, verbose=False)
        except Exception:
            pass


if __name__ == "__main__":
    run_translator_cli()
