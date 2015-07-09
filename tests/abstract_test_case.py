__author__ = 'PAY.ON'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import tests.test_data_utils
import opp.core


class AbstractTestCase(unittest.TestCase):
    def setUp(self):
        self.API = opp.core.API(**tests.test_data_utils.authentication)

    def tearDown(self):
        del self.API