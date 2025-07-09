# quote_api/Dockerfile

FROM python:3.9-slim
RUN apt-get update && apt-get install -y curl

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/