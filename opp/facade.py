# coding=utf-8
__author__ = 'PAY.ON'
import opp.core
import opp.utils
import logging

logger = logging.getLogger(__name__)


class Authentication(object):
    def __init__(self, user_id=None, password=None, entity_id=None):
        """


        :rtype : object
        :param user_id:
        :param password:
        :param entity_id:
        """
        self.user_id = user_id
        self.password = password
        self.entity_id = entity_id

    def to_params(self):
        return {"authentication.userId": self.user_id,
                "authentication.password": self.password,
                "authentication.entityId": self.entity_id}


class BasicPayment(object):
    def __init__(self, amount=None, currency=None, payment_brand=None, descriptor=None, merchant_transaction_id=None,
                 merchant_invoice_id=None):
        """


        :rtype : object
        :param payment_brand:
        :param amount:
        :param currency:
        :param descriptor:
        :param merchant_transaction_id:
        :param merchant_invoice_id:
        """
        self.amount = amount
        self.currency = currency
        self.payment_brand = payment_brand
        self.descriptor = descriptor
        self.merchant_transaction_id = merchant_transaction_id
        self.merchant_invoice_id = merchant_invoice_id

    def to_params(self):
        return {"amount": self.amount,
                "currency": self.currency,
                "paymentBrand": self.payment_brand,
                "descriptor": self.descriptor,
                "merchantTransactionId": self.merchant_transaction_id,
                "merchantInvoiceId": self.merchant_invoice_id}


class CardAccount(object):
    def __init__(self, holder=None, number=None, expiry_month=None, expiry_year=None, cvv=None):
        """
        The card object holds all information regarding a credit or debit card account.

        :rtype : object
        :param holder:
        :param number:
        :param expiry_month:
        :param expiry_year:
        :param cvv:
        """
        self.holder = holder
        self.number = number
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.cvv = cvv

    def to_params(self):
        return {"card.holder": self.holder,
                "card.number": self.number,
                "card.expiryMonth": self.expiry_month,
                "card.expiryYear": self.expiry_year,
                "card.cvv": self.cvv}

    @staticmethod
    def from_params(params):
        if params is not None:
            return CardAccount(holder=params.get('holder'), number=params.get('number'),
                               expiry_month=params.get('expiryMonth'), expiry_year=params.get('expiryYear'),
                               cvv=params.get('cvv'))


class VirtualAccount(object):
    def __init__(self, account_id=None, password=None):
        """
        The virtual account object is used to send account-based payments, e.g. PAYPAL, NETELLER...

        :rtype : object
        :param account_id:
        :param password:
        """
        self.account_id = account_id
        self.password = password

    def to_params(self):
        return {"virtualAccount.accountId": self.account_id,
                "virtualAccount.password": self.password}

    @staticmethod
    def from_params(params):
        if params is not None:
            return VirtualAccount(account_id=params.get('accountId'), password=params.get('password'))


class BankAccount(object):
    def __init__(self, holder=None, bank_name=None, number=None, iban=None, bank_code=None, bic=None, country=None,
                 mandate_id=None, mandate_date_of_signature=None, transaction_due_date=None):
        """


        :rtype : object
        :param holder:
        :param bank_name:
        :param number:
        :param iban:
        :param bank_code:
        :param bic:
        :param country:
        :param mandate_id:
        :param mandate_date_of_signature:
        :param transaction_due_date:
        """
        self.holder = holder
        self.bank_name = bank_name
        self.number = number
        self.iban = iban
        self.bank_code = bank_code
        self.bic = bic
        self.country = country
        self.mandate_id = mandate_id
        self.mandate_date_of_signature = mandate_date_of_signature
        self.transaction_due_date = transaction_due_date

    def to_params(self):
        return {"bankAccount.holder": self.holder,
                "bankAccount.bankName": self.bank_name,
                "bankAccount.number": self.number,
                "bankAccount.iban": self.iban,
                "bankAccount.bankCode": self.bank_code,
                "bankAccount.bic": self.bic,
                "bankAccount.country": self.country,
                "bankAccount.mandate.id": self.mandate_id,
                "bankAccount.mandate.dateOfSignature": self.mandate_date_of_signature,
                "transactionDueDate": self.transaction_due_date}

    @staticmethod
    def from_params(params):
        if params is not None:
            return BankAccount(holder=params.get('holder'), bank_name=params.get('bankName'),
                               number=params.get('number'),
                               iban=params.get('iban'), bank_code=params.get('bankCode'), bic=params.get('bic'),
                               country=params.get('country'), mandate_id=params.get('mandate.id'),
                               mandate_date_of_signature=params.get('mandate.dateOfSignature'),
                               transaction_due_date=params.get('transactionDueDate'))


class Customer(object):
    def __init__(self, merchant_customer_id=None, given_name=None, surname=None, sex=None, birth_date=None, phone=None,
                 mobile=None, email=None, company_name=None, identification_doc_type=None, identification_doc_id=None,
                 customer_ip=None):
        """


        :rtype : object
        :param merchant_customer_id:
        :param given_name:
        :param surname:
        :param sex:
        :param birth_date:
        :param phone:
        :param mobile:
        :param email:
        :param company_name:
        :param identification_doc_type:
        :param identification_doc_id:
        :param customer_ip:
        """
        self.merchant_customer_id = merchant_customer_id
        self.given_name = given_name
        self.surname = surname
        self.sex = sex
        self.birth_date = birth_date
        self.phone = phone
        self.mobile = mobile
        self.email = email
        self.company_name = company_name
        self.identification_doc_type = identification_doc_type
        self.identification_doc_id = identification_doc_id
        self.customer_ip = customer_ip

    def to_params(self):
        return {"customer.merchantCustomerId": self.merchant_customer_id,
                "customer.givenName": self.given_name,
                "customer.surname": self.surname,
                "customer.sex": self.sex,
                "customer.birthDate": self.birth_date,
                "customer.phone": self.phone,
                "customer.mobile": self.mobile,
                "customer.email": self.email,
                "customer.companyName": self.company_name,
                "customer.identificationDocType": self.identification_doc_type,
                "customer.identificationDocId": self.identification_doc_id,
                "customer.ip": self.customer_ip}

    @staticmethod
    def from_params(params):
        if params is not None:
            return Customer(merchant_customer_id=params.get('merchantCustomerId'), given_name=params.get('givenName'),
                            surname=params.get('surname'), sex=params.get('sex'), birth_date=params.get('birthDate'),
                            phone=params.get('phone'), mobile=params.get('mobile'), email=params.get('email'),
                            company_name=params.get('companyName'),
                            identification_doc_type=params.get('identificationDocType'),
                            identification_doc_id=params.get('identificationDocId'),
                            customer_ip=params.get('customer.ip'))


class BillingAddress(object):
    def __init__(self, street1=None, street2=None, city=None, state=None, postcode=None, country=None):
        """


        :rtype : object
        :param street1:
        :param street2:
        :param city:
        :param state:
        :param postcode:
        :param country:
        """
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country

    def to_params(self):
        return {"billing.street1": self.street1,
                "billing.street2": self.street2,
                "billing.city": self.city,
                "billing.state": self.state,
                "billing.postcode": self.postcode,
                "billing.country": self.country}

    @staticmethod
    def from_params(params):
        if params is not None:
            return BillingAddress(street1=params.get('street1'), street2=params.get('street2'), city=params.get('city'),
                                  state=params.get('state'), postcode=params.get('postcode'),
                                  country=params.get('country'))


class ShippingAddress(object):
    def __init__(self, given_name=None, surname=None, street1=None, street2=None, city=None, state=None, postcode=None,
                 country=None):
        """


        :rtype : object
        :param given_name:
        :param surname:
        :param street1:
        :param street2:
        :param city:
        :param state:
        :param postcode:
        :param country:
        """
        self.given_name = given_name
        self.surname = surname
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country

    def to_params(self):
        return {"shipping.givenName": self.given_name,
                "shipping.surname": self.surname,
                "shipping.street1": self.street1,
                "shipping.street2": self.street2,
                "shipping.city": self.city,
                "shipping.state": self.state,
                "shipping.postcode": self.postcode,
                "shipping.country": self.country}

    @staticmethod
    def from_params(params):
        if params is not None:
            return BillingAddress(given_name=params.get('givenName'), surname=params.get('surname'),
                                  street1=params.get('street1'), street2=params.get('street2'), city=params.get('city'),
                                  state=params.get('state'),
                                  postcode=params.get('postcode'), country=params.get('country'))


class Item(object):
    def __init__(self, name=None, merchant_item_id=None, quantity=None, type=None, price=None, currency=None,
                 description=None, tax=None, shipping=None, discount=None):
        """


        :rtype : object
        :param name:
        :param merchant_item_id:
        :param quantity:
        :param type:
        :param price:
        :param currency:
        :param description:
        :param tax:
        :param shipping:
        :param discount:
        """
        self.name = name
        self.merchant_item_id = merchant_item_id
        self.quantity = quantity
        self.type = type
        self.price = price
        self.currency = currency
        self.description = description
        self.tax = tax
        self.shipping = shipping
        self.discount = discount

    def to_params(self):
        return {"name": self.name,
                "merchantItemId": self.merchant_item_id,
                "quantity": self.quantity,
                "type": self.type,
                "price": self.price,
                "currency": self.currency,
                "description": self.description,
                "tax": self.tax,
                "shipping": self.shipping,
                "discount": self.discount}

    @staticmethod
    def from_params(params):
        if params is not None:
            return Item(name=params.get('name'), merchant_item_id=params.get('merchantItemId'),
                        quantity=params.get('quantity'), type=params.get('type'), price=params.get('price'),
                        currency=params.get('currency'), description=params.get('description'), tax=params.get('tax'),
                        shipping=params.get('shipping'), discount=params.get('discount'))


class Cart(object):
    def __init__(self, items=None):
        self.items = items

    def to_params(self):
        params = {}
        count = 0
        for item in self.items:
            for k, v in item.to_params().iteritems():
                key_str = "cart.items[{0}].{1}".format(count, k)
                value_str = "{0}".format(v)
                d = {key_str: value_str}
                params.update(d)
            count += 1
        return params

    @staticmethod
    def from_params(params):
        items = list()
        if params is not None:
            for param in params:
                item = Item.from_params(param)
                if item is not None:
                    items.append(item)

            return Cart(items=items)


class TokenizationAndRegistration(object):
    def __init__(self, create_registration=None):
        """


        :rtype : object
        :param create_registration:
        """
        self.create_registration = create_registration

    def to_params(self):
        return {"createRegistration": self.create_registration}


class Recurring(object):
    def __init__(self, type=None):
        """


        :rtype : object
        :param type:
        """
        self.type = type

    def to_params(self):
        return {"recurringType": self.type}


class ThreeDSecure(object):
    def __init__(self, eci=None, verification_id=None, xid=None):
        """


        :rtype : object
        :param eci:
        :param verification_id:
        :param xid:
        """
        self.eci = eci
        self.verification_id = verification_id
        self.xid = xid

    def to_params(self):
        return {"threeDSecure.eci": self.eci,
                "threeDSecure.verificationId": self.verification_id,
                "threeDSecure.xid": self.xid}


class CustomParameters(object):
    def __init__(self, **kwargs):
        """
        :param kwargs:
        :rtype : object
        :param name:
        """
        for key, value in kwargs.iteritems():
            self.key = value

    def to_params(self):
        params = {}
        for key, value in self.__dict__.iteritems():
            params.update({"customParameters[{0}]".format(key): value})
        return params


class AsynchronousPayments(object):
    def __init__(self, shopper_result_url=None, notification_url=None):
        """


        :rtype : object
        :param shopper_result_url:
        :param notification_url:
        """
        self.shopper_result_url = shopper_result_url
        self.notification_url = notification_url

    def to_params(self):
        return {"shopperResultUrl": self.shopper_result_url,
                "notificationUrl": self.notification_url}


class Result(object):
    def __init__(self, code=None, description=None):
        self.code = code
        self.description = description

    @staticmethod
    def from_params(params):
        if params is not None:
            return Result(code=params.get('code'), description=params.get('description'))


class Merchant(object):
    def __init__(self, bank_account=None):
        self.bank_account = bank_account

    @staticmethod
    def from_params(params):
        if params is not None:
            return Merchant(bank_account=BankAccount.from_params(params.get('bankAccount')))


class Parameter(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def from_params(params):
        if params is not None:
            return Parameter(name=params.get('name'), value=params.get('value'))


class Redirect(object):
    def __init__(self, url=None, parameters=None):
        self.url = url
        self.parameters = parameters

    @staticmethod
    def from_params(params):
        if params is not None:
            parameters_list = list()
            parameters = params.get('parameters')
            for param in parameters:
                parameter = Parameter.from_params(param)
                if parameter is not None:
                    parameters_list.append(parameter)

            return Redirect(url=params.get('url'), parameters=parameters_list)


class ResponseParameters(object):
    def __init__(self, id=None, payment_type=None, payment_brand=None, amount=None, currency=None, descriptor=None,
                 result=None, card_account=None, virtual_account=None, bank_account=None, customer=None,
                 billing_address=None, shipping_address=None, cart=None, merchant=None, redirect=None,
                 timestamp=None, build_number=None, ndc=None):
        self.id = id
        self.payment_type = payment_type
        self.payment_brand = payment_brand
        self.amount = amount
        self.currency = currency
        self.descriptor = descriptor
        self.result = result
        self.card_account = card_account
        self.virtual_account = virtual_account
        self.bank_account = bank_account
        self.customer = customer
        self.billing_address = billing_address
        self.shipping_address = shipping_address
        self.cart = cart
        self.merchant = merchant
        self.async_payments = redirect
        self.timestamp = timestamp
        self.build_number = build_number
        self.ndc = ndc

    @staticmethod
    def from_params(params):
        if params is not None:
            # flat values
            id = params.get('id')
            payment_type = params.get('paymentType')
            payment_brand = params.get('paymentBrand')
            amount = params.get('paymentType')
            currency = params.get('currency')
            descriptor = params.get('descriptor')
            # nested objects
            result = Result.from_params(params.get('result'))
            card_account = CardAccount.from_params(params.get('cardAccount'))
            virtual_account = VirtualAccount.from_params(params.get('virtualAccount'))
            bank_account = BankAccount.from_params(params.get('bankAccount'))
            customer = Customer.from_params(params.get('customer')),
            billing_address = BillingAddress.from_params(params.get('billingAddress'))
            shipping_address = ShippingAddress.from_params(params.get('shippingAddress'))
            cart = Cart.from_params(params.get('cart'))
            merchant = Merchant.from_params(params.get('merchant'))
            redirect = Redirect.from_params(params.get('redirect'))
            timestamp = params.get('timestamp')
            build_number = params.get('buildNumber')
            ndc = params.get('ndc')
            response_params = ResponseParameters(id=id, payment_type=payment_type, payment_brand=payment_brand,
                                                 amount=amount, currency=currency, descriptor=descriptor,
                                                 result=result, card_account=card_account,
                                                 virtual_account=virtual_account,
                                                 bank_account=bank_account, customer=customer,
                                                 billing_address=billing_address, shipping_address=shipping_address,
                                                 cart=cart, merchant=merchant, redirect=redirect, timestamp=timestamp,
                                                 build_number=build_number, ndc=ndc)

            return response_params

    def response_successful(self):
        if opp.utils.check_result_code(self.result.code) == opp.utils.CODE_SUCCESSFUL:
            return True
        return False


class ErrorUtils(object):
    @staticmethod
    def create_exception_for_error(code='200', response='', err_codes=['400', '403', '404']):
        if str(code) in err_codes:
            return ExceptionFactory.create_exception(str(code), response)

    @staticmethod
    def raise_exception_for_error_code(code=None, response=None):
        exception = ErrorUtils.create_exception_for_error(code, response)
        if exception is not None:
            raise exception


def merge_inputs_to_dict(*args):
    request = {}
    for a in args:
        if a is not None:
            request.update(a.to_params())

    return request


class Captures(object):
    def __init__(self, payment_id=None, core=None):
        self.core = core
        self.captures = core.payments(payment_id=payment_id)

    def create(self, basic_payment=BasicPayment()):
        params = basic_payment.to_params()
        params.update({"paymentType": "CP"})
        response = self.captures.create(**params)
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)

    def get(self):
        return self.captures.get()


class Refunds(object):
    def __init__(self, payment_id=None, core=None):
        self.core = core
        self.refunds = core.payments(payment_id=payment_id)

    def create(self, basic_payment=BasicPayment()):
        params = basic_payment.to_params()
        params.update({"paymentType": "RF"})
        response = self.refunds.create(**params)
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)

    def get(self):
        return self.refunds.get()


class Reversals(object):
    def __init__(self, payment_id=None, core=None):
        self.core = core
        self.reversals = core.payments(payment_id=payment_id)

    def create(self):
        response = self.reversals.create(**{"paymentType": "RV"})
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)

    def get(self):
        return self.reversals.get()


class Credits(object):
    def __init__(self, payment_id=None, core=None):
        self.core = core
        self.credits = core.payments(payment_id=payment_id)

    def create(self, basic_payment=None, card_account=None):
        request = merge_inputs_to_dict(basic_payment, card_account)
        request.update({"paymentType": "CD"})
        response = self.credits.create(**request)
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)

    def get(self):
        return self.credits.get()


class Debits(object):
    def __init__(self, payment_id=None, core=None):
        self.core = core
        self.debits = core.payments(payment_id=payment_id)

    def create(self, basic_payment=None, card_account=None, virtual_account=None, bank_account=None, customer=None,
               billing_address=None, shipping_address=None, cart=None, create_registration=None, recurring_type=None,
               secure_3d=None, custom_parameters=None, async_payments=None, with_risk_check=False):
        request = merge_inputs_to_dict(basic_payment, card_account, virtual_account, bank_account, customer,
                                       billing_address, shipping_address, cart, create_registration, recurring_type,
                                       secure_3d, custom_parameters, async_payments)
        if with_risk_check:
            request.update({"paymentType": "PA.CP"})
        else:
            request.update({"paymentType": "DB"})
        response = self.debits.create(**request)
        exception = ErrorUtils.create_exception_for_error(self.core.http_client.response.status_code, response)
        if exception is not None:
            raise exception
        return opp.facade.ResponseParameters.from_params(response)

    def get(self):
        return self.debits.get()


class Preauthorizations(object):
    def __init__(self, payment_id=None, core=None):
        self.core = core
        self.preauthorizations = core.payments(payment_id=payment_id)

    def create(self, basic_payment=None, card_account=None, virtual_account=None, bank_account=None, customer=None,
               billing_address=None, shipping_address=None, cart=None, create_registration=None, recurring_type=None,
               secure_3d=None, custom_parameters=None, async_payments=None):
        request = merge_inputs_to_dict(basic_payment, card_account, virtual_account, bank_account, customer,
                                       billing_address, shipping_address, cart, create_registration, recurring_type,
                                       secure_3d, custom_parameters, async_payments)

        request.update({"paymentType": "PA"})
        response = self.preauthorizations.create(**request)
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)

    def get(self):
        return self.preauthorizations.get()


class Checkouts(object):
    def __init__(self, checkout_id=None, core=None):
        self.checkouts = core.checkouts(checkout_id=checkout_id)

    def create(self, basic_payment=BasicPayment()):
        response = self.checkouts.create(**basic_payment.to_params())
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)

    def get(self):
        return self.checkouts.get()


class Registrations(object):
    def __init__(self, registration_id=None, core=None):
        self.registrations = core.registrations(registration_id=registration_id)

    def create(self, basic_payment=None, card_account=None):
        request = merge_inputs_to_dict(basic_payment, card_account)
        response = self.registrations.create(**request)
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)

    def get(self):
        response = self.registrations.get()
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)

    def delete(self):
        response = self.registrations.delete()
        ErrorUtils.raise_exception_for_error_code(self.core.http_client.response.status_code, response)
        return opp.facade.ResponseParameters.from_params(response)


class API(object):
    def __init__(self, authentication=None):
        """


        :param authentication:
        :rtype : object
        """
        self.authentication = authentication
        self.core = opp.core.API(**authentication.to_params())

    def refunds(self, payment_id=None):
        return Refunds(payment_id=payment_id, core=self.core)

    def captures(self, payment_id=None):
        return Captures(payment_id=payment_id, core=self.core)

    def reversals(self, payment_id=None):
        return Reversals(payment_id=payment_id, core=self.core)

    def debits(self, payment_id=None):
        return Debits(payment_id=payment_id, core=self.core)

    def credits(self, payment_id=None):
        return Credits(payment_id=payment_id, core=self.core)

    def preauthorizations(self, payment_id=None):
        return Preauthorizations(payment_id=payment_id, core=self.core)

    def checkouts(self, checkout_id=None):
        return Checkouts(checkout_id=checkout_id, core=self.core)

    def registrations(self, registration_id):
        return Registrations(registration_id=registration_id, core=self.core)


class ApiError(Exception):
    def __init__(self, code, response):
        self.code = code
        self.response = response

    def __str__(self):
        return repr("""http_code: {0}
                       reason:    {1}
                       response:  {2}""".format(self.code, opp.utils.check_result_code(self.response.get('result')
                                                                                       .get('code')), self.response))


class Unauthenticated(ApiError):
    pass


class NotFound(ApiError):
    pass


class BadRequest(ApiError):
    pass


class ExceptionFactory(object):
    code_exception_dict = {'400': BadRequest,
                           '403': Unauthenticated,
                           '404': NotFound}

    @staticmethod
    def create_exception(code, response):
        return ExceptionFactory.code_exception_dict[code](code, response)



