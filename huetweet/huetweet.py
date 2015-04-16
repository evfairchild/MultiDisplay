#!/usr/bin/env python
import json
import logging
import os
import select
import sys
import time

import backoff

from phue import Bridge
from util import get_rgb_from_hex

from zymbit.arduino.console import Console
from zymbit.client import Client
from zymbit.websocket import WebSocketConnectionClosedException


BRIDGE_HOST = os.environ.get('BRIDGE_HOST')
BRIDGE_USERNAME = os.environ.get('BRIDGE_USERNAME', 'a549f459bca9bc63e41e0aee681e09b2')


class Disconnected(Exception):
    pass


MAX = 65536
MAX_BRIGHTNESS = 256


class HueController(object):
    def __init__(self):
        self.client = Client(connected_callback=self.connected)

        if BRIDGE_HOST:
            self.bridge = Bridge(ip=BRIDGE_HOST, username=BRIDGE_USERNAME)
            self.bridge.connect()
        else:
            self.logger.warning('Not connecting to bridge')

        self.arduino = Console()

    @property
    def logger(self):
        return logging.getLogger(__name__)

    def connected(self):
        self.logger.debug('connected to websocket')

        self.client.send('subscribe', {
            'exchange': 'data',
            'routing_key': 'zymbit.mood.#',
        })

    def data(self, envelope):
        hexstr = envelope['params']['hex']
        r, g, b = get_rgb_from_hex(hexstr)

        self.set_arduino_color(r, g, b)

    def handle_message(self):
        try:
            payload = self.client.recv()
        except WebSocketConnectionClosedException:
            # the connection is closed
            self._ws = None
            return

        if payload is None:
            self.logger.warning('got an empty payload')
            return

        try:
            data = json.loads(payload)
        except TypeError:
            self.logger.error('unable to load payload={}'.format(payload))
            raise

        print 'data={}'.format(data)

        handler_fn = data.get('action')
        if handler_fn is None:
            self.logger.warning('no action in data={}'.format(data))
            return

        handler = getattr(self, handler_fn, None)
        if handler is None:
            self.logger.warning('no handler for handler_fn={}'.format(handler_fn))
            return

        return handler(data)

    @backoff.on_exception(backoff.expo, Disconnected, max_value=30)
    def loop(self):
        r, _, _ = select.select([self.client], [], [], 1.0)
        if self.client in r:
            self.handle_message()

    def run(self):
        while True:
            self.loop()

    def set_arduino_color(self, r, g, b):
        command = 'set_colors {} {} {}'.format(r, g, b)
        self.logger.debug('sending arduino command={}'.format(command))

        self.arduino.send(command)

    def set_color(self, color):
        self.value = color

        self.bridge.set_group(1, 'hue', self.value)


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
