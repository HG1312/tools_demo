# Modern, maintained base image (realistic for production).
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
COPY . .

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "src.app:app"]
