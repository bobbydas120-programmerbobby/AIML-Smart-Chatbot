# 🤖 AIML Smart Chatbot

A rule-based conversational chatbot built with **Python** and **Artificial Intelligence Markup Language (AIML)**. It demonstrates how AIML patterns and templates can be used to create a simple interactive chatbot.

## Features

- Greeting and conversational responses
- FAQs about Python and AIML
- Wildcard matching with `*`
- Dynamic responses using `<star/>`
- Response redirection using `<srai>`
- Fallback response for unknown questions
- Interactive command-line chat interface

## Technologies

- Python
- AIML
- Git and GitHub
- GitHub Codespaces

## Project structure

```text
AIML-Smart-Chatbot/
├── aiml/
│   └── standard.aiml
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Run in GitHub Codespaces

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> Note: `aiml` is an older package and may not install on every recent Python version. If installation fails, check the package compatibility and error message before changing dependencies.

### 3. Start the chatbot

```bash
python main.py
```

## Example conversation

```text
Bot: Hello! How can I help you today?

You: hello
Bot: Hello! Welcome to AIML Smart Chatbot.

You: what is aiml
Bot: AIML stands for Artificial Intelligence Markup Language...

You: bye
Bot: Goodbye! Have a great day.
```

## How it works

1. `main.py` creates an AIML interpreter.
2. The interpreter loads `aiml/standard.aiml`.
3. Each message is matched against an AIML pattern.
4. The matching template generates a response.
5. A wildcard category handles messages without a more specific match.

## Try these messages

- `hello`
- `what is your name`
- `what is AIML`
- `what is Python`
- `my name is Rahul`
- `howdy`

## Future improvements

- Add more AIML categories
- Add automated tests
- Store conversation history
- Build a web interface with Flask
- Add multilingual responses

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
