import streamlit as st
from langchain.llms import OpenAI
st.title('🦜🔗 Quickstart App')
# openai_api_key = st.sidebar.text_input('OpenAI API Key')
openai_api_key = "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"
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))
with st.form('my_form'):
  text = st.text_area('Enter text:', '...')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)