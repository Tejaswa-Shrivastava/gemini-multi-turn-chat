Installation

1. Install the required package:
```bash
pip install google-generativeai
```
```
pip install --upgrade google-api-python-client
```

Setup

1. Get your API key:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create or select a project
   - Enable the Generative AI API
   - Create a new API key

2. Set the API key as an environment variable:
```bash
export GEMINI_API_KEY=your_api_key_here

Run the chatbot:
```bash
python gemini.py
```

The program will:
1. Ask for temperature (0.0 to 1.0)
2. Ask for top-p (0.0 to 1.0)
3. Start the chat conversation

To end the conversation, type 'exit'
