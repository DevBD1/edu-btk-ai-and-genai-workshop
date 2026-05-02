from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("ChatGPT API Uygulamasi")
prompt = st.text_input("Soru:")

if prompt:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
    )
    st.write(response.choices[0].message.content)