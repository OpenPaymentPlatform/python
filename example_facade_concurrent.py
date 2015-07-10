__author__ = 'PAY.ON'
import opp
import logging

import threading
logger = logging.getLogger("example_facade_concurrent")


def success_worker(num, worker_api):
    #success_worker creates a transaction and should succeed

    # create payment parameters
    basic_payment = opp.facade.BasicPayment(amount='92.00', currency='EUR', payment_brand='AMEX', descriptor='Test Amex')

    # create card account parameters
    card_account = opp.facade.CardAccount(holder='Jane Jones', number='377777777777770', expiry_month='05',
                                          expiry_year='2018',
                                          cvv='1234')

    try:
        preauthorization = worker_api.preauthorizations().create(basic_payment, card_account)
        logger.debug("Success Worker #{0} RESPONSE: {1}".format(num, preauthorization.__dict__))
    except opp.facade.ApiError as e:
        #handle error
        print(e)


def failure_worker(num, worker_api):
    #failure_worker tries to create a transaction without sending any payment data and should fail with an exception,
    #so output will come from except case
    try:
        worker_api.preauthorizations().create()
    except opp.facade.ApiError as e:
        #handle error
        logger.debug("Failure Worker #{0} RESPONSE: {1}".format(num, e))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='opp.log')
    threads = []
    authentication = opp.facade.Authentication(user_id='8a8294174b7ecb28014b9699220015cc', password='sy6KJsT8',
                                               entity_id='8a8294174b7ecb28014b9699220015ca')

    # initialize OPP API with authentication object
    api = opp.facade.API(authentication)
    #start workers with passing through the shared opp.facade.API object
    for i in range(5):
        t = threading.Thread(target=success_worker, args=(i, api, ))
        t2 = threading.Thread(target=failure_worker, args=(i, api, ))
        threads.append(t)
        t2.start()
        t.start()



