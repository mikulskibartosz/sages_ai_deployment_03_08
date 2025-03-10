FROM python:3.12.8-slim

WORKDIR /app
VOLUME /katalog

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
