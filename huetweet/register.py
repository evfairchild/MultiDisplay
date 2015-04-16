#!/usr/bin/env python

import colorsys
import json
import logging
import os
import select
import socket
import sys
import time

import backoff
import websocket

from websocket._exceptions import WebSocketConnectionClosedException

from phue import Bridge


BRIDGE_HOST = os.environ['BRIDGE_HOST']
BRIDGE_USERNAME = os.environ.get('BRIDGE_USERNAME', 'a549f459bca9bc63e41e0aee681e09b2')
WEBSOCKET_URL = os.environ.get('WEBSOCKET_URL', 'ws://g6.local:8888/websocket')


class Disconnected(Exception):
    pass


# api = bridge.get_api()
# api.keys()
# api['groups']
# api['lights']

# bridge.lights[0].on
# bridge.lights[0].name
# bridge.lights[0].light_id
# bridge.lights[0].hue
# bridge.lights[0].effect

# print [[l.light_id, l.name] for l in bridge.lights]

MAX = 65536

MAX_BRIGHTNESS = 256


class HueController(object):
    def __init__(self):
        self.value = 0
        self.increment = 10000

        self.brightness = 128
        self.is_on = False

        self._ws = None

        self.bridge = Bridge(ip=BRIDGE_HOST, username=BRIDGE_USERNAME)

    def run(self):
        print self.bridge.register_app()

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    while True:
        try:
            logger = logging.getLogger(__name__)
            logger.info('starting Hue Controller')

            controller = HueController()
            controller.run()
        except Exception, exc:
            logger = logging.getLogger(__name__)
            logger.exception(exc)

            time.sleep(10)
