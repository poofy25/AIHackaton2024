
import streamlit as st

st.set_page_config(
    page_title="Media Detectives",
    page_icon="./assets/logo.png",
)

from functions import getContentFromLink
from functions import getMetaData

from promptFunctions import getGPTResponse

from calculateWeights import calculatePercentage
from calculateWeights import returnEmoji

from details import getDetails

from blacklist import checkIfBlacklisted


st.title("Media Detectives")

st.subheader("Check the quaility of news articles")

link = st.text_input('Link to the news article')


if st.button('Verify quality'):
    content = getContentFromLink(link)
    metadata = getMetaData(link)
    gptResponse = getGPTResponse(content , metadata["title"])
    isBlackListed = checkIfBlacklisted(link)
    data = {
        "grammar":gptResponse["grammar"],
        "discriminatory":gptResponse['discriminatory'],
        "morbid":gptResponse['morbid'],
        "corellency":gptResponse['corellency'],
        "questions": gptResponse['questions'],
        "emotion":gptResponse['emotion'],
        "blackListed":isBlackListed
    }
    percentage = calculatePercentage(data)
    emoji = returnEmoji(percentage)
    details = getDetails(data, emoji["text"])
    st.title(f"Article quality : {emoji["emoji"]}  ({emoji["text"]})")
    st.write(f"Precentage : {percentage} % (quality)")
    st.subheader("Why ?")
    st.write(details)
    print(data)

