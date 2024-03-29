FROM python:3.8-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN apk update && apk add gcc build-base libpq-dev
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]