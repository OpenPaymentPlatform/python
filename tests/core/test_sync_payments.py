__author__ = 'PAY.ON'
import tests.core
import tests


class TestSyncPayments(tests.core.abstract_payments_test_case.AbstractPaymentsTestCase):

    #payment brand independent operations
    def test_create_capture_payment(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.AMEX)
        capture = self.API.payments(payment_id=response['id']).create(**{"amount": "90.00",
                                                                         "currency": "EUR",
                                                                         "paymentType": "CP"})
        self.assertEqual(capture['result']['code'], "000.100.110")

    def test_create_refund_payment(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.AMEX)
        refund = self.API.payments(payment_id=response['id']).create(**{"amount": "52.00",
                                                                        "currency": "EUR",
                                                                        "paymentType": "RF"})
        self.assertEqual(refund['result']['code'], "000.100.110")

    def test_create_credit_payment(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.AMEX)
        request.update({"paymentType": "CD"})
        credit = self.API.payments().create(**request)

        self.assertEqual(credit['result']['code'], "000.100.110")

    def test_create_reverse_payment(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.AMEX)
        reverse = self.API.payments(payment_id=response['id']).create(**{"paymentType": "RV"})
        self.assertEqual(reverse['result']['code'], "000.100.110")


    #payment brand dependent operations
    def create_preauthorization_with_payment_brand(self, request=None):
        request.update({"paymentType": "PA"})
        response = self.API.payments().create(**request)
        return request, response

    def create_debit_with_payment_brand(self, request=None):
        request.update({"paymentType": "DB"})
        response = self.API.payments().create(**request)
        return request, response

    def test_create_preauthorization_with_sync_payment_brand_AMEX(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.AMEX)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_ASYACARD(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.ASYACARD)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_AXESS(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.AXESS)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_BONUS(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.BONUS)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_CARTEBLEUE(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.CARTEBLEUE)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_DANKORT(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.DANKORT)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_DINERS(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.DINERS)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_DIRECTDEBIT_SEPA(self):
        request, response = self.create_preauthorization_with_payment_brand(tests.test_data_utils.DIRECTDEBIT_SEPA)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_DISCOVER(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.DISCOVER)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_HIPERCARD(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.HIPERCARD)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_JCB(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.JCB)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_MAESTRO(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.MAESTRO)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_MASTER(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.MASTER)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_VISA(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.VISA)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_VISAELECTRON(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.VISAELECTRON)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_VPAY(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.DISCOVER)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_sync_payment_brand_WORLD(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.WORLD)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_AMEX(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.AMEX)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_ASYACARD(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.ASYACARD)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_AXESS(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.AXESS)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_BONUS(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.BONUS)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_CARTEBLEUE(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.CARTEBLEUE)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_DANKORT(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.DANKORT)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_DINERS(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.DINERS)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_DIRECTDEBIT_SEPA(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.DIRECTDEBIT_SEPA)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_DISCOVER(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.DISCOVER)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_HIPERCARD(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.HIPERCARD)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_JCB(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.JCB)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_MAESTRO(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.MAESTRO)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_MASTER(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.MASTER)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_VISA(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.VISA)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_VISAELECTRON(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.VISAELECTRON)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_VPAY(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.VPAY)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_sync_payment_brand_WORLD(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.WORLD)
        self.assert_payment_equal(request, response)
