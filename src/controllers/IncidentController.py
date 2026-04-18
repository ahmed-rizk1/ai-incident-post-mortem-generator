from src.stores.llm.LLMProviderFactory import LLMProviderFactory
from src.helpers.config import config

class IncidentController:
    def __init__(self):
        self.llm_provider = LLMProviderFactory.get_provider("openrouter", config.OPENROUTER_API_KEY)

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

    def generate_post_mortem_stream(self, raw_logs: str):
        if not config.OPENROUTER_API_KEY or config.OPENROUTER_API_KEY == "your_openrouter_api_key_here":
            raise ValueError("OPENROUTER_API_KEY is not configured.")
        
        user_prompt = f"Here is the incident data:\n\n{raw_logs}"
        return self.llm_provider.generate_post_mortem_stream(self.system_prompt, user_prompt)
