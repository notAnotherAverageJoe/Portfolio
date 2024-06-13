import streamlit as st
import pandas as pd

def show_certifications():
    st.title("Certifications")

    try:
        df = pd.read_csv("certifications.csv")
        
        for index, row in df.iterrows():
            st.subheader(row["title"])
            st.write(f"Institution: {row['institution']}")
            st.write(f"Year: {row['year']}")
            image_path = "images/" + row["image"]
            st.image(image_path, caption=row["title"], width=600)
            st.markdown("---")
    except FileNotFoundError:
        st.warning("No certifications file found. ")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    show_certifications()
