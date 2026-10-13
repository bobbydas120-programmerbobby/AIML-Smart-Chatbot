"""AIML Smart Chatbot — Python entry point."""

from pathlib import Path
import sys

import aiml

BASE_DIR = Path(__file__).resolve().parent
AIML_FILE = BASE_DIR / "aiml" / "standard.aiml"


def create_chatbot():
    """Create the AIML kernel and load the conversation rules."""
    if not AIML_FILE.is_file():
        raise FileNotFoundError(
            f"AIML file not found: {AIML_FILE}\n"
            "Make sure aiml/standard.aiml exists."
        )

    kernel = aiml.Kernel()
    kernel.learn(str(AIML_FILE))
    return kernel


def main():
    """Run an interactive terminal conversation."""
    try:
        kernel = create_chatbot()
    except Exception as error:
        print(f"Could not start the chatbot: {error}")
        sys.exit(1)

    print("=" * 45)
    print("       Welcome to AIML Smart Chatbot!")
    print("=" * 45)
    print("Type 'exit', 'quit', or 'bye' to end the chat.")
    print("Bot: Hello! How can I help you today?")

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Have a great day.")
            break

        if not user_input:
            print("Bot: Please type a message.")
            continue

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Bot: Goodbye! Have a great day.")
            break

        response = kernel.respond(user_input)
        if not response:
            response = (
                "I'm not sure how to answer that yet. "
                "Try asking me about Python, AIML, or my features."
            )

        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
