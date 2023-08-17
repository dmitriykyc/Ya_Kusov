FROM python:3.8

WORKDIR /ya_kusov_bot
COPY requirements.txt /ya_kusov_bot
RUN pip install -r requirements.txt
COPY . /ya_kusov_bot
