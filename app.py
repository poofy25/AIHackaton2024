# Import convention
import streamlit as st

st.write("""
# Calitatea stirii
""")

link = st.text_input('Link la articolul stirii')

st.write("""
*sau*
""")
text = st.text_area('Continutul stirii')


if st.button('Verifica calitatea stirii'):
    st.write(text)