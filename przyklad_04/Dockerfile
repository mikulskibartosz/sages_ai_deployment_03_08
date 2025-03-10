FROM python:3.12.8-slim as builder

WORKDIR /app

COPY ./requirements_build.txt .

RUN pip install -r requirements_build.txt

COPY . .

RUN python build.py

FROM python:3.12.8-slim

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY --from=builder /app/content.txt .
COPY . .

ENTRYPOINT [ "uvicorn", "main:app" ]
CMD ["--host", "0.0.0.0", "--port", "8000"]

