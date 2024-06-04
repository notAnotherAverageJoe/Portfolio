import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/selfie 2024.jpg", width=300)
    
with col2:
    st.title("Joseph Skokan")
    content = """
    Joseph Skokan
Junior Software Engineer | Problem Solver | Veteran
Phone: 571-271-7383 | Email: joeskokan20@gmail.com |

As a proud veteran and dedicated junior software engineer, 
I bring a unique blend of discipline, critical thinking, 
and problem-solving skills to every project I undertake. 
My journey has equipped me with a solid foundation in various programming languages,
including Python and JavaScript, and a passion for continuous learning and innovation.

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
Education
A.A. in Apologetics
Liberty University, Lynchburg, VA, 2022

Electro-Mechanical Diploma
Tulsa Welding School, Jacksonville, FL, 2019

Professional Welder Diploma
Tulsa Welding School, Jacksonville, FL, 2018

Personal Training Certification
American Council on Exercise, Jacksonville, FL, 2017

Military Certificate of Completion
Security Forces Technical School, Lackland Air Force Base, TX, 2010

As a veteran, I have honed my skills in discipline,
leadership, and adaptability, which I now apply to my career in software engineering.
I am eager to bring my diverse background and technical expertise to a dynamic development team,
contributing to innovative projects and continuously advancing my skills in the field.
    
    """
    st.info(content)
    
    content2 ='''
    Below you will find a compilation of some Python projects have I completed!
    '''
st.write(content2)