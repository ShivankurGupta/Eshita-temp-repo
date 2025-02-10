import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

st.title("Smart Note Summarizer & To-Do Generator")

notes = st.text_area("Enter your notes:", "Finish the project report, Call the client, Prepare for the meeting.")

if st.button("Generate Summary and Tasks"):
    if notes:
        input_data = {"notes": notes}
        response = client.flow.execute("shivankur/notesummarizer", input_data)
        st.write(response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please enter some notes.")
