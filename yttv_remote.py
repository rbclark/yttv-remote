#!/usr/bin/env python3

import RPi.GPIO as GPIO
import IRModule
import pychromecast
import traceback
from time import sleep
from collections import OrderedDict
from pychromecast.controllers.youtube_tv import YouTubeTVController

from google_oauth import GoogleOauth

from tv_controller import TVController

auth = GoogleOauth(token_file='.authorization')

TV_CONTROLLER = None

def remote_callback(code):
    global CHANNEL_INDEX
    if code == 0x609f8877:
        TV_CONTROLLER.prev_channel()
    elif code == 0x609f48b7:
        TV_CONTROLLER.next_channel()
    elif code == 0xe0e040bf:
        # Power on or off depending on current state
        TV_CONTROLLER.toggle_power()
    elif code == 0x609f20df:
        TV_CONTROLLER.number_pressed('1')
    elif code == 0x609fa05f:
        TV_CONTROLLER.number_pressed('2')
    elif code == 0x609f609f:
        TV_CONTROLLER.number_pressed('3')
    elif code == 0x609fe01f:
        TV_CONTROLLER.number_pressed('4')
    elif code == 0x609f10ef:
        TV_CONTROLLER.number_pressed('5')
    elif code == 0x609f906f:
        TV_CONTROLLER.number_pressed('6')
    elif code == 0x609f50af:
        TV_CONTROLLER.number_pressed('7')
    elif code == 0x609fd02f:
        TV_CONTROLLER.number_pressed('8')
    elif code == 0x609f30cf:
        TV_CONTROLLER.number_pressed('9')
    elif code == 0x609f708f:
        TV_CONTROLLER.number_pressed('0')
    # else:
    #     print(hex(code))
    return

# Change to the name of your Chromecast
CAST_NAME = "Living Room TV"

# set up IR pi pin and IR remote object
irPin = 16
ir = IRModule.IRRemote()
# using 'DECODE' option for callback will print out
# the IR code received in hexadecimal
# this can used to get the codes for whichever NEC
# compatable remote you are using

# set up GPIO options and set callback function required
# by the IR remote module (ir.pWidth)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)      # uses numbering outside circles
GPIO.setup(irPin,GPIO.IN)   # set irPin to input
GPIO.add_event_detect(irPin,GPIO.BOTH,callback=ir.pWidth)

ir.set_verbose() # verbose option prints outs high and low width durations (ms)
print('Starting IR remote sensing using DECODE function and verbose setting equal True ')
print('Use ctrl-c to exit program')

try:
    while not auth.token:
        sleep(1)

    TV_CONTROLLER = TVController(CAST_NAME, YouTubeTVController(auth.get_request_session()))

    # sleep(5)
    print('Turning off verbose setting')
    ir.set_verbose(False)

    # change callback function to the function created above - remote_callback()
    print('Setting up callback')
    ir.set_callback(remote_callback)

    while True:
        TV_CONTROLLER.change_channel_timer()
        TV_CONTROLLER.channel_timer_count()
        sleep(0.5)

except Exception as error:
    print('Exception encountered %s' % error)
    traceback
    print('Removing callback and cleaning up GPIO')
    ir.remove_callback()
    GPIO.cleanup(irPin)
