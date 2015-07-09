__author__ = 'PAY.ON'
import tests.core
import tests


class TestCheckouts(tests.core.abstract_payments_test_case.AbstractPaymentsTestCase):

    def test_create_get_checkout(self):
        checkout1 = self.API.checkouts().create(**{"amount": "92.00",
                                                  "currency": "EUR",
                                                  "paymentType": "PA"})

        checkout2 = self.API.checkouts(checkout_id=checkout1['id']).get()

        self.assertEqual(checkout1['buildNumber'], checkout2['buildNumber'])

