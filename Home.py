import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/selfie 2024.jpg", width=300)
    st.text("Joseph Skokan")
    st.text("Junior Software Engineer | Problem Solver | Veteran")
    st.text("Phone: 571-271-7383 | Email: joeskokan20@gmail.com")
    content1 = """
As a proud veteran and dedicated junior software engineer, 
I bring a unique blend of discipline, critical thinking, 
and problem-solving skills to every project I undertake. 
My journey has equipped me with a solid foundation in various programming languages,
including Python, Rust and JavaScript, and a passion for continuous learning and innovation.


    """
    st.info(content1)
    
    
with col2:
    st.title("Joseph Skokan")
    content = """

Project Highlight: BitBuddy Cryptocurrency Platform
BitBuddy is a cryptocurrency platform I developed using Flask,
enabling users to buy, sell, and stake cryptocurrencies while providing real-time market data.
This project showcases my skills in both frontend and backend development, 
as well as my ability to integrate external APIs for real-time data retrieval.

Key Features:

User authentication and portfolio management
Real-time market data integration
Cryptocurrency transactions and staking calculator
RESTful API for cryptocurrency management
Crypto mining game for user engagement
Technologies Used:

Flask, SQLAlchemy, PostgreSQL
HTML, CSS, JavaScript
External APIs for market data
Git, Linux, CMD
Technical Skills
Programming Languages: Python, JavaScript, Rust
Web Development: HTML, CSS, Flask, SQLAlchemy
Databases: SQL, PostgreSQL
Tools: Git, Linux, Command Line
Software Development: Data structures, algorithms, debugging, testing
Soft Skills
Collaboration and teamwork
Effective communication
Problem-solving and critical thinking
Time management
Attention to detail
Adaptability and creativity

As a veteran, I have honed my skills in discipline,
leadership, and adaptability, which I now apply to my career in software engineering.
I am eager to bring my diverse background and technical expertise to a dynamic development team,
contributing to innovative projects and continuously advancing my skills in the field.
    
    """
    st.info(content)
    
    content2 ='''
    Below you will find a compilation of some Python projects have I either completed or am actively working on!
    '''
st.info(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:14].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        image_path = "images/" + row["image"]
        st.image(image_path, caption=row['title'], width=300)
        st.write(f"[Source Code]({row['url']})")

        
    
    
with col4:
    for index, row in df[14:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        image_path = "images/" + row["image"]
        st.image(image_path, caption=row['title'], width=300)
        st.write(f"[Source Code]({row['url']})")
        
        