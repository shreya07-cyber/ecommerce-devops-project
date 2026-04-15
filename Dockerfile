FROM python:3.10-slim

LABEL maintainer="tejalkunde"
LABEL description="E-Commerce Flask Application - DevOps Mini Project"
LABEL version="1.0"

# Set working directory
WORKDIR /app

# Copy requirements first (layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Expose Flask port
EXPOSE 5000

# Health check so Docker/Render knows the container is alive
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000')" || exit 1

# Run the app
CMD ["python", "demo_ecommerce/app.py"]
