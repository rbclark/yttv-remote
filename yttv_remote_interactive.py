#!/usr/bin/env python3

import traceback
import threading
from time import sleep
from pychromecast.controllers.youtube_tv import YouTubeTVController

from google_oauth import GoogleOauth

from tv_controller import TVController

auth = GoogleOauth(token_file='.authorization')

TV_CONTROLLER = None

# Change to the name of your Chromecast
CAST_NAME = "SHIELD"

def wait_for_input():
    global TV_CONTROLLER
    while True:
        TV_CONTROLLER.number_pressed(input("Please input a channel: "))

try:
    while not auth.token:
        sleep(1)
    # Seed with first channel so we can start in the off state.
    TV_CONTROLLER = TVController(CAST_NAME, YouTubeTVController(auth.get_request_session()))

    threading.Thread(target=wait_for_input).start()

    while True:
        TV_CONTROLLER.change_channel_timer()
        TV_CONTROLLER.channel_timer_count()
        sleep(0.5)

except Exception as error:
    print('Exception encountered %s' % error)
    traceback.print_exception()
