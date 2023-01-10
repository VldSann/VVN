FROM python:3-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /home/test/Desktop/web_site

RUN python -m pip install django

COPY . .

CMD python3 manage.py runserver
