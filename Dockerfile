FROM python:3-alpine

RUN apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/main --no-cache py3-psycopg2

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY manage.py /
COPY cristoreferendum /cristoreferendum
COPY whoiscristo /whoiscristo

ENV PRODUCTION=1
EXPOSE 8080
CMD python manage.py migrate && /usr/local/bin/gunicorn cristoreferendum.wsgi --workers 8 -b :8080