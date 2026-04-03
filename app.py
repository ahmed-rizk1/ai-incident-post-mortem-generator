import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up page config
st.set_page_config(
    page_title="AI Post-Mortem Generator",
    page_icon="🐛",
    layout="centered"
)

# Configuration: Initialize OpenAI client with OpenRouter's Base URL
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

if not openrouter_api_key or openrouter_api_key == "your_openrouter_api_key_here":
    st.error("⚠️ OPENROUTER_API_KEY is not set. Please add it to your .env file.")
else:
    # OpenRouter uses the exact same interface as OpenAI
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_api_key,
    )

st.title("🐛 AI Incident Post-Mortem Generator")
st.markdown("Paste chaotic logs and Slack conversations below. The AI will analyze the chaos and construct a highly professional engineering post-mortem document.")

system_prompt = """
You are a Senior Site Reliability Engineer (SRE) at a top-tier tech company.
The user will provide messy logs, panicked Slack chats, or raw errors.
Your job is to analyze this and output a pristine, professional Engineering Incident Post-Mortem in Markdown.

Use this exact section format:
# 📝 Incident Summary
(Brief 2-3 sentence overview of what went wrong)

# 🕵️ Root Cause Analysis
(Technical explanation of why it failed)

# 🛠️ Resolution
(How the incident was fixed, based on the logs/chat)

# 📅 Timeline of Events
(Chronological list of what happened and when, if given)

# 🚀 Action Items
(3-5 preventative measures to ensure it never happens again)

Do NOT include any filler text like 'Here is your report'. Just output the markdown document directly.
"""

# The UI Form
with st.form("incident_form"):
    raw_logs = st.text_area("Paste Logs / Chat / Chaos Here:", height=250, placeholder="[10:04 AM] John: Production is down!?\n[10:05 AM] ERROR: Connection refused to DB cluster...")
    submitted = st.form_submit_button("Generate Professional Post-Mortem")

if submitted:
    if not openrouter_api_key or openrouter_api_key == "your_openrouter_api_key_here":
        st.error("Please configure your OpenRouter API key first!")
    elif not raw_logs.strip():
        st.warning("Please paste some logs or chat history!")
    else:
        with st.spinner("Analyzing incident data..."):
            try:
                # Stream the response for a better user experience
                response = client.chat.completions.create(
                    model="openai/gpt-4o-mini", # The openrouter model ID
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Here is the incident data:\n\n{raw_logs}"}
                    ],
                    stream=True,
                )
                
                st.subheader("💡 Generated Post-Mortem")
                
                # We use a placeholder to stream the markdown into
                output_placeholder = st.empty()
                full_response = ""
                
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        full_response += chunk.choices[0].delta.content
                        output_placeholder.markdown(full_response)
                        
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
