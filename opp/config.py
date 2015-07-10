__author__ = 'PAY.ON'
# following module represents the configuration of the OPP library
# all configuration values apply both for opp.core and opp.facade modules

#constants
TEST_INTERNAL = 0
TEST_EXTERNAL = 1
LIVE = 3

#configuration values for OPP
TEST_URL = "https://test.oppwa.com/v1"  # url used for TEST_INTERNAL and TEST_EXTERNAL mode
LIVE_URL = 'https://oppwa.com/v1'  # url used for LIVE mode
MODE = TEST_INTERNAL  # default value for mode
REQUEST_TIMEOUT = 60  # default value for all request timeouts
VALIDATE_SSL = True  # default value for SSL validation for all requests
HTTP_DEBUG_MODE = False  # default value for http debug mode, it will set http_client.HTTPConnection.debuglevel


class Config(object):
    def __init__(self, test_url=TEST_URL, live_url=LIVE_URL, mode=TEST_INTERNAL, request_timeout=REQUEST_TIMEOUT,
                 ssl_verify=VALIDATE_SSL, http_debug_mode=HTTP_DEBUG_MODE):
        self.test_url = test_url
        self.live_url = live_url
        self.mode = mode
        self.request_timeout = request_timeout
        self.ssl_verify = ssl_verify
        self.http_debug_mode = http_debug_mode
        self.current_url = self.live_url if mode == LIVE else self.test_url


config = Config()


def configure(test_url=TEST_URL, live_url=LIVE_URL, mode=TEST_INTERNAL, request_timeout=REQUEST_TIMEOUT):
    global config
    config = Config(test_url=test_url, live_url=live_url, mode=mode, request_timeout=request_timeout)

