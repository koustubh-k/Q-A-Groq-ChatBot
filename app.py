import streamlit as st
import langchain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot "
groq_api_key1= os.getenv("GROQ_API_KEY")

prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant ,please answer the question to the best of your ability."),
    ("user","question : {question}")
])

def generate_answer(question,max_tokens,temperature,llm,api_key=groq_api_key1):
    model=ChatGroq(
        model=llm,
        groq_api_key=api_key,
        temperature=temperature,
        )
    output_parser=StrOutputParser()
    chain=prompt | model | output_parser
    answer=chain.invoke({"question": question})
    return answer
    
st.title("Q&A Chatbot")

## sidebar for user input
st.sidebar.title("User Input")
api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

# dropdown for model selection
llm = st.sidebar.selectbox(
    "Select a model",
    ["gemma2-9b-it", "llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768"],
)

# slider for temperature
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.6)
max_tokens=st.sidebar.slider("Max Tokens",min_value=20,max_value=300,value=150)

#Main input box for question
st.write("Ask a question:")
user_input=st.text_input("Question", placeholder="Type your question here...")

if(user_input):
    response=generate_answer(user_input,max_tokens,temperature,llm,api_key)
    st.write(response)
else:
    st.write("Please enter a question to get an answer.")
