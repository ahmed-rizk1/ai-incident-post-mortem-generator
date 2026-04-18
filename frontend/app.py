import streamlit as st
import requests
import json

st.set_page_config(
    page_title="AI Post-Mortem Generator",
    page_icon="🐛",
    layout="centered"
)

st.title("🐛 AI Incident Post-Mortem Generator")
st.markdown("Paste chaotic logs and Slack conversations below. The AI will analyze the chaos and construct a highly professional engineering post-mortem document.")

import os

API_URL = os.getenv("API_URL", "http://localhost:8000/api/incident/generate")

with st.form("incident_form"):
    raw_logs = st.text_area("Paste Logs / Chat / Chaos Here:", height=250, placeholder="[10:04 AM] John: Production is down!?\n[10:05 AM] ERROR: Connection refused to DB cluster...")
    submitted = st.form_submit_button("Generate Professional Post-Mortem")

if submitted:
    if not raw_logs.strip():
        st.warning("Please paste some logs or chat history!")
    else:
        with st.spinner("Analyzing incident data..."):
            try:
                response = requests.post(
                    API_URL, 
                    json={"raw_logs": raw_logs},
                    stream=True
                )
                
                if response.status_code == 400:
                    st.error(f"Configuration error: {response.json().get('detail', 'Bad Request')}")
                elif response.status_code != 200:
                    st.error(f"Error: {response.text}")
                else:
                    st.subheader("💡 Generated Post-Mortem")
                    output_placeholder = st.empty()
                    full_response = ""
                    
                    for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                        if chunk:
                            full_response += chunk
                            output_placeholder.markdown(full_response)
            except Exception as e:
                st.error(f"Could not connect to the backend server. Is it running? Error: {str(e)}")
