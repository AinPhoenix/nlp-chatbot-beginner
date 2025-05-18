# NLP Chatbot (Beginner)

A simple Python chatbot that uses intent matching and sentiment analysis to chat with users.

## Features
- Responds to common questions using keywords
- Analyzes message sentiment for replies
- Easy to run and modify

## How It Works
- Checks your message for keywords to match a known intent
- If no intent matches, uses sentiment analysis (TextBlob) to reply positively or negatively

## Getting Started
### Requirements
- Python 3.x ([Download Python](https://www.python.org/downloads/))
- textblob (`pip install textblob`) ([TextBlob Docs](https://textblob.readthedocs.io/en/dev/))

### Installation
1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install textblob
   ```

## Usage
1. Run the chatbot:
   ```bash
   python project.py
   ```
2. Chat with the bot (type 'exit' to quit)

## Example
```
You: What are your hours?
Bot: We are open from 9 AM to 9 PM Monday to Friday.
```

## Customizing
- To add new intents or responses, open `project.py` and update the intents section.

## Project Structure
- `project.py`: Main chatbot code
- `README.md`: Project documentation

## License
MIT License

## Note
This project is for learning purposes.