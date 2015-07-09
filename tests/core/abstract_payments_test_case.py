__author__ = 'PAY.ON'
import tests


class AbstractPaymentsTestCase(tests.abstract_test_case.AbstractTestCase):
    def assert_payment_equal(self, request, response):
        # added for debugging
        print("-----------RESPONSE-----------")
        print(response)
        self.assertEqual(request['paymentBrand'], response['paymentBrand'])
        self.assertEqual(request['paymentType'], response['paymentType'])