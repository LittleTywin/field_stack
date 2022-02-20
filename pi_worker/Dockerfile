FROM python:3.10.2-alpine3.15

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt

RUN adduser --disabled-password --no-create-home app && \
    addgroup -g 997 gpio && \
    adduser app gpio

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt

COPY ./code /code
WORKDIR /code

ENV PATH "/py/bin:$PATH"

USER app

CMD [ "python","run.py" ]