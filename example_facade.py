import opp

__author__ = 'PAY.ON'
# change module name, package, project
#use opp instead

# create authentication object

authentication = opp.facade.Authentication(user_id='8a8294174b7ecb28014b9699220015cc', password='sy6KJsT8',
                                           entity_id='8a8294174b7ecb28014b9699220015ca')

# initialize Payon Api with authentication object and mode
api = opp.facade.API(authentication)

# create payment parameters
basic_payment = opp.facade.BasicPayment(amount='92.00', currency='EUR', payment_brand='AMEX', descriptor='Test Amex')

# create card account parameters
card_account = opp.facade.CardAccount(holder='Jane Jones', number='377777777777770', expiry_month='05',
                                      expiry_year='2018',
                                      cvv='1234')

try:
    # create preauthorization
    preauthorization1 = api.preauthorizations().create(basic_payment, card_account)
    if preauthorization1 is not None:
        print(preauthorization1)
        print(type(preauthorization1))
        print("---------------------Preauth Object Response-------------------")
        print("---------------------Object Dict-------------------------------")
        print(preauthorization1.__dict__)
        print("---------------------Object Nested Object-------------------------------")
        print(preauthorization1.result)
        print("---------------------Object Nested Object Property-------------------------------")
        print(preauthorization1.result.code)

except opp.facade.ApiError as e:
    #handle error
    print(e)

try:
    # create transaction
    transaction1 = api.debits().create(basic_payment, card_account)
    if transaction1 is not None:
        print("---------------------Transaction Response-------------------")
        print(transaction1)
except opp.facade.ApiError as e:
    #handle error
    print(e)

try:
    # create capture with risk check
    cap1 = api.risk_checked_captures().create(basic_payment, card_account)
    print("---------------------Capture Response-------------------")
    print(cap1)
    print(cap1.__dict__)

except opp.facade.ApiError as e:
    #handle error
    print(e)
