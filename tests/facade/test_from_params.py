__author__ = 'PAY.ON'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import tests.test_data_utils
import opp.facade


class TestFromParams(unittest.TestCase):
    def test_card_account_from_params(self):
        card_account_with_result_parameters = opp.facade.CardAccount.from_params(
            {"card.number": "377777777777770", "card.holder": "Jane Jones",
             "card.expiryMonth": "05", "card.expiryYear": "2018",
             "card.cvv": "1234"
             }
        )
        self.assertEqual(card_account_with_result_parameters.holder, "Jane Jones")
        self.assertEqual(card_account_with_result_parameters.number, "377777777777770")
        self.assertEqual(card_account_with_result_parameters.expiry_month, "05")
        self.assertEqual(card_account_with_result_parameters.expiry_year, "2018")
        self.assertEqual(card_account_with_result_parameters.cvv, "1234")

    def test_virtual_account_from_params(self):
        virtual_account_with_result_parameters = opp.facade.VirtualAccount.from_params(
            {"virtualAccount.accountId": "1a2b3c4d5e6f7g8h9i", "virtualAccount.password": "sy6KJsT8"}
        )
        self.assertEqual(virtual_account_with_result_parameters.account_id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(virtual_account_with_result_parameters.password, "sy6KJsT8")

    def test_bank_account_from_params(self):
        bank_account_with_result_parameters = opp.facade.BankAccount.from_params(
            {"bankAccount.holder": "Jane Jones",
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
        )
        self.assertEqual(bank_account_with_result_parameters.holder, "Jane Jones")
        self.assertEqual(bank_account_with_result_parameters.bank_name, "Deutsche Bank")
        self.assertEqual(bank_account_with_result_parameters.number, "1009534785")
        self.assertEqual(bank_account_with_result_parameters.iban, "DE23100000001234567890")
        self.assertEqual(bank_account_with_result_parameters.bank_code, "DEUTDEMM")
        self.assertEqual(bank_account_with_result_parameters.bic, "DEUTDEFF")
        self.assertEqual(bank_account_with_result_parameters.country, "DE")
        self.assertEqual(bank_account_with_result_parameters.mandate_id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(bank_account_with_result_parameters.mandate_date_of_signature, "2015-07-09")
        self.assertEqual(bank_account_with_result_parameters.transaction_due_date, "2015-07-09")

    def test_customer_from_params(self):
        customer_with_result_parameters = opp.facade.Customer.from_params(
            {"customer.merchantCustomerId": "1a2b3c4d5e6f7g8h9i",
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
             "customer.ip": "XX.XXX.XX.XXX"
             }
        )
        self.assertEqual(customer_with_result_parameters.merchant_customer_id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(customer_with_result_parameters.given_name, "Jane")
        self.assertEqual(customer_with_result_parameters.surname, "Jones")
        self.assertEqual(customer_with_result_parameters.sex, "F")
        self.assertEqual(customer_with_result_parameters.birth_date, "1983-10-05")
        self.assertEqual(customer_with_result_parameters.phone, "+49 123456789")
        self.assertEqual(customer_with_result_parameters.mobile, "+49 987654321")
        self.assertEqual(customer_with_result_parameters.email, "jane.jones@test.de")
        self.assertEqual(customer_with_result_parameters.company_name, "Test Company")
        self.assertEqual(customer_with_result_parameters.identification_doc_type, "TAXSTATEMENT")
        self.assertEqual(customer_with_result_parameters.identification_doc_id, "a1b2c3d4e5f6g7h8i9")
        self.assertEqual(customer_with_result_parameters.customer_ip, "XX.XXX.XX.XXX")

    def test_billing_address_from_params(self):
        billing_address_with_result_parameters = opp.facade.BillingAddress.from_params(
            {"billing.street1": "Street 1",
             "billing.street2": "Street 2",
             "billing.city": "Test city",
             "billing.state": "Test state",
             "billing.postcode": "12345",
             "billing.country": "DE"
             }
        )
        self.assertEqual(billing_address_with_result_parameters.street1, "Street 1")
        self.assertEqual(billing_address_with_result_parameters.street2, "Street 2")
        self.assertEqual(billing_address_with_result_parameters.city, "Test city")
        self.assertEqual(billing_address_with_result_parameters.state, "Test state")
        self.assertEqual(billing_address_with_result_parameters.postcode, "12345")
        self.assertEqual(billing_address_with_result_parameters.country, "DE")

    def test_shipping_address_from_params(self):
        shipping_address_with_result_parameters = opp.facade.ShippingAddress.from_params(
            {"shipping.givenName": "Jane",
             "shipping.surname": "Jones",
             "shipping.street1": "Street 1",
             "shipping.street2": "Street 2",
             "shipping.city": "Test city",
             "shipping.state": "Test state",
             "shipping.postcode": "12345",
             "shipping.country": "DE"
             }
        )
        self.assertEqual(shipping_address_with_result_parameters.given_name, "Jane")
        self.assertEqual(shipping_address_with_result_parameters.surname, "Jones")
        self.assertEqual(shipping_address_with_result_parameters.street1, "Street 1")
        self.assertEqual(shipping_address_with_result_parameters.street2, "Street 2")
        self.assertEqual(shipping_address_with_result_parameters.city, "Test city")
        self.assertEqual(shipping_address_with_result_parameters.state, "Test state")
        self.assertEqual(shipping_address_with_result_parameters.postcode, "12345")
        self.assertEqual(shipping_address_with_result_parameters.country, "DE")

    def test_cart_from_params(self):
        item = opp.facade.Item(name="T-shirt", merchant_item_id="1a2b3c4d5e6f7g8h9i", quantity="1",
                               item_type="XL",
                               price="5", currency="EUR",
                               description="Summer", tax="0.25", shipping="1",
                               discount="5").to_params()
        list_of_items = [item]
        cart = opp.facade.Cart.from_params(list_of_items)

        self.assertEqual(cart.items[0].name, "T-shirt")
        self.assertEqual(cart.items[0].merchant_item_id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(cart.items[0].quantity, "1")
        self.assertEqual(cart.items[0].item_type, "XL")
        self.assertEqual(cart.items[0].price, "5")
        self.assertEqual(cart.items[0].currency, "EUR")
        self.assertEqual(cart.items[0].description, "Summer")
        self.assertEqual(cart.items[0].tax, "0.25")
        self.assertEqual(cart.items[0].shipping, "1")
        self.assertEqual(cart.items[0].discount, "5")

    def test_result_from_params(self):
        result_with_result_parameters = opp.facade.Result.from_params(
            {"result.code": "000.100.110",
             "result.description": "Request successfully processed"
             }
        )
        self.assertEqual(result_with_result_parameters.code, "000.100.110")
        self.assertEqual(result_with_result_parameters.description, "Request successfully processed")

    def test_merchant_from_params(self):
        bank_account_parameters = opp.facade.BankAccount(holder="Jane Jones", number="1009534785", bic="DEUTDEFF",
                                                         country="DE").to_params()
        merchant = opp.facade.Merchant.from_params(bank_account_parameters)
        self.assertEqual(merchant.bank_account.holder, "Jane Jones")
        self.assertEqual(merchant.bank_account.number, "1009534785")
        self.assertEqual(merchant.bank_account.bic, "DEUTDEFF")
        self.assertEqual(merchant.bank_account.country, "DE")

    def test_parameter_from_params(self):
        parameter_with_result_parameters = opp.facade.Parameter.from_params(
            {"name": "test_parameter",
             "value": "test"
             }
        )
        self.assertEqual(parameter_with_result_parameters.name, "test_parameter")
        self.assertEqual(parameter_with_result_parameters.value, "test")

