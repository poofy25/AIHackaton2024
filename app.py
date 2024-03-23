# Import convention
import streamlit as st
from openai import OpenAI
from functions import prompt
client = OpenAI(
    # This is the default and can be omitted
    api_key="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"
)

st.write("""
# Calitatea stirii
""")

link = st.text_input('Link la articolul stirii')

st.write("""
*sau*
""")
text = st.text_area('Continutul stirii')


if st.button('Verifica calitatea stirii'):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt + text,
            }
        ],
        model="gpt-4-turbo-preview",
    )
    st.write(chat_completion.choices[0].message.content)