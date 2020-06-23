FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV APP_MODULE="boker_api:app"

COPY ./boker_api /app/boker_api
COPY ./requirements.txt /app/

RUN pip install -r ./requirements.txt
