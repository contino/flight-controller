FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./src ./src

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 "src.entrypoints.cloudrun:app"