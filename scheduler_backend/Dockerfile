FROM python:3.10.5

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir /app && apt-get update
WORKDIR /app

COPY ./pyproject.toml /app/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /app