# coding=utf-8
__author__ = 'PAY.ON'
from requests import Session
import opp.config
from six.moves import http_client

http_client.HTTPConnection.debuglevel = opp.config.HTTP_DEBUG_MODE


class Utils(object):
    @staticmethod
    def path_str(s):
        if s is None:
            return ''
        return str('/' + s)


class Payments(object):
    _path = '/payments'

    def __init__(self, http_client=None, payment_id=None):
        self.http_client = http_client
        self.payment_id = payment_id

    @property
    def path(self):
        return '%(id)s' % {'id': Utils.path_str(self.payment_id)}

    def create(self, **kwargs):
        return self.http_client('POST', kwargs, (Payments._path + self.path), None)

    def get(self, **kwargs):
        return self.http_client('GET', kwargs, (Payments._path + self.path), None)


class Checkouts(object):
    _path = '/checkouts'

    def __init__(self, http_client=None, checkout_id=None):
        self.http_client = http_client
        self.checkout_id = checkout_id

    @property
    def path(self):
        return '%(id)s' % {'id': Utils.path_str(self.checkout_id)}

    def create(self, **kwargs):
        return self.http_client('POST', kwargs, (Checkouts._path + self.path), None)

    def get(self, **kwargs):
        return self.http_client('GET', kwargs, (Checkouts._path + self.path + '/payment'), None)


class Registrations(object):
    _path = '/registrations'

    def __init__(self, http_client=None, registration_id=None):
        self.http_client = http_client
        self.registration_id = registration_id

    @property
    def path(self):
        return '%(id)s' % {'id': Utils.path_str(self.registration_id)}

    def create(self, **kwargs):
        return self.http_client('POST', kwargs, (Registrations._path + self.path), None)

    def get(self, **kwargs):
        return self.http_client('GET', kwargs, (Registrations._path + self.path), None)

    def delete(self, **kwargs):
        return self.http_client('DELETE', kwargs, (Registrations._path + self.path), None)


class API(object):
    def __init__(self, **auth_params):
        """


        :rtype : object
        :type auth_params: object
        """
        url = opp.config.config.current_url
        self.http_client = HTTPClient(url, auth_params)

    def payments(self, payment_id=None):
        return Payments(http_client=self.http_client, payment_id=payment_id)

    def checkouts(self, checkout_id=None):
        return Checkouts(http_client=self.http_client, checkout_id=checkout_id)

    def registrations(self, registration_id=None):
        return Registrations(http_client=self.http_client, registration_id=registration_id)


class HTTPClient(object):
    def __init__(self, base_url, auth_params):
        """Initialize a new opp connection. Requires user name and password."""
        self.base_url = base_url
        self.session = Session()
        self.session.verify = opp.config.config.ssl_verify
        # self.session.auth = (user_name, "")
        self.auth_params = auth_params
        self.operations = dict(GET=self.get, POST=self.post, PUT=self.put, DELETE=self.delete)
        # for internal usage
        self.response = None

    def __call__(self, request_type, params, url, return_type):
        """

        :param request_type:
        :param params:
        :param url:
        :param return_type:
        :return: :raise ValueError:
        """
        if request_type == 'POST':
            params.update({"customParameters[SHOPPER_pluginId]": "Python"})
            if opp.config.config.mode == opp.config.TEST_INTERNAL:
                params.update({"testMode": "INTERNAL"})
            if opp.config.config.mode == opp.config.TEST_EXTERNAL:
                params.update({"testMode": "EXTERNAL"})
        if self.auth_params:
            params.update(self.auth_params)
        try:
            return self.operations[request_type](params, url, return_type)
        except ValueError as v:
            # JSON encoding failed
            if self.response is not None:
                raise ValueError(self.response.content, self.response.status_code)
            else:
                raise ValueError()

    def put(self, params, url, return_type):
        """

        :param params:
        :param url:
        :param return_type:
        :return:
        """
        return self._check_response(self.session.put(self.base_url + url, params,
                                                     timeout=opp.config.config.request_timeout,
                                                     hooks=dict(response=self._request_callback), ).json(), return_type)

    def post(self, params, url, return_type):
        """

        :param params:
        :param url:
        :param return_type:
        :return:
        """
        json = self.session.post(self.base_url + url, params, timeout=opp.config.config.request_timeout,
                                 hooks=dict(response=self._request_callback)).json()
        return self._check_response(json, return_type)

    def delete(self, params, url, return_type):
        """

        :param params:
        :param url:
        :param return_type:
        :return:
        """
        return self._check_response(self.session.delete(self.base_url + url, params=params,
                                                        timeout=opp.config.config.request_timeout,
                                                        hooks=dict(response=self._request_callback)).json(),
                                    return_type)

    def get(self, params, url, return_type):
        """

        :param params:
        :param url:
        :param return_type:
        :return:
        """
        return self._check_response(self.session.get(self.base_url + url, params=params,
                                                     timeout=opp.config.config.request_timeout,
                                                     hooks=dict(response=self._request_callback)).json(), return_type)

    def _request_callback(self, r, *args, **kwargs):
        """

        :param r:
        :param args:
        :param kwargs:
        """
        self.response = r

    def _check_response(self, json_data, return_type):
        """

        :param json_data:
        :param return_type:
        :return: :raise ValueError:
        """
        if json_data:
            # success
            if isinstance(json_data, dict):
                return dict(json_data)
            elif isinstance(json_data, list):
                return list(json_data)
            else:
                return str(json_data)
        else:
            # error
            raise ValueError(json_data, self.response.status_code)
