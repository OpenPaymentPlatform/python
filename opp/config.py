__author__ = 'PAY.ON'
import sys
#Following module represents the configuration of the OPP library
#All configuration values apply both for opp.core and opp.facade modules

#constants
TEST_INTERNAL = 0
TEST_EXTERNAL = 1
LIVE = 3

#configuration values for OPP
TEST_URL = "https://test.oppwa.com/v1"
LIVE_URL = 'https://oppwa.com/v1'
MODE = TEST_INTERNAL
REQUEST_TIMEOUT = 60
VALIDATE_SSL = True
LOGGING_DESTINATION = sys.__stdout__


class Config(object):
    def __init__(self, test_url=TEST_URL, live_url=LIVE_URL, mode=TEST_INTERNAL, request_timeout=REQUEST_TIMEOUT,
                 ssl_verify=VALIDATE_SSL, logging_destination=LOGGING_DESTINATION):
        self.test_url = test_url
        self.live_url = live_url
        self.mode = mode
        self.request_timeout = request_timeout
        self.ssl_verify = ssl_verify
        self.logging_destination = logging_destination
        self.current_url = self.live_url if mode == LIVE else self.test_url


config = Config()


def configure(test_url=TEST_URL, live_url=LIVE_URL, mode=TEST_INTERNAL, request_timeout=REQUEST_TIMEOUT):
    global config
    config = Config(test_url=test_url, live_url=live_url, mode=mode, request_timeout=request_timeout)

