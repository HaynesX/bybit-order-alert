FROM python:3.8

RUN mkdir -p /home/bybit-order-alert
WORKDIR /home/bybit-order-alert

COPY requirements.txt /home/bybit-order-alert

RUN pip install -r /home/bybit-order-alert/requirements.txt

COPY . /home/bybit-order-alert