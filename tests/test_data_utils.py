__author__ = 'PAY.ON'
import random


# Supported payment types

syncPaymentTypes = ["DIRECTDEBIT_SEPA",  # order matters for DIRECTDEBIT_SEPA
                    "AMEX",
                    "ASYACARD",
                    "AXESS",
                    "BONUS",
                    "CARTEBLEUE",
                    "DANKORT",
                    "DINERS",
                    "DISCOVER",
                    "HIPERCARD",
                    "JCB",
                    "MAESTRO",
                    "MASTER",
                    "VISA",
                    "VISAELECTRON",
                    "VPAY",
                    "WORLD"]

asyncPaymentTypes = ["BOLETO", "CHINAUNIONPAY", "DAOPAY", "EPS", "GIROPAY", "IDEAL", "KLARNA_INSTALLMENTS",
                     "KLARNA_INVOICE",
                     "MONEYBOOKERS", "PAYOLUTION_ELV", "PAYOLUTION_INS", "PAYOLUTION_INVOICE", "PAYPAL", "PAYSAFECARD",
                     "PAYTRAIL",
                     "PF_KARTE_DIRECT", "POLI", "PREPAYMENT", "PRZELEWY", "SOFORTUEBERWEISUNG", "TRUSTLY",
                     "TRUSTPAY_VA", "UKASH", "YANDEX"]

# Data utils functions


def random_async_payment_brand():
    return str(asyncPaymentTypes[random.randrange(0, len(asyncPaymentTypes) - 1, 1)])


def random_sync_payment_brand():
    return str(syncPaymentTypes[random.randrange(1, len(syncPaymentTypes) - 1, 1)])

# Authentication test data

authentication = {"authentication.userId": "8a8294174b7ecb28014b9699220015cc",
                  "authentication.password": "sy6KJsT8",
                  "authentication.entityId": "8a8294174b7ecb28014b9699220015ca"}


# Sync payments test data

DIRECTDEBIT_SEPA = {"amount": "12.12",
                    "currency": "EUR",
                    "paymentBrand": "DIRECTDEBIT_SEPA",
                    "bankAccount.bic": "MARKDEF1100",
                    "bankAccount.iban": "DE23100000001234567890",
                    "bankAccount.country": "DE",
                    "bankAccount.holder": "Jane Jones"}

AMEX = {"amount": "92.00",
        "currency": "EUR",
        "paymentBrand": "AMEX",
        "card.number": "377777777777770",
        "card.holder": "Jane Jones",
        "card.expiryMonth": "05",
        "card.expiryYear": "2018",
        "card.cvv": "1234"
}

ASYACARD = {"amount": "92.00",
            "currency": "TRY",
            "paymentBrand": "ASYACARD",
            "card.number": "4022751585445574",
            "card.holder": "Jane Jones",
            "card.expiryMonth": "05",
            "card.expiryYear": "2018",
            "card.cvv": "123"
}

AXESS = {"amount": "92.00",
         "currency": "TRY",
         "paymentBrand": "AXESS",
         "card.number": "4200000000000000",
         "card.holder": "Jane Jones",
         "card.expiryMonth": "05",
         "card.expiryYear": "2018",
         "card.cvv": "123"
}

BONUS = {"amount": "92.00",
         "currency": "TRY",
         "paymentBrand": "BONUS",
         "card.number": "4090700500869563",
         "card.holder": "Jane Jones",
         "card.expiryMonth": "05",
         "card.expiryYear": "2018",
         "card.cvv": "123"
}

CARTEBLEUE = {"amount": "92.00",
              "currency": "EUR",
              "paymentBrand": "CARTEBLEUE",
              "card.number": "5555555555554444",
              "card.holder": "Jane Jones",
              "card.expiryMonth": "05",
              "card.expiryYear": "2018",
              "card.cvv": "123"
}

DANKORT = {"amount": "92.00",
         "currency": "EUR",
         "paymentBrand": "DANKORT",
         "card.number": "5019717010103742",
         "card.holder": "Jane Jones",
         "card.expiryMonth": "05",
         "card.expiryYear": "2018",
         "card.cvv": "123"
}

DINERS = {"amount": "92.00",
          "currency": "EUR",
          "paymentBrand": "DINERS",
          "card.number": "36961903000009",
          "card.holder": "Jane Jones",
          "card.expiryMonth": "05",
          "card.expiryYear": "2018",
          "card.cvv": "123"
}

DISCOVER = {"amount": "92.00",
            "currency": "EUR",
            "paymentBrand": "DISCOVER",
            "card.number": "6011587918359498",
            "card.holder": "Jane Jones",
            "card.expiryMonth": "05",
            "card.expiryYear": "2018",
            "card.cvv": "123"
}

HIPERCARD = {"amount": "92.00",
             "currency": "EUR",
             "paymentBrand": "HIPERCARD",
             "card.number": "6062825624254001",
             "card.holder": "Jane Jones",
             "card.expiryMonth": "05",
             "card.expiryYear": "2018",
             "card.cvv": "123"
}

JCB = {"amount": "92.00",
       "currency": "EUR",
       "paymentBrand": "JCB",
       "card.number": "3541599999092431",
       "card.holder": "Jane Jones",
       "card.expiryMonth": "05",
       "card.expiryYear": "2018",
       "card.cvv": "123"
}

MAESTRO = {"amount": "92.00",
           "currency": "EUR",
           "paymentBrand": "MAESTRO",
           "card.number": "6799851000000032",
           "card.holder": "Jane Jones",
           "card.expiryMonth": "05",
           "card.expiryYear": "2018",
           "card.cvv": "123"
}

MASTER = {"amount": "92.00",
          "currency": "EUR",
          "paymentBrand": "MASTER",
          "card.number": "5454545454545454",
          "card.holder": "Jane Jones",
          "card.expiryMonth": "05",
          "card.expiryYear": "2018",
          "card.cvv": "123"
}

VISA = {"amount": "92.00",
        "currency": "EUR",
        "paymentBrand": "VISA",
        "card.number": "4200000000000000",
        "card.holder": "Jane Jones",
        "card.expiryMonth": "05",
        "card.expiryYear": "2018",
        "card.cvv": "123"
}

VISAELECTRON = {"amount": "92.00",
                "currency": "EUR",
                "paymentBrand": "VISAELECTRON",
                "card.number": "4917300800000000",
                "card.holder": "Jane Jones",
                "card.expiryMonth": "05",
                "card.expiryYear": "2018",
                "card.cvv": "123"
}

VPAY = {"amount": "92.00",
        "currency": "EUR",
        "paymentBrand": "VPAY",
        "card.number": "4822000000000000003",
        "card.holder": "Jane Jones",
        "card.expiryMonth": "05",
        "card.expiryYear": "2018",
        "card.cvv": "123"
}

WORLD = {"amount": "92.00",
         "currency": "TRY",
         "paymentBrand": "WORLD",
         "card.number": "4200000000000000",
         "card.holder": "Jane Jones",
         "card.expiryMonth": "05",
         "card.expiryYear": "2018",
         "card.cvv": "123"
}

#Async payments test data

BOLETO = {"amount": "1.03",
          "currency": "BRL",
          "paymentBrand": "BOLETO",
          "customer.givenName": "Braziliano",
          "customer.surname": "Babtiste",
          "billing.city": "Brasilia",
          "billing.country": "BR",
          "billing.state": "SP",
          "billing.street1": "Amazonstda",
          "billing.postcode": "12345678",
          "customParameters[BRADESCO_cpfsacado]": "11111111111",
          "shopperResultUrl": "https://docs.oppwa.com", "testMode": "EXTERNAL",
          "testMode": "EXTERNAL"}

CHINAUNIONPAY = {"amount": "12.12",
                 "currency": "USD",
                 "paymentBrand": "CHINAUNIONPAY",
                 "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

DAOPAY = {"amount": "12.12",
          "currency": "EUR",
          "paymentBrand": "DAOPAY",
          "billing.country": "DE",
          "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

EPS = {"amount": "12.12",
       "currency": "EUR",
       "paymentBrand": "EPS",
       "bankAccount.country": "AT",
       "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

GIROPAY = {"amount": "12.12",
           "currency": "EUR",
           "paymentBrand": "GIROPAY",
           "bankAccount.bic": "TESTDETT421",
           "bankAccount.iban": "DE14940593100000012346",
           "bankAccount.country": "DE", "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

IDEAL = {"amount": "92.12",
         "currency": "EUR",
         "paymentBrand": "IDEAL",
         "bankAccount.bankName": "ING_TEST",
         "bankAccount.country": "NL",
         "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

KLARNA_INSTALLMENTS = {"amount": "92.12",
                       "currency": "EUR",
                       "paymentBrand": "KLARNA_INSTALLMENTS",
                       "customer.givenName": "Jane",
                       "customer.surname": "Jones",
                       "billing.country": "SE",
                       "cart.items[0].merchantItemId": "1",
                       "cart.items[0].discount": "0.00",
                       "cart.items[0].quantity": "5",
                       "cart.items[0].name": "Product 1",
                       "cart.items[0].price": "1.00",
                       "cart.items[0].tax": "6.00",
                       "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

KLARNA_INVOICE = {"amount": "92.12",
                  "currency": "EUR",
                  "paymentBrand": "KLARNA_INVOICE",
                  "customer.givenName": "Jane",
                  "customer.surname": "Jones",
                  "billing.country": "SE",
                  "cart.items[0].merchantItemId": "1",
                  "cart.items[0].discount": "0.00",
                  "cart.items[0].quantity": "5",
                  "cart.items[0].name": "Product 1",
                  "cart.items[0].price": "1.00",
                  "cart.items[0].tax": "6.00",
                  "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

MONEYBOOKERS = {"amount": "92.12",
                 "currency": "USD",
                 "paymentBrand": "MONEYBOOKERS",
                 "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PAYOLUTION_ELV = {"amount": "92.12",
                  "currency": "EUR",
                  "paymentBrand": "PAYOLUTION_ELV",
                  "customer.givenName": "Jane",
                  "customer.surname": "Jones",
                  "customer.email": "test@test.com",
                  "customer.ip": "123.123.123.123",
                  "billing.country": "DE",
                  "billing.street1": "123 Street",
                  "billing.city": "Munich",
                  "billing.postcode": "A1 2BC",
                  "customParameters[PAYOLUTION_ITEM_PRICE_1]": "2.00",
                  "customParameters[PAYOLUTION_ITEM_DESCR_1]": "Test item #1",
                  "customParameters[PAYOLUTION_ITEM_PRICE_2]": "3.00",
                  "customParameters[PAYOLUTION_ITEM_DESCR_2]": "Test item #2",
                  "testMode": "EXTERNAL",
                  "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PAYOLUTION_INS = {"amount": "92.12",
                  "currency": "EUR",
                  "paymentBrand": "PAYOLUTION_INS",
                  "customer.givenName": "Jane",
                  "customer.surname": "Jones",
                  "customer.email": "test@test.com",
                  "customer.ip": "123.123.123.123",
                  "billing.country": "DE",
                  "billing.street1": "123 Street",
                  "billing.city": "Munich",
                  "billing.postcode": "A1 2BC",
                  "customParameters[PAYOLUTION_ITEM_PRICE_1]": "2.00",
                  "customParameters[PAYOLUTION_ITEM_DESCR_1]": "Test item #1",
                  "customParameters[PAYOLUTION_ITEM_PRICE_2]": "3.00",
                  "customParameters[PAYOLUTION_ITEM_DESCR_2]": "Test item #2",
                  "testMode": "EXTERNAL",
                  "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PAYOLUTION_INVOICE = {"amount": "92.12",
                      "currency": "EUR",
                      "paymentBrand": "PAYOLUTION_INS",
                      "customer.givenName": "Jane",
                      "customer.surname": "Jones",
                      "customer.email": "test@test.com",
                      "customer.ip": "123.123.123.123",
                      "billing.country": "DE",
                      "billing.street1": "123 Street",
                      "billing.city": "Munich",
                      "billing.postcode": "A1 2BC",
                      "customParameters[PAYOLUTION_ITEM_PRICE_1]": "2.00",
                      "customParameters[PAYOLUTION_ITEM_DESCR_1]": "Test item #1",
                      "customParameters[PAYOLUTION_ITEM_PRICE_2]": "3.00",
                      "customParameters[PAYOLUTION_ITEM_DESCR_2]": "Test item #2",
                      "testMode": "EXTERNAL",
                      "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PAYPAL = {"amount": "92.12",
          "currency": "EUR",
          "paymentBrand": "PAYPAL",
          "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PAYSAFECARD = {"amount": "92.12",
               "currency": "EUR",
               "paymentBrand": "PAYSAFECARD",
               "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PAYTRAIL = {"amount": "92.12",
            "currency": "EUR",
            "paymentBrand": "PAYTRAIL",
            "bankAccount.bankName": "Bank Paytrail",
            "bankAccount.country": "FI",
            "bankAccount.holder": "Jane Jones",
            "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PF_KARTE_DIRECT = {"amount": "92.12",
                   "currency": "CHF",
                   "paymentBrand": "PF_KARTE_DIRECT",
                   "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

POLI = {"amount": "92.12",
        "currency": "AUD",
        "paymentBrand": "POLI",
        "bankAccount.country": "AU",
        "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PREPAYMENT = {"amount": "92.12",
              "currency": "EUR",
              "paymentBrand": "PREPAYMENT",
              "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

PRZELEWY = {"amount": "92.12",
            "currency": "PLN",
            "paymentBrand": "PRZELEWY",
            "customer.givenName": "Jane",
            "customer.surname": "Jones",
            "customer.email": "test@test.com",
            "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

SOFORTUEBERWEISUNG = {"amount": "92.12",
                      "currency": "EUR",
                      "paymentBrand": "SOFORTUEBERWEISUNG",
                      "bankAccount.country": "AT",
                      "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

TRUSTLY = {"amount": "92.12",
           "currency": "EUR",
           "paymentBrand": "TRUSTLY",
           "customer.merchantCustomerId": "123456",
           "customer.givenName": "Jane",
           "customer.surname": "Jones",
           "billing.country": "DE",
           "merchantTransactionId": "abc123",
           "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

TRUSTPAY_VA = {"amount": "92.12",
               "currency": "EUR",
               "paymentBrand": "TRUSTPAY_VA",
               "customer.givenName": "Jane",
               "customer.surname": "Jones",
               "customer.email": "test@test.com",
               "testMode": "EXTERNAL",
               "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

UKASH = {"amount": "92.12",
         "currency": "EUR",
         "paymentBrand": "UKASH",
         "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}

YANDEX = {"amount": "92.12",
          "currency": "RUB",
          "paymentBrand": "YANDEX",
          "shopperResultUrl": "https://docs.oppwa.com/?q=initial-payment"}
