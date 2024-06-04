import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/selfie 2024.jpg", width=300)
    
with col2:
    st.title("Joseph Skokan")
    content = """
    Work in progress, things to be added later.
    
    """
    st.info(content)