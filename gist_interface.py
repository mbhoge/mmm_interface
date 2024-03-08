import streamlit as st
import re


def parse_pdf(pdf_file):
    # Parse the PDF file using pdfminer
    pdf_text = "pdftext"
    return pdf_text

def parse_txt(txt_file):
    # Read the text file and remove unnecessary characters and whitespace
    with open(txt_file, 'r') as f:
        txt_data = f.read()
        txt_data = re.sub(r'\s+', ' ', txt_data).strip()

    return txt_data

def parse_url(url):
    # Request the URL and get the HTML response
    html_text = "htmltext"
    return html_text

def get_length(text):
    return len(text)

st.title("Streamlit Content Analyzer")
st.write("This application allows you to analyze the content of a PDF, text file, or URL.")


# Create three columns
col1, col2, col3 = st.columns(3)

# Initialize session state
if "file_type" not in st.session_state:
    st.session_state.file_type = None

# Create a radio button in each column
if st.session_state.file_type is None or st.session_state.file_type == "PDF":
    pdf_option = col1.radio("Select file type:", ["PDF"], key="1")
if st.session_state.file_type is None or st.session_state.file_type == "Text file":
    txt_option = col2.radio("", ["Text file"], key="2")
if st.session_state.file_type is None or st.session_state.file_type == "URL":
    url_option = col3.radio("", ["URL"], key="3")

# Determine which option was selected
if pdf_option:
    st.session_state.file_type = "PDF"
elif txt_option:
    st.session_state.file_type = "Text file"
elif url_option:
    st.session_state.file_type = "URL"

# Add the text and length to the main page
pdf_text = "pdf"
txt_text = "txt"
html_text = "html"
text_length = get_length(pdf_text or txt_text or html_text)
main_page = st.empty()
main_page.write(f"Text: {pdf_text or txt_text or html_text}")
main_page.write(f"Length: {text_length}")