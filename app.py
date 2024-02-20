## Conversational Q&A Chatbot
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os


#load dotenv
load_dotenv()


## Function to load OpenAI model and get respones

def get_openai_responses(question):
    llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response=llm(question)
    return response


## Streamlit UI
st.set_page_config(page_title="Simple Q&A Chatbot")
st.header("Chat with me")

input=st.text_input("Input: ",key="input")
response=get_openai_responses(input)
submit=st.button("Ask the question")


## If ask button is clicke

if submit:
    st.subheader("The Response is")
    st.write(response)
