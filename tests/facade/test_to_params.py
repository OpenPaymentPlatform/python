__author__ = 'PAY.ON'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import tests.test_data_utils
import opp.facade


class TestToParams(unittest.TestCase):
    def test_authentication_to_params(self):
        expected_parameters = tests.test_data_utils.authentication
        result_parameters = opp.facade.Authentication(user_id="8a8294174b7ecb28014b9699220015cc", password="sy6KJsT8",
                                                      entity_id="8a8294174b7ecb28014b9699220015ca").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_basic_payment_to_params(self):
        expected_parameters = {"amount": "92.00",
                               "currency": "EUR",
                               "paymentBrand": "AMEX",
                               "descriptor": "Test AMEX",
                               "merchantTransactionId": "1a2b3c4d5e6f7g8h9i",
                               "merchantInvoiceId": "a1b2c3d4e5f6g7h8i9"
                               }
        result_parameters = opp.facade.BasicPayment(amount="92.00", currency="EUR", payment_brand="AMEX",
                                                    descriptor="Test AMEX",
                                                    merchant_transaction_id="1a2b3c4d5e6f7g8h9i",
                                                    merchant_invoice_id="a1b2c3d4e5f6g7h8i9").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_card_account_to_params(self):
        expected_parameters = {"card.holder": "Jane Jones",
                               "card.number": "377777777777770",
                               "card.expiryMonth": "05",
                               "card.expiryYear": "2018",
                               "card.cvv": "1234"
                               }
        result_parameters = opp.facade.CardAccount(holder="Jane Jones", number="377777777777770", expiry_month="05",
                                                   expiry_year="2018",
                                                   cvv="1234").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_virtual_account_to_params(self):
        expected_parameters = {"virtualAccount.accountId": "1a2b3c4d5e6f7g8h9i",
                               "virtualAccount.password": "sy6KJsT8"
                               }
        result_parameters = opp.facade.VirtualAccount(account_id="1a2b3c4d5e6f7g8h9i", password="sy6KJsT8").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_bank_account_to_params(self):
        expected_parameters = {"bankAccount.holder": "Jane Jones",
                               "bankAccount.bankName": "Deutsche Bank",
                               "bankAccount.number": "1009534785",
                               "bankAccount.iban": "DE23100000001234567890",
                               "bankAccount.bankCode": "DEUTDEMM",
                               "bankAccount.bic": "DEUTDEFF",
                               "bankAccount.country": "DE",
                               "bankAccount.mandate.id": "1a2b3c4d5e6f7g8h9i",
                               "bankAccount.mandate.dateOfSignature": "2015-07-09",
                               "transactionDueDate": "2015-07-09"
                               }
        result_parameters = opp.facade.BankAccount(holder="Jane Jones", bank_name="Deutsche Bank", number="1009534785",
                                                   iban="DE23100000001234567890", bank_code="DEUTDEMM", bic="DEUTDEFF",
                                                   country="DE",
                                                   mandate=opp.facade.Mandate(id='1a2b3c4d5e6f7g8h9i', date_of_signature='2015-07-09'),
                                                   transaction_due_date="2015-07-09").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_customer_to_params(self):
        expected_parameters = {"customer.merchantCustomerId": "1a2b3c4d5e6f7g8h9i",
                               "customer.givenName": "Jane",
                               "customer.surname": "Jones",
                               "customer.sex": "F",
                               "customer.birthDate": "1983-10-05",
                               "customer.phone": "+49 123456789",
                               "customer.mobile": "+49 987654321",
                               "customer.email": "jane.jones@test.de",
                               "customer.companyName": "Test Company",
                               "customer.identificationDocType": "TAXSTATEMENT",
                               "customer.identificationDocId": "a1b2c3d4e5f6g7h8i9",
                               "customer.ip": "XX.XXX.XX.XXX"}
        result_parameters = opp.facade.Customer(merchant_customer_id="1a2b3c4d5e6f7g8h9i", given_name="Jane",
                                                surname="Jones", sex="F",
                                                birth_date="1983-10-05", phone="+49 123456789", mobile="+49 987654321",
                                                email="jane.jones@test.de", company_name="Test Company",
                                                identification_doc_type="TAXSTATEMENT",
                                                identification_doc_id="a1b2c3d4e5f6g7h8i9",
                                                customer_ip="XX.XXX.XX.XXX").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_billing_address_to_params(self):
        expected_parameters = {"billing.street1": "Street 1",
                               "billing.street2": "Street 2",
                               "billing.city": "Test city",
                               "billing.state": "Test state",
                               "billing.postcode": "12345",
                               "billing.country": "DE"}
        result_parameters = opp.facade.BillingAddress(street1="Street 1", street2="Street 2",
                                                      city="Test city", state="Test state",
                                                      postcode="12345", country="DE").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_shipping_address_to_params(self):
        expected_parameters = {"shipping.givenName": "Jane",
                               "shipping.surname": "Jones",
                               "shipping.street1": "Street 1",
                               "shipping.street2": "Street 2",
                               "shipping.city": "Test city",
                               "shipping.state": "Test state",
                               "shipping.postcode": "12345",
                               "shipping.country": "DE"}
        result_parameters = opp.facade.ShippingAddress(given_name="Jane", surname="Jones", street1="Street 1",
                                                       street2="Street 2",
                                                       city="Test city", state="Test state",
                                                       postcode="12345", country="DE").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_cart_to_params(self):
        expected_parameters = {"cart.items[0].name": "T-shirt",
                               "cart.items[0].merchantItemId": "1a2b3c4d5e6f7g8h9i",
                               "cart.items[0].quantity": "1",
                               "cart.items[0].type": "XL",
                               "cart.items[0].price": "5",
                               "cart.items[0].currency": "EUR",
                               "cart.items[0].description": "Summer",
                               "cart.items[0].tax": "0.25",
                               "cart.items[0].shipping": "1",
                               "cart.items[0].discount": "5"}
        item_object = opp.facade.Item(name="T-shirt", merchant_item_id="1a2b3c4d5e6f7g8h9i", quantity="1",
                                      type="XL",
                                      price="5", currency="EUR",
                                      description="Summer", tax="0.25", shipping="1",
                                      discount="5")
        list_of_items = [item_object]
        result_parameters = opp.facade.Cart(list_of_items).to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_tokenization_and_registration_to_params(self):
        expected_parameters = {"createRegistration": "true"}
        result_parameters = opp.facade.TokenizationAndRegistration(create_registration="true").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_recurring_to_params(self):
        expected_parameters = {"recurringType": "INITIAL"}
        result_parameters = opp.facade.Recurring(type="INITIAL").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_threed_secure_to_params(self):
        expected_parameters = {"threeDSecure.eci": "07",
                               "threeDSecure.verificationId": "dGVzdF92ZXJpZmljYXRpb25faWQ=",
                               "threeDSecure.xid": "dGVzdF94aWQ="
                               }
        result_parameters = opp.facade.ThreeDSecure(eci="07", verification_id="dGVzdF92ZXJpZmljYXRpb25faWQ=", xid="dGVzdF94aWQ=").to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_custom_parameters_to_params(self):
        expected_parameters = {"customParameters[SHOPPER_number_of_installments]": "3",
                               "customParameters[SHOPPER_trial_period_days]": "10"
                               }
        result_parameters = opp.facade.CustomParameters(number_of_installments='3', trial_period_days='10').to_params()
        self.assertEqual(expected_parameters, result_parameters)

    def test_asynchronous_payments_to_params(self):
        expected_parameters = {"shopperResultUrl": "http://shopperurl.com",
                               "notificationUrl": "http://notificationurl.com"
                               }
        result_parameters = opp.facade.AsynchronousPayments(shopper_result_url="http://shopperurl.com", notification_url="http://notificationurl.com").to_params()
        self.assertEqual(expected_parameters, result_parameters)