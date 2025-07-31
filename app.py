import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.exceptions import OutputParserException
from requests.exceptions import RequestException

load_dotenv()

# Load environment variables
langchain_key = os.getenv("LANGCHAIN_API_KEY")
groq_api_key1 = os.getenv("GROQ_API_KEY")

# Set required LangChain env vars
if langchain_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot"
else:
    st.warning("LANGCHAIN_API_KEY not found in environment.")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the question to the best of your ability."),
    ("user", "question: {question}")
])

def generate_answer(question, max_tokens, temperature, llm, api_key):
    try:
        if not api_key:
            raise ValueError("API key is required to call the Groq model.")

        model = ChatGroq(
            model=llm,
            groq_api_key=api_key,
            temperature=temperature,
        )
        output_parser = StrOutputParser()
        chain = prompt | model | output_parser
        answer = chain.invoke({"question": question})
        return answer
    except OutputParserException:
        return "There was an error parsing the output. Please try again with a different question."
    except RequestException as e:
        return f"Network error occurred: {str(e)}"
    except Exception as e:
        return f"An error occurred while generating the answer: {str(e)}"

# Streamlit UI
st.title("Q&A Chatbot")

# Sidebar: API key, model selection, temperature, max tokens
st.sidebar.title("User Input")
api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")
llm = st.sidebar.selectbox(
    "Select a model",
    ["gemma2-9b-it", "llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768"],
)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.6)
max_tokens = st.sidebar.slider("Max Tokens", min_value=20, max_value=300, value=150)

# Main input
st.write("Ask a question:")
user_input = st.text_input("Question", placeholder="Type your question here...")

# Handle empty input and missing API key
if user_input:
    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
    else:
        response = generate_answer(user_input, max_tokens, temperature, llm, api_key)
        st.write(response)
else:
    st.write("Please enter a question to get an answer.")
