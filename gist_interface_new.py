import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import urllib.request

def app():
    st.image("images/logo.png", width=200)
    st.markdown('<p class="header">Your Text</p>', unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    
    st.write('# Left Section')
    input_selection = left_column.selectbox('Select input type', ['Text', 'URL', 'PDF'])
    
    if input_selection == 'Text':
        txt = left_column.text_area("Insert your text here")
        if st.button('Submit Text'):
            result = parse_txt(txt)
            st.write(result)

    elif input_selection == 'URL':
        url = left_column.text_input("Insert the URL here")
        if st.button('Submit URL'):
            result = parse_url(url)
            st.write(result)

    elif input_selection == 'PDF':
        uploaded_file = st.file_uploader("Upload a file")
        if uploaded_file is not None:
            if st.button('Submit PDF'):
                result = parse_pdf(uploaded_file.read())
                st.write(result)
                
    if st.button('Publish'):
        #save to db
        pass

    # Right Section
    st.write('# Right Section')
    st.write("News Feed Here")

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