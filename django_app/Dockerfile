FROM python:3.10.2-alpine3.15

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client pcre-dev

RUN apk add --update --no-cache --virtual .build-deps \
        build-base postgresql-dev musl-dev linux-headers python3-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .build-deps

RUN adduser --disabled-password --no-create-home app && \
    addgroup -g 997 gpio && \
    adduser app gpio && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R app:app /data && \
    chmod -R 755 /data

COPY ./code /code

COPY ./scripts /scripts
RUN chmod +x /scripts/*

WORKDIR /code

ENV PATH="/scripts:/py/bin:$PATH"

USER app

EXPOSE 8000