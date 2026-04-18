# 🐛 AI Incident Post-Mortem Generator

A Full-Stack AI utility designed for Site Reliability Engineers (SREs) and DevOps teams. This application takes chaotic server logs and panicked Slack/Teams conversations and automatically synthesizes them into a highly professional, strictly-formatted Incident Post-Mortem document using Large Language Models.
 
 ### it is live here ->  https://ai-incident-post-mortem-generator.onrender.com/
## 🚀 Features
- **Instant Analysis**: Parses chaotic, unstructured text logs and chat histories.
- **Smart Formatting**: Generates a standard Engineering Post-Mortem including:
  - Incident Summary
  - Root Cause Analysis
  - Resolution Steps
  - Timeline of Events
  - Action Items / Preventative Measures
- **Live Output Streaming**: Streams the LLM output in real-time for an incredibly fast and premium UX.
- **Model Agnostic**: Built using the OpenAI Python SDK and OpenRouter (Adapter Pattern), allowing seamless swapping of underlying AI models (GPT-4o, Claude 3.5, Llama 3) without code rewrites.

## 🛠️ Tech Stack
- **Frontend / UI**: [Streamlit](https://streamlit.io/)
- **Backend**: FastAPI & Python 3.12
- **Architecture**: Modular Monolith (Routes, Controllers, Factories)
- **AI Integrations**: OpenRouter API (`gpt-4o-mini`) via Factory Pattern
- **Package Management**: `uv`

---

## 💻 How to Run Locally

### Option A: Running with `uv` (Fastest for Development)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-postmortem-generator.git
   cd ai-postmortem-generator
   ```

2. **Set up Environment Variables:**
   Copy the example environment file and add your OpenRouter/OpenAI API key.
   ```bash
   cp .env.example .env
   # Edit .env and paste your OPENROUTER_API_KEY
   ```

3. **Install Dependencies:**
   This project uses `uv` for ultra-fast dependency management.
   ```bash
   uv sync
   ```

4. **Run the Backend API (FastAPI):**
   ```bash
   uv run uvicorn src.main:app --reload --port 8000
   ```

5. **Run the Frontend (Streamlit) in another terminal:**
   ```bash
   uv run streamlit run frontend/app.py
   ```

### Option B: Running with Docker (Production Environment)

1. **Build the Image:**
   ```bash
   docker build -t postmortem-gen .
   ```

2. **Run the Container:**
   ```bash
   docker run -p 8501:8501 --env-file .env postmortem-gen
   ```

Open your browser and navigate to `http://localhost:8501`.

---

## 🚢 Continuous Deployment (CI/CD)
This project is configured for Continuous Deployment via Render. Any commits pushed to the `main` branch trigger an isolated Docker build on Render's cloud infrastructure, instantly updating the live public endpoint.

## 📝 License
MIT License
