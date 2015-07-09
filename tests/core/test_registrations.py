__author__ = 'PAY.ON'

import tests.core
import tests


class TestRegistration(tests.core.abstract_payments_test_case.AbstractPaymentsTestCase):

    def test_create_get_delete_registration(self):
        registration1 = self.API.registrations().create(**{"paymentBrand": "AMEX",
                                                           "descriptor": "Test PA",
                                                           "card.number": "377777777777770",
                                                           "card.holder": "Jane Jones",
                                                           "card.expiryMonth": "05",
                                                           "card.expiryYear": "2018",
                                                           "card.cvv": "1234"})
        registration2 = self.API.registrations(registration_id=registration1['id']).get()

        self.assertEqual(registration1['buildNumber'], registration2['buildNumber'])

        # check this action and the response
        # self.API.registrations(registration_id=registration1['id']).delete()
        # registration3 = self.API.registrations(registration_id=registration1['id']).get()
        # self.assertEqual(registration3['result']['code'], "200.300.404")
