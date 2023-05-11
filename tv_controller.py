from collections import OrderedDict
import pychromecast
from time import time

class TVController():
    def __init__(self, device_name, yttv_controller):
        self.channel_timer = 0
        self.device_name = device_name
        self.controller = yttv_controller
        chromecasts = pychromecast.get_chromecasts()
        self.cast = next(cc for cc in chromecasts if cc.device.friendly_name == self.device_name)
        self.cast.wait()
        self.cast.register_handler(self.controller)

        # For handling remote control
        self.button_press_time = None
        self.button_queue = ''

        self.channels = OrderedChannelDict(
            [
                ('3', 'LsXpBULs0Xo'), # WEDU PBS
                ('4', '5mDTOp9WS6M'), # WEDU PBS2
                ('7', 'OSlg3cF4UXc'), # ABC 7
                ('8', 'LES5_GxJfdg'), # NBC 8
                ('9', 'OOS_3X6WIMo'), # NBCLX
                ('10', 'beSs1S77QHc'), # 10 News
                ('11', 'gWnphzRqlAs'), # ABC 28
                ('12', 'UVMXZFtNDk4'), # ABC News Live
                ('13', 'AC4HOoWNMt8'), # FOX 13
                ('15', 'pwbQWAvDN_U'), # BTN
                ('16', 'uCG54kK5hXo'), # CBS Sports Network
                ('18', 'G-0O-AOaipc'), # NFL Network
                ('19', 'VHm4BVBP6So'), # Cozi
                ('20', 'gFyl838DxDA'), # Comet TV
                ('21', '0Jy_MdPASiA'), # Start TV
                ('22', 'KikCDgQ01co'), # Universo
                ('23', 'ltVfJCPu7KY'), # Telemundo Tampa
                ('24', 'f-nudN1rxLI'), # Turner Classic Movies
                ('25', '_u7za3b3W1M'), # Cartoon Network
                ('26', 'AvfwmRt2R-k'), # FS2
                ('28', 'RF8_ud7iZVU'), # TBS
                ('29', '33OcHAbWEvc'), # USA
                ('30', '5TE9OfoV05E'), # SYFY
                ('31', 'zAaMHaGWzmY'), # TNT
                ('32', 'kpwuG5TwJY0'), # ESPN
                ('33', 'iky6Bj8zcNk'), # ESPN2
                ('34', 'HWjfLB68ZLg'), # SEC Network
                ('35', 'ZWOZ335yfQE'), # ACC Network
                ('36', 'j46-7EKcbCE'), # ESPNU
                ('37', 'buuNxjALdfM'), # ESPNews
                ('38', 'UzApIq7mws0'), # MLB Network
                ('39', 'a_iWg49haok'), # FXX
                ('40', 'lfkf3ITXUy0'), # CNBC
                ('41', '6xvf4GyA83c'), # HLN
                ('42', '4HETjQzNpFk'), # CNN
                ('43', 'WGQE4JizI2U'), # FOX News
                ('44', 'a69jkGp8rjg'), # CW 44
                ('45', 'gdynBrl1XjY'), # E!
                ('46', 'PW8gNtxtPFs'), # CNBC World
                ('47', 'o3Okl4MUAtQ'), # FX
                ('48', '_PVFb12-gd4'), # Discovery Channel
                ('49', '1BragulqVyM'), # Smithsonian Channel
                ('50', 'i2LcYe_Q6Yw'), # Freeform
                ('51', 'imqFFeyv7gc'), # Golf Channel
                ('53', 'JLlRL9UfLgA'), # NBCSN
                ('54', 'zJ_YbpPD-Hk'), # NBA TV
                ('55', 'r0BG-u8AyVE'), # Food Network
                ('56', '46_CYKEBWKY'), # Travel Channel
                ('57', 'bZC65P615Iw'), # FS1
                ('58', 'u5RDGBdFkbU'), # Nat Geo
                ('59', '5-z7X15KRGo'), # HGTV
                ('61', 'piQKo31Edk4'), # Disney Channel
                ('62', 'w8XKPRD2b8w'), # Disney XD
                ('63', 'bL0BgLSK5ck'), # ID
                ('64', '88cuBsuOIjo'), # TLC
                ('65', 'TLgh78Lumas'), # AMC
                ('66', 'gSDHyuEYLy0'), # Bravo
                ('67', 'YP_hyVVR9f8'), # Animal Planet
                ('68', 'DjzkOw-3aEs'), # TYT Network
                ('69', '2h8XkKBLw3Y'), # Oxygen
                ('70', 'A8TqbFYysMg'), # Tastemade
                ('71', 'kKkc2oS4HBk'), # FOX Business
                ('72', 'eDLQBktRrLM'), # BBC World News
                ('73', 'eaGW0kq7zF4'), # truTV
                ('74', 'qGpWjXoFKtY'), # Local Now
                ('75', 'U12IJQZHKOE'), # VH1
                ('76', 'YSU0bW3YhCQ'), # Paramount
                ('77', '4BUf29xnQjw'), # TV Land
                ('78', '4ACtrIqP9y8'), # Court TV
                ('79', 'iVy-1LbogGQ'), # OWN
                ('80', 'udRowhxv4CQ'), # MTV
                ('81', 'aLZ3wtFUKAw'), # MSNBC
                ('82', 'wYdC3DXjsB4'), # Nickelodeon
                ('83', 'HxezIULigSw'), # SundanceTV
                ('84', 'h0m0uMt8igc'), # IFC
                ('85', 'W8bk7pJg-F4'), # Pop
                ('86', 'OkUaU4FZMg0'), # Nat Geo Wild
                ('87', 'B3UUHeVbrp8'), # Olympic Channel
                ('88', 'JUw21pp_D6g'), # Disney Junior
                ('89', '2QOJT_ju-g8'), # Universal Kids
                ('90', '9T6IvMh30z0'), # FXM
                ('91', '3VWjylQcueE'), # MotorTrend
                ('92', 'Z2NhQ2_vHjw'), # WE tv
                ('93', 'IlhP7v1_8xI'), # Newsy
                ('94', '4VEll9ZbZYE'), # Comedy Central
                ('95', 'YYaBZE1p-y0'), # CMT
                ('96', 'a7_4w6591mY'), # BET
                ('97', 'HvVs28bv5iI'), # BBC America
                ('98', '_dh27DIQWvA'), # Cheddar
            ]
        )
        self.channel_index = self.channels.first()

    def prev_channel(self):
        print('Playing previous channel')
        self.play_channel(self.channels.prev_channel(self.channel_index)[0])

    def next_channel(self):
        print('Playing next channel')
        self.play_channel(self.channels.next_channel(self.channel_index)[0])

    def play_channel(self, channel_index):
        print('Playing channel %s' % channel_index)
        try:
            if not self.controller.is_active:
                self.controller.update_screen_id()
            self.controller.play_video(self.channels[channel_index])
            self.channel_index = channel_index
            self.channel_timer = 0
        except:
            print('Error playing channel %s' % self.channels[channel_index])

    def number_pressed(self, button):
        print('Button pressed %s' % button)
        self.button_queue += button
        self.button_press_time = time()
        self.change_channel_timer()

    def change_channel_timer(self):
        if (self.button_queue) and ((time() - self.button_press_time > 1) or (len(self.button_queue) >= 2)):
            if self.button_queue in self.channels:
                self.play_channel(self.button_queue)

            self.button_queue = ''
            self.button_press_time = None

    # Counts how long we have been on a specific channel and pauses and plays if we are on the correct tick
    def channel_timer_count(self):
        if self.channel_timer == 5:
            self.cast.media_controller.pause()
        elif self.channel_timer == 6:
            self.cast.media_controller.play()
        # Our loop timer is .5 seconds so we increment by .5 here
        self.channel_timer += 0.5

    def toggle_power(self):
        if self.cast.media_controller.is_playing:
            self.cast.media_controller.stop()
        else:
            self.play_channel(self.channel_index)


class OrderedChannelDict(OrderedDict):
    def first(self):
        return next(iter(self))

    def next_channel(self, key):
        index = list(self.keys()).index(key) + 1
        return list(self.items())[index % len(self)]

    def prev_channel(self, key):
        index = list(self.keys()).index(key) - 1
        return list(self.items())[index % len(self)]
