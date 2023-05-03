FROM python:3.10-slim

ENV PYTHONUNBUFFERED True
ENV BIGQUERY_EVENTS_TABLE=contino-squad0-fc.event_sourcing_table.events_data
ENV BIGQUERY_METRICS_TABLE=contino-squad0-fc.metric_sourcing_table.metrics_data

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./src ./src

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 "src.entrypoints.cloudrun:app"