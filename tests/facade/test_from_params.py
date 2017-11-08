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
            {"number": "377777777777770", "holder": "Jane Jones",
             "expiryMonth": "05", "expiryYear": "2018",
             "cvv": "1234"
             }
        )
        self.assertEqual(card_account_with_result_parameters.holder, "Jane Jones")
        self.assertEqual(card_account_with_result_parameters.number, "377777777777770")
        self.assertEqual(card_account_with_result_parameters.expiry_month, "05")
        self.assertEqual(card_account_with_result_parameters.expiry_year, "2018")
        self.assertEqual(card_account_with_result_parameters.cvv, "1234")

    def test_virtual_account_from_params(self):
        virtual_account_with_result_parameters = opp.facade.VirtualAccount.from_params(
            {"accountId": "1a2b3c4d5e6f7g8h9i", "password": "sy6KJsT8"}
        )
        self.assertEqual(virtual_account_with_result_parameters.account_id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(virtual_account_with_result_parameters.password, "sy6KJsT8")

    def test_bank_account_from_params(self):
        bank_account_with_result_parameters = opp.facade.BankAccount.from_params(
            {"holder": "Jane Jones",
             "bankName": "Deutsche Bank",
             "number": "1009534785",
             "iban": "DE23100000001234567890",
             "bankCode": "DEUTDEMM",
             "bic": "DEUTDEFF",
             "country": "DE",
             "mandate": {"id": "1a2b3c4d5e6f7g8h9i",
                         "dateOfSignature": "2015-07-09"
                         },
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
        self.assertEqual(bank_account_with_result_parameters.mandate.id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(bank_account_with_result_parameters.mandate.date_of_signature, "2015-07-09")
        self.assertEqual(bank_account_with_result_parameters.transaction_due_date, "2015-07-09")

    def test_customer_from_params(self):
        customer_with_result_parameters = opp.facade.Customer.from_params(
            {"merchantCustomerId": "1a2b3c4d5e6f7g8h9i",
             "givenName": "Jane",
             "surname": "Jones",
             "sex": "F",
             "birthDate": "1983-10-05",
             "phone": "+49 123456789",
             "mobile": "+49 987654321",
             "email": "jane.jones@test.de",
             "companyName": "Test Company",
             "identificationDocType": "TAXSTATEMENT",
             "identificationDocId": "a1b2c3d4e5f6g7h8i9",
             "ip": "XX.XXX.XX.XXX"
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
            {"street1": "Street 1",
             "street2": "Street 2",
             "city": "Test city",
             "state": "Test state",
             "postcode": "12345",
             "country": "DE"
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
            {"givenName": "Jane",
             "surname": "Jones",
             "street1": "Street 1",
             "street2": "Street 2",
             "city": "Test city",
             "state": "Test state",
             "postcode": "12345",
             "country": "DE"
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
        item = {"name": "T-shirt",
                "merchantItemId": "1a2b3c4d5e6f7g8h9i",
                "quantity": "1",
                "type": "XL",
                "price": "5",
                "currency": "EUR",
                "description": "Summer",
                "tax": "0.25",
                "shipping": "1",
                "discount": "5"
                }
        second_item = {"name": "FIFA16",
                       "merchantItemId": "2b3c4d5e6f7g8h9i1a",
                       "quantity": "1",
                       "type": "PS4",
                       "price": "55",
                       "currency": "EUR",
                       "description": "New",
                       "tax": "0.25",
                       "shipping": "1",
                       "discount": "5"
                       }
        list_of_items = [item, second_item]
        cart = opp.facade.Cart.from_params(list_of_items)

        self.assertEqual(cart.items[0].name, "T-shirt")
        self.assertEqual(cart.items[0].merchant_item_id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(cart.items[0].quantity, "1")
        self.assertEqual(cart.items[0].type, "XL")
        self.assertEqual(cart.items[0].price, "5")
        self.assertEqual(cart.items[0].currency, "EUR")
        self.assertEqual(cart.items[0].description, "Summer")
        self.assertEqual(cart.items[0].tax, "0.25")
        self.assertEqual(cart.items[0].shipping, "1")
        self.assertEqual(cart.items[0].discount, "5")
        self.assertEqual(cart.items[1].name, "FIFA16")
        self.assertEqual(cart.items[1].merchant_item_id, "2b3c4d5e6f7g8h9i1a")
        self.assertEqual(cart.items[1].quantity, "1")
        self.assertEqual(cart.items[1].type, "PS4")
        self.assertEqual(cart.items[1].price, "55")
        self.assertEqual(cart.items[1].currency, "EUR")
        self.assertEqual(cart.items[1].description, "New")
        self.assertEqual(cart.items[1].tax, "0.25")
        self.assertEqual(cart.items[1].shipping, "1")
        self.assertEqual(cart.items[1].discount, "5")

    def test_result_from_params(self):
        result_with_result_parameters = opp.facade.Result.from_params(
            {"code": "000.100.110",
             "description": "Request successfully processed",
             "avsResponse": "Y",
             "cvvResponse": "M",
             }
        )
        self.assertEqual(result_with_result_parameters.code, "000.100.110")
        self.assertEqual(result_with_result_parameters.description, "Request successfully processed")
        self.assertEqual(result_with_result_parameters.avs_response, "Y")
        self.assertEqual(result_with_result_parameters.cvv_response, "M")

    def test_merchant_from_params(self):
        bank_account_parameters = {"bankAccount": {"holder": "Jane Jones",
                                                   "number": "1009534785",
                                                   "iban": "DE23100000001234567890",
                                                   "country": "DE"
                                                   }
                                   }
        merchant = opp.facade.Merchant.from_params(bank_account_parameters)
        self.assertEqual(merchant.bank_account.holder, "Jane Jones")
        self.assertEqual(merchant.bank_account.number, "1009534785")
        self.assertEqual(merchant.bank_account.iban, "DE23100000001234567890")
        self.assertEqual(merchant.bank_account.country, "DE")

    def test_mandate_from_params(self):
        mandate_with_result_parameters = opp.facade.Mandate.from_params(
            {"id": "1a2b3c4d5e6f7g8h9i",
             "dateOfSignature": "2015-07-09"
             }
        )
        self.assertEqual(mandate_with_result_parameters.id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(mandate_with_result_parameters.date_of_signature, "2015-07-09")

    def test_parameter_from_params(self):
        parameter_with_result_parameters = opp.facade.Parameter.from_params(
            {"name": "test_parameter",
             "value": "test"
             }
        )
        self.assertEqual(parameter_with_result_parameters.name, "test_parameter")
        self.assertEqual(parameter_with_result_parameters.value, "test")

    def test_redirect_from_params(self):
        redirect_parameters = {"url": "http://mupteste.comercioeletronico.com.br/sepsBoletoRet/15300/prepara_pagto.asp",
                               "parameters": [
                                   {"name": "cdk10",
                                    "value": "0AWe9qIp0v8pXrJtFrxF+w=="
                                    },
                                   {"name": "cdk6",
                                    "value": "lxJCnzrEzeM="
                                    }
                               ]
                               }
        redirect = opp.facade.Redirect.from_params(redirect_parameters)
        self.assertEqual(redirect.url, "http://mupteste.comercioeletronico.com.br/sepsBoletoRet/15300/prepara_pagto.asp")
        self.assertEqual(redirect.parameters[0].name, "cdk10")
        self.assertEqual(redirect.parameters[0].value, "0AWe9qIp0v8pXrJtFrxF+w==")
        self.assertEqual(redirect.parameters[1].name, "cdk6")
        self.assertEqual(redirect.parameters[1].value, "lxJCnzrEzeM=")

    def test_response_parameters_from_params(self):
        response_parameters = {"id": "8a8294494e735cfa014e763863a80add",
                               "paymentType": "PA",
                               "paymentBrand": "BOLETO",
                               "amount": "1.03",
                               "currency": "BRL",
                               "descriptor": "2203.5434.7682 OPP_Channel",
                               "result": {
                                   "code": "000.100.112",
                                   "description": "Request successfully processed in 'Merchant in Connector Test Mode'"
                               },
                               "cardAccount": {
                                   "number": "377777777777770",
                                   "holder": "Jane Jones",
                                   "expiryMonth": "05",
                                   "expiryYear": "2018",
                                   "cvv": "1234"
                               },
                               "virtualAccount": {
                                   "accountId": "1a2b3c4d5e6f7g8h9i",
                                   "password": "sy6KJsT8"
                               },
                               "bankAccount": {
                                   "holder": "Jane Jones",
                                   "bankName": "Deutsche Bank",
                                   "number": "1009534785",
                                   "iban": "DE23100000001234567890",
                                   "bankCode": "DEUTDEMM",
                                   "bic": "DEUTDEFF",
                                   "country": "DE",
                                   "mandate": {"id": "1a2b3c4d5e6f7g8h9i",
                                               "dateOfSignature": "2015-07-09"
                                               },
                                   "transactionDueDate": "2015-07-09"
                               },
                               "merchant": {
                                   "bankAccount": {
                                       "holder": "merchantName",
                                       "number": "15300",
                                       "iban": "DE23100000001234567890",
                                       "country": "BR"
                                   }
                               },
                               "customer": {
                                   "givenName": "Braziliano",
                                   "surname": "Babtiste"
                               },
                               "billing": {
                                   "street1": "Amazonstda",
                                   "city": "Brasilia",
                                   "state": "DE",
                                   "postcode": "12345678",
                                   "country": "BR"
                               },
                               "shipping": {
                                   "givenName": "Jane",
                                   "surname": "Jones",
                                   "street1": "Riostda",
                                   "city": "Rio de Janeiro",
                                   "state": "FE",
                                   "postcode": "12345698",
                                   "country": "BR"
                               },
                               "cart": {
                                   "items": [
                                       {
                                           "name": "T-shirt",
                                           "merchantItemId": "1a2b3c4d5e6f7g8h9i",
                                           "quantity": "1",
                                           "type": "XL",
                                           "price": "5",
                                           "currency": "EUR",
                                           "description": "Summer",
                                           "tax": "0.25",
                                           "shipping": "1",
                                           "discount": "5"
                                       },
                                       {
                                           "name": "FIFA16",
                                           "merchantItemId": "2b3c4d5e6f7g8h9i1a",
                                           "quantity": "1",
                                           "type": "PS4",
                                           "price": "55",
                                           "currency": "EUR",
                                           "description": "New",
                                           "tax": "0.25",
                                           "shipping": "1",
                                           "discount": "5"
                                       }
                                   ]
                               },
                               "customParameters": {
                                   "BRADESCO_cpfsacado": "11111111111"
                               },
                               "redirect": {
                                   "url": "http://mupteste.comercioeletronico.com.br/sepsBoletoRet/15300/prepara_pagto.asp",
                                   "parameters": [
                                       {
                                           "name": "cdk10",
                                           "value": "0AWe9qIp0v8pXrJtFrxF+w=="
                                       },
                                       {
                                           "name": "cdk6",
                                           "value": "lxJCnzrEzeM="
                                       }
                                   ]
                               },
                               "buildNumber": "20150707-105209.r185912.opp-tags-20150709_lr",
                               "timestamp": "2015-07-10 04:28:03+0000",
                               "ndc": "8a8294174b7ecb28014b9699220015ca_8a102b3e46974c83bbeb0bfc62a9518e",
                               "resultDetails": {
                                   "ConnectorTxID1": "8a8393c259876e841989ab6f4da1408d",
                                   "ConnectorTxID2": "614486",
                                   "ConnectorTxID3": "827428|||74301731986",
                                   "clearingInstituteName": "Some Institute",
                               },
                               "registrationId": "8a82944a5dbc8820015dc30fc19e3641"
                               }
        response = opp.facade.ResponseParameters.from_params(response_parameters)
        self.assertEqual(response.id, "8a8294494e735cfa014e763863a80add")
        self.assertEqual(response.payment_type, "PA")
        self.assertEqual(response.payment_brand, "BOLETO")
        self.assertEqual(response.amount, "1.03")
        self.assertEqual(response.descriptor, "2203.5434.7682 OPP_Channel")
        self.assertEqual(response.result.code, "000.100.112")
        self.assertEqual(response.result.description, "Request successfully processed in 'Merchant in Connector Test Mode'")
        self.assertEqual(response.card_account.number, "377777777777770")
        self.assertEqual(response.card_account.holder, "Jane Jones")
        self.assertEqual(response.card_account.expiry_month, "05")
        self.assertEqual(response.card_account.expiry_year, "2018")
        self.assertEqual(response.card_account.cvv, "1234")
        self.assertEqual(response.virtual_account.account_id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(response.virtual_account.password, "sy6KJsT8")
        self.assertEqual(response.bank_account.holder, "Jane Jones")
        self.assertEqual(response.bank_account.bank_name, "Deutsche Bank")
        self.assertEqual(response.bank_account.iban, "DE23100000001234567890")
        self.assertEqual(response.bank_account.bank_code, "DEUTDEMM")
        self.assertEqual(response.bank_account.bic, "DEUTDEFF")
        self.assertEqual(response.bank_account.country, "DE")
        self.assertEqual(response.bank_account.mandate.id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(response.bank_account.mandate.date_of_signature, "2015-07-09")
        self.assertEqual(response.bank_account.transaction_due_date, "2015-07-09")
        self.assertEqual(response.customer.given_name, "Braziliano")
        self.assertEqual(response.customer.surname, "Babtiste")
        self.assertEqual(response.billing_address.street1, "Amazonstda")
        self.assertEqual(response.billing_address.city, "Brasilia")
        self.assertEqual(response.billing_address.state, "DE")
        self.assertEqual(response.billing_address.postcode, "12345678")
        self.assertEqual(response.billing_address.country, "BR")
        self.assertEqual(response.shipping_address.given_name, "Jane")
        self.assertEqual(response.shipping_address.surname, "Jones")
        self.assertEqual(response.shipping_address.street1, "Riostda")
        self.assertEqual(response.shipping_address.city, "Rio de Janeiro")
        self.assertEqual(response.shipping_address.state, "FE")
        self.assertEqual(response.shipping_address.postcode, "12345698")
        self.assertEqual(response.shipping_address.country, "BR")
        self.assertEqual(response.cart.items[0].name, "T-shirt")
        self.assertEqual(response.cart.items[0].merchant_item_id, "1a2b3c4d5e6f7g8h9i")
        self.assertEqual(response.cart.items[0].quantity, "1")
        self.assertEqual(response.cart.items[0].type, "XL")
        self.assertEqual(response.cart.items[0].price, "5")
        self.assertEqual(response.cart.items[0].currency, "EUR")
        self.assertEqual(response.cart.items[0].description, "Summer")
        self.assertEqual(response.cart.items[0].tax, "0.25")
        self.assertEqual(response.cart.items[0].shipping, "1")
        self.assertEqual(response.cart.items[0].discount, "5")
        self.assertEqual(response.cart.items[1].name, "FIFA16")
        self.assertEqual(response.cart.items[1].merchant_item_id, "2b3c4d5e6f7g8h9i1a")
        self.assertEqual(response.cart.items[1].quantity, "1")
        self.assertEqual(response.cart.items[1].type, "PS4")
        self.assertEqual(response.cart.items[1].price, "55")
        self.assertEqual(response.cart.items[1].currency, "EUR")
        self.assertEqual(response.cart.items[1].description, "New")
        self.assertEqual(response.cart.items[1].tax, "0.25")
        self.assertEqual(response.cart.items[1].shipping, "1")
        self.assertEqual(response.cart.items[1].discount, "5")
        self.assertEqual(response.merchant.bank_account.holder, "merchantName")
        self.assertEqual(response.merchant.bank_account.number, "15300")
        self.assertEqual(response.merchant.bank_account.iban, "DE23100000001234567890")
        self.assertEqual(response.merchant.bank_account.country, "BR")
        self.assertEqual(response.redirect.parameters[0].name, "cdk10")
        self.assertEqual(response.redirect.parameters[0].value, "0AWe9qIp0v8pXrJtFrxF+w==")
        self.assertEqual(response.redirect.parameters[1].name, "cdk6")
        self.assertEqual(response.redirect.parameters[1].value, "lxJCnzrEzeM=")
        self.assertEqual(response.build_number, "20150707-105209.r185912.opp-tags-20150709_lr")
        self.assertEqual(response.timestamp, "2015-07-10 04:28:03+0000")
        self.assertEqual(response.ndc, "8a8294174b7ecb28014b9699220015ca_8a102b3e46974c83bbeb0bfc62a9518e")
        self.assertEqual(response.result_details["ConnectorTxID1"], "8a8393c259876e841989ab6f4da1408d")
        self.assertEqual(response.result_details["ConnectorTxID2"], "614486")
        self.assertEqual(response.result_details["ConnectorTxID3"], "827428|||74301731986")
        self.assertEqual(response.result_details["clearingInstituteName"], "Some Institute")
        self.assertEqual(response.registration_id, "8a82944a5dbc8820015dc30fc19e3641")
