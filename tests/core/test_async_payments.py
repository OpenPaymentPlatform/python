__author__ = 'PAY.ON'
import tests.core
import tests


class TestAsyncPayments(tests.core.abstract_payments_test_case.AbstractPaymentsTestCase):

    #payment brand dependent operations

    def create_preauthorization_with_payment_brand(self, request=None):
        request.update({"paymentType": "PA"})
        response = self.API.payments().create(**request)
        return request, response

    def create_debit_with_payment_brand(self, request=None):
        request.update({"paymentType": "DB"})
        response = self.API.payments().create(**request)
        return request, response

    def test_create_preauthorization_with_async_payment_brand_BOLETO(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.BOLETO)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_CHINAUNIONPAY(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.CHINAUNIONPAY)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_DAOPAY(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.DAOPAY)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_KLARNA_INVOICE(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.KLARNA_INVOICE)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_MONEYBOOKERS(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.MONEYBOOKERS)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PAYOLUTION_ELV(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PAYOLUTION_ELV)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PAYOLUTION_INS(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PAYOLUTION_INS)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PAYOLUTION_INVOICE(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PAYOLUTION_INVOICE)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PAYPAL(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PAYPAL)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PAYSAFECARD(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PAYSAFECARD)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PF_KARTE_DIRECT(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PF_KARTE_DIRECT)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PREPAYMENT(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PREPAYMENT)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PRZELEWY(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PRZELEWY)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_TRUSTLY(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.TRUSTLY)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_TRUSTPAY_VA(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.TRUSTPAY_VA)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_UKASH(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.UKASH)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_YANDEX(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.YANDEX)
        self.assert_payment_equal(request, response)

    # def test_create_debit_with_async_payment_brand_BOLETO(self):
    #     request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.BOLETO)
    #     self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_CHINAUNIONPAY(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.CHINAUNIONPAY)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_DAOPAY(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.DAOPAY)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_EPS(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.EPS)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_GIROPAY(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.GIROPAY)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_IDEAL(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.IDEAL)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_KLARNA_INVOICE(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.KLARNA_INVOICE)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_MONEYBOOKERS(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.MONEYBOOKERS)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PAYOLUTION_ELV(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PAYOLUTION_ELV)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_PAYOLUTION_INS(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.PAYOLUTION_INS)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_PAYOLUTION_INVOICE(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.PAYOLUTION_INVOICE)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_PAYPAL(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.PAYPAL)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_PAYSAFECARD(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.PAYSAFECARD)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_PAYTRAIL(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.PAYTRAIL)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_PF_KARTE_DIRECT(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.PF_KARTE_DIRECT)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_POLI(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.POLI)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_PREPAYMENT(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.PREPAYMENT)
        self.assert_payment_equal(request, response)

    def test_create_preauthorization_with_async_payment_brand_PRZELEWY(self):
        request, response = self.create_preauthorization_with_payment_brand(request=tests.test_data_utils.PRZELEWY)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_SOFORTUEBERWEISUNG(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.SOFORTUEBERWEISUNG)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_TRUSTLY(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.TRUSTLY)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_TRUSTPAY_VA(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.TRUSTPAY_VA)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_UKASH(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.UKASH)
        self.assert_payment_equal(request, response)

    def test_create_debit_with_async_payment_brand_YANDEX(self):
        request, response = self.create_debit_with_payment_brand(request=tests.test_data_utils.YANDEX)
        self.assert_payment_equal(request, response)
