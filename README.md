# opp-python
Python wrapper for the [PAY.ON’s Open Payment Platform](https://docs.oppwa.com/) server-to-server REST API.

## Getting started

- We highly recommend to start with the [integration guide](https://docs.oppwa.com/) to get familiar with the OPP workflow.
- Check the server-to-server [documentation](https://docs.oppwa.com/server-to-server) and try out our code snippets.
- Install the latest release.
- Take a look at our [tests](tests/) to see the wrapper in action.

## Installation
The recommended way for installing the package is from PyPi, executing the following line:

```
pip install opp
```

Alternatively, you can clone the project and install it locally.

```
git clone git@github.com:OpenPaymentPlatform/python.git
cd python
pip install .
```
## News

We have just released the first version of our wrapper - 1.0.0 . Feel free to share with us any feedback, bugs, feature requests or your project using our wrapper, by opening an [issue](issues).

## Usage
The wrapper exposes two interfaces.
- The core interface is a simple http client for low level communication. It exposes only basic services, corresponding to the API endpoints. Requests and responses are dictionaries.
- The facade interface allows a higher level communication with the API. It exposes convinience services for implementing specific payment workflows. Requests are parameterized, API responses are deserialized. The interface also contains several helper functions.

### Core
In order to use the core module, you should first import it as shown below:
```python
import opp.core
```

#### Initialization
Initialize a core wrapper instance by providing your credentials:
```python
api = opp.core.API(**{"authentication.userId": "YourUserId",
                      "authentication.password": "YourPassword",
                      "authentication.entityId": "YourEntityId"})
```


##### Services

The core interface exposes several services through ``opp.core.API``, representing the different API endpoints:

- payments()
- checkouts()
- registrations()

Every service provides methods for the (available) CRUD functionality of the endpoint.
Note, that the services are initialized along the wrapper instance, you should not create them explicitly.

##### Create

To create an object, just call the ``create`` method on the service, for example:

```python
checkout = api.checkouts().create(**{"amount": "92.00",
                                     "currency": "EUR",
                                     "paymentType": "PA"})
```
##### Retrieve

To retrieve an object, just supply the ID as an argument to the service and call ``get()``, for example:

```python
checkout2 = api.checkouts(checkout_id='some_id').get()
```

##### Delete

To delete an object, just supply the ID as an argument to the service and call ``get()``, for example:

```python
result = api.registrations(registration_id='some_id').delete()
```


### Facade
In order to use the ``facade`` module, you should first import it as shown below:
```python
import opp.facade
```

#### Objects
The facade interface is exposing convenience Python objects for the Open Payment Platform [parameters](https://docs.oppwa.com/parameters#) for inputs, as well as for response parameters. Following examples show some of the these objects and how to create them.
**Convention: All object properties in the facade are in snake case notation as opposed to the OPP API reference where a camel case notation is used.**

##### BasicPayment
```python
basic_payment = opp.facade.BasicPayment(amount='92.00', currency='EUR', payment_brand='AMEX', descriptor='Test Amex')
```
*The ``paymentType`` parameter from the OPP API reference is not included in the BasicPayment object, because it is mapped automatically depending which of the opp.facade.API services is used.*

##### CardAccount
```python
card_account = opp.facade.CardAccount(holder='Jane Jones', number='377777777777770', expiry_month='05',
                                      expiry_year='2018',
                                      cvv='1234')
```

##### VirtualAccount
```python
virtual_account = opp.facade.VirtualAccount(account_id="1a2b3c4d5e6f7g8h9i", password="sy6KJsT8")
```

##### BankAccount
```python
bank_account = opp.facade.BankAccount(holder="Jane Jones", bank_name="Deutsche Bank", number="1009534785",
                                      iban="DE23100000001234567890", bank_code="DEUTDEMM", bic="DEUTDEFF",
                                      country="DE",
                                      mandate=opp.facade.Mandate(id='1a2b3c4d5e6f7g8h9i', date_of_signature='2015-07-09'),
                                      transaction_due_date="2015-07-09")
```

##### Customer
```python
opp.facade.Customer(merchant_customer_id="1a2b3c4d5e6f7g8h9i", given_name="Jane",
                    surname="Jones", sex="F",
                    birth_date="1983-10-05", phone="+49 123456789", mobile="+49 987654321",
                    email="jane.jones@test.de", company_name="Test Company",
                    identification_doc_type="TAXSTATEMENT",
                    identification_doc_id="a1b2c3d4e5f6g7h8i9",
                    customer_ip="XX.XXX.XX.XXX")
```

#### Initialization
First, create an ``opp.facade.Authentication`` object:
```python
authentication = opp.facade.Authentication(user_id='8a8294174b7ecb28014b9699220015cc', password='sy6KJsT8',
                                           entity_id='8a8294174b7ecb28014b9699220015ca')
```

Then initialize the facade interface:

```python
api = opp.facade.API(authentication)
```

##### Services
The facade interface provides a more granular level of service description based on the operations and workflows you should implement.
Based on the payment type of the operation the ``opp.core.API.payments()`` service is divided into:

- preauthorizations()
- debits()
- credits()
- refunds()
- captures()
- reversals()

As in the ``core`` module the facade exposes its services through an object called ``opp.facade.API`` where following services are defined:

- preauthorizations()
- debits()
- credits()
- refunds()
- captures()
- reversals()
- checkouts()
- registrations()

As in the core module every service provides methods for the (available) CRUD functionality of the endpoint.
Note, that the services are initialized along the wrapper instance, you should not create them explicitly.

The ``facade`` modules provides an Exception mechanism when the OPP platform returns an error response.

##### Create

To create an object, just call the ``create`` method on the service, for example:

```python
try:
    preauthorization = api.preauthorizations().create(basic_payment, card_account)
    print(preauthorization.result.code)
except opp.facade.ApiError as e:
    #handle error
    print(e)
```

As you can see in the example above all returned properties by the OPP API can be accessed with the dot operator from the returned Python object.

##### Retrieve

To retrieve an object, just supply the ID as an argument to the service and call ``get()``, for example:

```python
try:
    transaction = api.debits(payment_id='some_id').get()
except opp.facade.ApiError as e:
    #handle error
    print(e)
```

##### Delete

To delete an object, just supply the ID as an argument to the service and call ``get()``, for example:

```python
try:
    result = api.registrations(registration_id='some_id').delete()
except opp.facade.ApiError as e:
    #handle error
    print(e)
```

### Configuration
The ``config`` module provides a simple interface for configuring some HTTP related policies as shown below.

```python
import opp.config
opp.config.configure(test_url=TEST_URL, live_url=LIVE_URL, mode=TEST_INTERNAL, request_timeout=REQUEST_TIMEOUT)
``` 
The same configuration applies for the ``opp.core``, as well as for the ``opp.facade`` modules.

### Logging
For logging the HTTP operations that are executed through the ``opp`` Python library you can use the standard ``logging`` utilityself.

```python
import logging
logging.basicConfig(level=logging.DEBUG, filename='opp.log')
``` 

## Changelog

### 1.0.0
* First version

## License

Copyright 2015 PAY.ON AG.

MIT License (enclosed)
