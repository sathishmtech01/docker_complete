FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /python
WORKDIR /python
ADD requirements.txt /python/
RUN pip install -r requirements.txt
ADD . /python/