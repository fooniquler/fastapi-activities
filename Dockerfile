FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app/ ./app/
