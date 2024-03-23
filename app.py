# Import convention

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json




# from promptFunctions import prompt
# from promptFunctions import returnSmile

from functions import getContentFromLink
from functions import getMetaData

from promptFunctions import getGPTResponse

from calculateWeights import calculateWeights
from calculateWeights import returnEmoji



load_dotenv()

GPT_API_KEY = os.getenv('GPT_API_KEY')

client = OpenAI(
    # This is the default and can be omitted
    api_key=GPT_API_KEY
)

st.write("""
# Calitatea stirii
""")

link = st.text_input('Link la articolul stirii')



if st.button('Verifica calitatea stirii'):
    content = getContentFromLink(link)
    metadata = getMetaData(link)
    gptResponse = getGPTResponse(content , metadata["title"])
    data = {
        "grammar":gptResponse["grammar"],
        "discriminatory":gptResponse['discriminatory'],
        "morbid":gptResponse['morbid'],
        "corellency":gptResponse['corellency'],
        "questions": gptResponse['questions'],
        "emotion":gptResponse['emotion']
    }
    weight = calculateWeights(data)
    emoji = returnEmoji(weight)
    st.write(weight)
    st.subheader(emoji)
    st.write(data)
