__author__ = 'PAY.ON'
import opp
import logging
logging.basicConfig(level=logging.DEBUG, filename='opp.log')
logger = logging.getLogger(__name__)

logger.info(('Example facade logging level {0} logs to file {1}'.format(logging.DEBUG, 'opp.log')))

logger.debug('Creating facade objects...')
authentication = opp.facade.Authentication(user_id='8a8294174b7ecb28014b9699220015cc', password='sy6KJsT8',
                                           entity_id='8a8294174b7ecb28014b9699220015ca')

# initialize OPP API with authentication object
api = opp.facade.API(authentication)

# create payment parameters
basic_payment = opp.facade.BasicPayment(amount='92.00', currency='EUR', payment_brand='AMEX', descriptor='Test Amex')

# create card account parameters
card_account = opp.facade.CardAccount(holder='Jane Jones', number='377777777777770', expiry_month='05',
                                      expiry_year='2018',
                                      cvv='1234')
preauthorization = None

try:
    # create preauthorization
    logger.info('Calling opp.facade.API.preauthorizations().create ...')
    preauthorization = api.preauthorizations().create(basic_payment, card_account)
    logger.debug('Result from opp.facade.API.preauthorizations().create: result.code: %s result.description: %s',
                 preauthorization.result.code, preauthorization.result.description)
except opp.facade.ApiError as e:
    #handle error
    print(e)

if preauthorization is not None:
    try:
        # create transaction by capturing preauthorization
        logger.info('Calling captures(payment_id=preauthorization.id).create() ...')
        transaction = api.captures(payment_id=preauthorization.id).create(basic_payment)
        logger.debug('Result from captures(payment_id=preauthorization.id).create(): result.code: %s '
                     'result.description: %s', preauthorization.result.code, preauthorization.result.description)
    except opp.facade.ApiError as e:
        #handle error
        print(e)

