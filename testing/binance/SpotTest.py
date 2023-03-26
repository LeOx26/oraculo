#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

config_logging(logging, logging.DEBUG)

def message_handler(message):
    
    print(message['data'])


my_client = Client()
my_client.start()

my_client.instant_subscribe(
    stream=["linkusdt@ticker"],
    callback=message_handler
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()