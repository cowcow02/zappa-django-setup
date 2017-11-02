FROM lambci/lambda:build-python3.6

MAINTAINER "Your Name" <your_name@example.com>

RUN mkdir /code
WORKDIR /code
RUN pip install invoke
