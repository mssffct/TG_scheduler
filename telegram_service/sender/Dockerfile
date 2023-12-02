FROM python:3.10.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /sender && apt-get update
WORKDIR /sender

COPY ./pyproject.toml /sender/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /sender