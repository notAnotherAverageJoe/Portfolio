import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

# Column 1: Profile and Summary
with col1:
    st.image("images/selfie 2024.jpg", width=300)
    st.markdown("<h3 style='text-align: center;'>Joseph Skokan</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Junior Software Engineer | Problem Solver | Veteran</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><strong>📞 Phone:</strong> 571-274-1493 | <strong>📧 Email:</strong> joeskokan20@gmail.com</p>", unsafe_allow_html=True)
    
    # Introduction with background styling
    content1 = """
    <div style="background-color:#1e464e; padding:10px; border-radius:5px;">
    As a proud veteran and dedicated junior software engineer, I bring a unique blend of discipline, critical thinking, and problem-solving skills to every project I undertake. 
    My journey has equipped me with a solid foundation in various programming languages, including Python, Rust, and JavaScript, and a passion for continuous learning and innovation.
    </div>
    """
    st.markdown(content1, unsafe_allow_html=True)
    
# Column 2: Project Highlights and Skills
with col2:
    st.title("Project Highlights")
    
    # Project 1 Highlight
    content = """
    ### Property Preservation Plus
    **PPP** is a full-stack property management site that can handle companies, tenants, units, maintenance requests, and more. It features user access management to secure pages and uses higher-order components (HOCs) for security levels.
    
    ### BitBuddy Cryptocurrency Platform
    **BitBuddy** is a cryptocurrency platform built with Flask, enabling users to buy, sell, and stake cryptocurrencies while accessing real-time market data. This project highlights my skills in frontend and backend development and API integration.
    """
    st.markdown(content)

    # Technical Skills and Soft Skills with lists
    skills_content = """
    ### 🛠 Technical Skills
    - **Programming Languages**: Python, JavaScript, C, C#, Ruby, Erlang, Cobol, Perl
    - **Web Development**: React, HTML, CSS, Flask
    - **Databases**: SQL, PostgreSQL, MySQL, MongoDB
    - **Tools**: Git, Linux, Command Line
    - **Software Development**: Data structures, algorithms, debugging, testing
    
    ### 🌟 Soft Skills
    - Collaboration and teamwork
    - Effective communication
    - Problem-solving and critical thinking
    - Time management
    - Attention to detail
    - Adaptability and creativity
    """
    st.markdown(skills_content)

    # Personal statement
    personal_statement = """
    <div style="background-color:#1e464e; padding:10px; border-radius:5px; margin-top:10px;">
    As a veteran, I have honed my skills in discipline, leadership, and adaptability, which I now apply to my career in software engineering. I am eager to bring my diverse background and technical expertise to a dynamic development team, contributing to innovative projects and continuously advancing my skills.
    </div>
    """
    st.markdown(personal_statement, unsafe_allow_html=True)

# Project Gallery with Data
st.markdown("### 📂 Project Gallery")
st.markdown("Here are some of my completed or ongoing projects:")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

# Display projects in two columns
with col3:
    for index, row in df[:11].iterrows():
        st.markdown(f"#### {row['title']}")
        st.write(row["description"])
        st.image("images/" + row["image"], caption=row['title'], width=300)
        st.write(f"[Source Code]({row['url']})")
        st.markdown("---")

with col4:
    for index, row in df[11:].iterrows():
        st.markdown(f"#### {row['title']}")
        st.write(row["description"])
        st.image("images/" + row["image"], caption=row['title'], width=300)
        st.write(f"[Source Code]({row['url']})")
        st.markdown("---")
