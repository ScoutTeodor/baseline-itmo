FROM python:3.9-slim

WORKDIR /app

# Копируем зависимости и конфиги
COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Добавляем переменные окружения
ENV TZ=UTC
ENV MISTRAL_API_KEY=${MISTRAL_API_KEY}
ENV TAVILY_API_KEY=${TAVILY_API_KEY}

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]