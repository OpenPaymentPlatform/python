__author__ = 'PAY.ON'
import opp

if __name__ == "__main__":
    api = opp.core.API(**{"authentication.userId": "8a8294174b7ecb28014b9699220015cc",
                          "authentication.password": "sy6KJsT8",
                          "authentication.entityId": "8a8294174b7ecb28014b9699220015ca"})

    preauthorization = api.payments().create(**{"amount": "92.00",
                                                "currency": "EUR",
                                                "paymentBrand": "AMEX",
                                                "paymentType": "PA",
                                                "descriptor": "Test PA",
                                                "card.number": "377777777777770",
                                                "card.holder": "Jane Jones",
                                                "card.expiryMonth": "05",
                                                "card.expiryYear": "2018",
                                                "card.cvv": "1234"})

    print("------Preauthorization create: ------")
    print(preauthorization)

    preauthorization2 = api.payments(payment_id=preauthorization['id']).get()

    print("------Preauthorization get: ------")
    print(preauthorization2)

    reversal = api.payments(payment_id=preauthorization['id']).create(**{"paymentType": "RV"})

    print("------Reversal create: ------")
    print(reversal)

    checkout = api.checkouts().create(**{"amount": "92.00",
                                         "currency": "EUR",
                                         "paymentType": "PA"})
    print("------Checkout create: ------")
    print(checkout)

    checkout = api.checkouts().create(**{"amount": "92.00",
                                         "currency": "EUR",
                                         "paymentType": "PA"})
    print("------Checkout create: ------")
    print(checkout)

    checkout2 = api.checkouts(checkout_id=checkout['id']).get()

    print("------Checkout get: ------")
    print(checkout2)

    registration = api.registrations().create(**{"paymentBrand": "AMEX",
                                                 "descriptor": "Test PA",
                                                 "card.number": "377777777777770",
                                                 "card.holder": "Jane Jones",
                                                 "card.expiryMonth": "05",
                                                 "card.expiryYear": "2018",
                                                 "card.cvv": "1234"})

    print("------Registration create: ------")
    print(registration)

    registration2 = api.registrations(registration_id=registration['id']).get()

    print("------Registration get: ------")
    print(registration2)

    registration3 = api.registrations().create(**{"paymentBrand": "BOLETO",
                                                  "customer.givenName": "Braziliano",
                                                  "customer.surname": "Babtiste",
                                                  "billing.city": "Brasilia",
                                                  "billing.country": "BR",
                                                  "billing.state": "SP",
                                                  "billing.street1": "Amazonstda",
                                                  "billing.postcode": "12345678",
                                                  "customParameters[BRADESCO_cpfsacado]": "11111111111",
                                                  "shopperResultUrl": "https://docs.oppwa.com",
                                                  "testMode": "EXTERNAL"})

    print("------Registration with async payment method------")
    print(registration3)

    result = api.registrations(registration_id=registration['id']).delete()

    print("------Registration delete: ------")
    print(result)