FROM python:3.8



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app


COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install --upgrade pip -r /usr/src/requirements.txt

COPY . /usr/src/app
