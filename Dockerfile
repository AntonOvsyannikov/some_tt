FROM gitlab.ubic.tech:4567/docker/python:3.7

ADD wait /usr/bin/waitc
RUN chmod +x /usr/bin/waitc

WORKDIR /srv

ENV PYTHONPATH=/srv/src
ENV PYTHONUNBUFFERED=1

ADD requirements.txt .
RUN python3.7 -m pip install -r requirements.txt


COPY src src/
