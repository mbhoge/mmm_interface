import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import urllib.request

def app():
    
    st.sidebar.image("images/machine-learning-examples-applications.png", width=200)
    # Object notation
    # Using object notation
    add_selectbox = st.sidebar.selectbox(
    "How would you like Upload the Content?",
    ("Text", "URL", "PDF")
    )
    if add_selectbox == 'PDF':
        pdf_input = st.sidebar.file_uploader("Upload a file")
    elif add_selectbox == 'URL':
        url_input = st.sidebar.text_input("Enter the URL")
    else:
        # Perform further processing with the text
        text_input = st.sidebar.text_area("Enter the text")
        
    submit_button = st.sidebar.button("Publish")
    if submit_button:
        # Perform action on submit
        pass
    
    st.markdown('<p class="title">MetaMorphous Minds</p>', unsafe_allow_html=True)
    row1 = st.columns(3)
    row2 = st.columns(3)
    i = 0
    for col in row1 + row2:
        tile = col.container()
        tile.write("Tile " + str(i))
        tile._text_area("NEWS TEXT")  


def parse_txt(txt):
    # your text parsing logic here
    return txt

def parse_url(url):
    # your url parsing logic here
    return url

def parse_pdf(file):
    # your pdf parsing logic here
    return file

if __name__ == "__main__":
    app()