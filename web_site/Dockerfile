FROM python:3-alpine
USER root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /home/test/Desktop/web_site

RUN python -m pip install django

RUN python -m pip install requests

COPY . .

CMD python3 manage.py runserver 127.0.0.1:8000

CMD python3 test_api.py
