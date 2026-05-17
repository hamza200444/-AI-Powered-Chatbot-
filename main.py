"""Command-line chat loop with optional voice input."""

import sys

from chatbot.main.train import get_ai_response
from speech_input import get_voice_input
from speech_output import speak

sys.stdout.reconfigure(encoding="utf-8")


def main():
    print("University Assistant Chatbot (Machine Learning Project)")
    print("Type 'voice' for microphone mode, 'exit' to quit.\n")

    try:
        while True:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            if user_input.lower() == "voice":
                print("Voice mode — say 'stop' or 'exit' to return to typing.")
                while True:
                    spoken = get_voice_input()
                    if not spoken:
                        continue
                    cmd = spoken.strip().lower()
                    if cmd in ("stop", "exit"):
                        print("Leaving voice mode.")
                        break
                    response = get_ai_response(spoken)
                    print(f"Bot: {response}")
                    try:
                        speak(response, verbose=False)
                    except Exception:
                        pass
                continue

            response = get_ai_response(user_input)
            print(f"Bot: {response}")
            try:
                speak(response, verbose=False)
            except Exception:
                pass
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
