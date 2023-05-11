import requests

def findKey(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values[0]

def channelAlreadyFound(tup, channel):
    for _, _, name in tup:
        if name == channel:
            return True

    return False

channelMapping = {
    'Epix East': 0,
    'Epix 2': 1,
    'Showtime 2': 2,
    'WEDU PBS': 3,
    'WEDU PBS2': 4,
    'Epix Drive-in': 5,
    'Epix Hits': 6,
    'ABC 7': 7,
    'NBC 8': 8,
    'NBCLX': 9,
    '10 News': 10,
    'ABC 28': 11,
    'ABC News Live': 12,
    'FOX 13': 13,
    'MLB Game of The Week': 14,
    'BTN': 15,
    'CBS Sports Network': 16,
    'Showtime': 17,
    'NFL Network':18,
    'Cozi': 19,
    'Comet TV': 20,
    'Start TV': 21,
    'Universo': 22,
    'Telemundo Tampa': 23,
    'Turner Classic Movies': 24,
    'Cartoon Network': 25,
    'FS2': 26,
    'FOX Sports Florida': 27,
    'TBS': 28,
    'USA': 29,
    'SYFY': 30,
    'TNT': 31,
    'ESPN': 32,
    'ESPN2': 33,
    'SEC Network': 34,
    'ACC Network': 35,
    'ESPNU': 36,
    'ESPNews': 37,
    'MLB Network': 38,
    'FXX': 39,
    'CNBC': 40,
    'HLN': 41,
    'CNN': 42,
    'FOX News': 43,
    'CW 44': 44,
    'E!': 45,
    'CNBC World': 46,
    'FX': 47,
    'Discovery Channel': 48,
    'Smithsonian Channel': 49,
    'Freeform': 50,
    'Golf Channel': 51,
    'FOX Sports Sun': 52,
    'NBCSN': 53,
    'NBA TV': 54,
    'Food Network': 55,
    'Travel Channel': 56,
    'FS1': 57,
    'Nat Geo': 58,
    'HGTV': 59,
    'Tennis Channel': 60,
    'Disney Channel': 61,
    'Disney XD': 62,
    'ID': 63,
    'TLC': 64,
    'AMC': 65,
    'Bravo': 66,
    'Animal Planet': 67,
    'TYT Network': 68,
    'Oxygen': 69,
    'Tastemade': 70,
    'FOX Business': 71,
    'BBC World News': 72,
    'truTV': 73,
    'Local Now': 74,
    'VH1': 75,
    'Paramount': 76,
    'TV Land': 77,
    'Court TV': 78,
    'OWN': 79,
    'MTV': 80,
    'MSNBC': 81,
    'Nickelodeon': 82,
    'SundanceTV': 83,
    'IFC': 84,
    'Pop': 85,
    'Nat Geo Wild': 86,
    'Olympic Channel': 87,
    'Disney Junior': 88,
    'Universal Kids': 89,
    'FXM': 90,
    'MotorTrend': 91,
    'WE tv': 92,
    'Newsy': 93,
    'Comedy Central': 94,
    'CMT': 95,
    'BET': 96,
    'BBC America': 97,
    'Cheddar': 98,
    'Cheddar Business': 99,
    'Showtime2': 100,
    'SHOxBET': 101,
    'Showtime Extreme': 102,
    'Showtime Showcase': 103,
    'Showtime Next': 104,
    'Showtime Women': 105,
    'Showtime Family Zone': 106,
}

# The following cookies are required to access the YouTube TV API. They can be extracted from a browser session which is logged into YouTube TV.
# HSID, SSID, APISID, SAPISID, SID, LOGIN_INFO, SIDCC
cookies = {}

# The following headers are required to access the YouTube TV API. They can be extracted from a browser session which is logged into YouTube TV.
# x-origin, Authorization, Content-Type, Referer
headers = {}

channels = []

params = (
    ('alt', 'json'),
    ('key', '<API KEY>'),
)

data = '{"context":{"client":{"clientName":"WEB_UNPLUGGED","clientVersion":"0.1","screenDensityFloat":"2","browserName":"Chrome","browserVersion":"84.0.4147.135","osName":"Macintosh","osVersion":"10_15_6","experimentIds":[],"utcOffsetMinutes":-240,"timeZone":"America/New_York","userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","unpluggedLocationInfo":{"clientPermissionState":2,"timezone":"America/New_York"}},"request":{"internalExperimentFlags":[{"key":"force_route_unplugged_spoiler_mode_to_outertube","value":"true"},{"key":"force_route_unplugged_browse_library_to_outertube","value":"true"},{"key":"force_route_unplugged_browse_main_to_outertube","value":"true"},{"key":"flush_onbeforeunload","value":"true"},{"key":"pass_biscotti_id_in_header_ajax","value":"true"},{"key":"delay_gel_until_config_ready","value":"true"},{"key":"route_network_details_page_to_outertube","value":"true"},{"key":"unplugged_web_post_live_dvr_won","value":"true"},{"key":"enable_device_forwarding_from_xhr_client","value":"true"},{"key":"retry_web_logging_batches","value":"true"},{"key":"optimistically_create_transport_client","value":"true"},{"key":"disable_thumbnail_preloading","value":"true"},{"key":"log_js_error_clusters","value":"1"},{"key":"polymer_verifiy_app_state","value":"true"},{"key":"html5_enable_forecasting_in_pacf","value":"true"},{"key":"unplugged_uvas_in_uas","value":"true"},{"key":"enable_ve_tracker_key","value":"true"},{"key":"enable_mixed_direction_formatted_strings","value":"true"},{"key":"log_foreground_heartbeat_unplugged","value":"true"},{"key":"ignore_empty_xhr","value":"true"},{"key":"networkless_retry_attempts","value":"1"},{"key":"web_op_signal_type_banlist","value":""},{"key":"route_event_details_page_to_outertube","value":"true"},{"key":"force_route_unplugged_browse_library_to_outertube","value":"true"},{"key":"interaction_logging_on_gel_web","value":"true"},{"key":"use_typescript_transport","value":"true"},{"key":"route_sports_event_details_page_to_outertube","value":"true"},{"key":"unplugged_web_discovery_v2_home","value":"true"},{"key":"remove_web_visibility_batching","value":"true"},{"key":"suppress_gen_204","value":"true"},{"key":"web_api_url","value":"true"},{"key":"interaction_screen_on_gel_web","value":"true"},{"key":"web_screen_associated_all_layers","value":"true"},{"key":"networkless_throttle_timeout","value":"100"},{"key":"disable_simple_mixed_direction_formatted_strings","value":"true"},{"key":"polymer_bad_build_labels","value":"true"},{"key":"unplugged_unlock_paywall_variant","value":"direct_to_explore"},{"key":"networkless_ytidb_version","value":"1"},{"key":"web_logging_max_batch","value":"100"},{"key":"log_js_exceptions_fraction","value":"1"},{"key":"network_polling_interval","value":"30000"},{"key":"html5_experiment_id_label","value":"0"},{"key":"enable_gel_web_client_event_id","value":"true"},{"key":"web_gel_debounce_ms","value":"10000"},{"key":"web_screen_manager_use_default_client","value":"true"},{"key":"force_route_unplugged_browse_main_to_outertube","value":"true"},{"key":"web_log_connection","value":"true"},{"key":"web_post_search","value":"true"},{"key":"custom_csi_timeline_use_gel","value":"true"},{"key":"networkless_request_age_limit","value":"30"},{"key":"web_op_continuation_type_banlist","value":""},{"key":"web_op_endpoint_banlist","value":""},{"key":"overwrite_polyfill_on_logging_lib_loaded","value":"true"},{"key":"web_client_counter_random_seed","value":"true"},{"key":"web_client_version_override","value":""},{"key":"unplugged_unlock_paywall_living_room","value":"true"},{"key":"enable_x_trials_per_fop","value":"true"},{"key":"log_window_onerror_fraction","value":"0.1"},{"key":"interaction_click_on_gel_web","value":"true"},{"key":"botguard_async_snapshot_timeout_ms","value":"3000"},{"key":"unplugged_onboarding_v2","value":"true"},{"key":"web_gel_timeout_cap","value":"true"},{"key":"route_movie_details_page_to_outertube","value":"true"}]}},"browseId":"FEunplugged_epg","unpluggedBrowseOptions":{"epgOptions":{"maxAiringsPerStation":16,"initialEpgFetchStartTimeMs":"1598274000000","initialEpgFetchDurationMs":14058000,"paginationDurationMs":7734000,"maxDurationMs":"604800000"}}}'

response = requests.post('https://tv.youtube.com/youtubei/v1/unplugged/browse', headers=headers, params=params, cookies=cookies, data=data)

responseJson = response.json()

channelHash = responseJson["contents"]["epgRenderer"]["paginationRenderer"]["epgPaginationRenderer"]["contents"]

for channel in channelHash:
    channel_label = channel["epgRowRenderer"]["station"]["epgStationRenderer"]["icon"]["accessibility"]["accessibilityData"]["label"]
    if (channelAlreadyFound(channels, channel_label)):
        channel_label = channel_label + "2"
    channel_id = findKey(channel["epgRowRenderer"]["airings"][0]["epgAiringRenderer"]["navigationEndpoint"], "videoId")
    channels.append((channelMapping[channel_label], channel_id, channel_label))
    # if (channel_label == 'truTV'):
        #
    # print("('%s', '%s') # %s" % (channelMapping[channel_label], channel_id, channel_label))

for channel in sorted(channels, key=lambda tup: tup[0]):
    print("('%s', '%s'), # %s" % (channel[0], channel[1], channel[2]))
