# 1. Base Image: Start with a fully pre-configured Linux environment with Python 3.12
FROM python:3.12-slim

# 2. Set the Working Directory inside our container to /app
WORKDIR /app

# 3. Copy our specific dependency files from Windows into the Linux container
COPY pyproject.toml uv.lock ./

# 4. Install 'uv' inside the container, then use it to install our dependencies system-wide
RUN pip install uv && uv pip install --system -r pyproject.toml

# 5. Copy the rest of our application code (like app.py) into the container
COPY . .

# 6. Expose port 8501 so the outside world can talk to Streamlit inside the box
EXPOSE 8501

# 7. No default CMD, docker-compose will override depending on the service
