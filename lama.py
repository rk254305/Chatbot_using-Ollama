from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
##Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Rag_Groq"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
## prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant.please response to the user queries."),
        ("user","Question:{question}")
    ]
)

##streamlit framework
st.set_page_config(page_title="LangChain Chatbot", page_icon="🤖")
st.title("🤖 LangChain Chatbot")

input_text = st.text_input("Enter your message")

#openAi llm
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))