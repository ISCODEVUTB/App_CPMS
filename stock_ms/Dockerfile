FROM python:3.9.3-slim-buster

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD python manage.py runserver 0.0.0.0:${PORT}



