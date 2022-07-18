import time
from pybit import inverse_perpetual
from time import sleep
from datetime import datetime
import json
import pytz
import telebot
import os



TELEGRAM_SECRET_KEY = os.getenv('TELEGRAM_SECRET_KEY')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

BYBIT_SECRET_KEY = os.getenv('BYBIT_SECRET_KEY')
BYBIT_SECRET = os.getenv('BYBIT_SECRET')



bot = telebot.TeleBot(TELEGRAM_SECRET_KEY)



def handle_order(msg):
    orderID = msg["data"][0]["order_id"]
    side = msg["data"][0]["side"]
    entryOrExit = msg["data"][0]["last_exec_price"]
    orderStatus = msg["data"][0]["order_status"]
    isClose = msg["data"][0]["close_on_trigger"]
    createType = msg["data"][0]["create_type"]
    timestamp = msg["data"][0]["timestamp"]

    utcTimestampDatetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')

    local_timezone = pytz.timezone("Europe/London")
    local_datetime_converted = utcTimestampDatetime.replace(tzinfo=pytz.utc)
    local_datetime_converted = local_datetime_converted.astimezone(local_timezone)


    if side == "Buy":
        side == "Long"
    else:
        side == "Short"

    orderID = orderID[-5:]
    

    if orderStatus != "Filled":
        return

    telegramMessage = f"""
<b>Order: ${entryOrExit}</b>        
Direction: {side}
ID: {orderID}

UK: {local_datetime_converted.day}/{local_datetime_converted.month}/{local_datetime_converted.year} | {local_datetime_converted.hour}:{local_datetime_converted.minute}:{local_datetime_converted.second}
UTC: {utcTimestampDatetime.day}/{utcTimestampDatetime.month}/{utcTimestampDatetime.year} | {utcTimestampDatetime.hour}:{utcTimestampDatetime.minute}:{utcTimestampDatetime.second}
"""
    
    


    print(msg)

    bot.send_message(TELEGRAM_CHAT_ID, telegramMessage, parse_mode="HTML")









def poll_bybit_stream():
    ws_inverseP = inverse_perpetual.WebSocket(
        test=False,
        api_key=BYBIT_SECRET_KEY,
        api_secret=BYBIT_SECRET,
        ping_interval=40,  # the default is 30
        ping_timeout=20,  # the default is 10
        domain="bybit"  # the default is "bybit"
        )
    
    time.sleep(10)

    ws_inverseP.order_stream(
        handle_order
        )

    while True:
        sleep(1)


def main():
    poll_bybit_stream()


if __name__ == "__main__":
    main()