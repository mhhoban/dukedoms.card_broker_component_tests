FROM python:3.6.5-alpine3.7
RUN apk add --no-cache bash
RUN apk add --no-cache build-base
RUN apk add --no-cache postgresql-dev

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY utility_scripts/wait-for-it.sh /
COPY setup.py /

ARG service
COPY $service/ /$service

RUN pip3 install -e .

ARG service
WORKDIR /$service

CMD ["behave"]
