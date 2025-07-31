Groq-Powered Streamlit Q&A Chatbot
This is a basic, conversational Q&A chatbot built using Streamlit and powered by a Large Language Model (LLM) from Groq. The application allows users to interact with a model, providing a simple and fast chat interface.

Features
Groq LLM Integration: Uses the Groq API for high-speed, low-latency text generation.

Configurable Parameters: Users can easily select the LLM model, adjust temperature, and set the maximum number of tokens from the sidebar.

Conversational Memory: The chatbot maintains a conversation history, allowing it to respond to follow-up questions with context.

Streamlit UI: A clean and interactive web interface built with Streamlit, making it easy to use and deploy.

Secure API Key Handling: Uses a .env file for local development to keep API keys separate from the code.

Getting Started
Follow these steps to set up and run the application on your local machine.

Prerequisites
Python 3.8 or higher

Git

Installation
Clone the repository:

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

Create a virtual environment and activate it (recommended):

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate

Install dependencies:
The project uses a requirements.txt file to list all necessary libraries.

pip install -r requirements.txt

Configuration
The application requires a Groq API key to function.

Get a Groq API Key:

Sign up for a Groq account at https://groq.com/.

Navigate to the API keys section and create a new key.

Create a .env file:

In the root directory of your project, create a new file named .env.

Add your Groq API key to this file in the following format:

GROQ_API_KEY="YOUR_GROQ_API_KEY"
LANGCHAIN_API_KEY="YOUR_LANGCHAIN_API_KEY"

Note: Your .env file should be listed in .gitignore to prevent it from being committed to version control.

Running the Application
Once everything is set up, you can run the Streamlit application from your terminal:

streamlit run app.py

This will open a new tab in your web browser with the chatbot interface.

Deployment
This application is designed to be easily deployed on platforms like Streamlit Community Cloud.

GitHub Repository: Ensure your code is in a public GitHub repository. Do not commit your .env file.

Streamlit Cloud Secrets: When deploying on Streamlit Community Cloud, you will need to add your API key as a secret.

In the app deployment settings, add a new secret in the format GROQ_API_KEY="your_api_key_here". Streamlit will automatically handle this for your application.
