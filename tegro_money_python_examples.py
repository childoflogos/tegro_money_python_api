import json
import requests
import hashlib
from hashlib import sha256
import config
import hmac


#//////////////
#METHOD: CREATE ORDER
#//////////////

url = 'https://tegro.money/api/createOrder/'

params = {
    "shop_id": "1913EA935149B1E5D852A",
    "nonce": 1613435880,
    "currency": "RUB",
    "amount": 100,
    "order_id": "1",
    "payment_system": 1,
    "fields": {
        "email": "user@email.ru",
        "phone": "79111231212"
    },
    "receipt": {
        "items": [
          {
            "name": "test item 1",
            "count": 1,
            "price": 600
          },
          {
            "name": "test item 2",
            "count": 1,
            "price": 600
          }
        ]
    }
}

body = json.dumps(params)
sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    "Authorization": f"Bearer {sign}",
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=headers, params=params)
print(response.json())

#//////////////
#Succesful response.json() example:
#{
#  "type": "success",
#  "desc": "",
#  "data": {
#    "id": 755555,
#    "url": "https://tegro.money/pay/complete/755555/7f259f856e7682a6e98179036a623696/"
#  }
#}
#//////////////

#//////////////
#METHOD: LIST SHOPS
#//////////////

url = "https://tegro.money/api/shops/"

params = {
  "shop_id": "1913EA935149B1E5D852A",
  "nonce": 1613435880
}

body = json.dumps(params)
sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    "Authorization": f"Bearer {sign}",
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=headers, params=params)
print(response.json())

#//////////////
#Succesful response.json() example:
#{
#  "type": "success",
#  "desc": "",
#  "data": {
#    "user_id": 1,
#    "shops": [
#      {
#        "id": 1,
#        "date_added": "2020-11-03 18:04:07",
#        "name": "DEMO1",
#        "url": "https://demo1",
#        "status": 1,
#        "public_key": "D0F98E7DD86BB7500914",
#        "desc": "DEMO1 SHOP"
#      },
#      {
#        "id": 2,
#        "date_added": "2020-11-03 22:38:58",
#        "name": "DEMO2",
#        "url": "https://demo2",
#        "status": 0,
#        "public_key": "1913EA935149B1E5D852A",
#        "desc": "DEMO2 SHOP"
#      }
#    ]
#  }
#}
#//////////////

#//////////////
#METHOD: BALANCE
#//////////////

url = "https://tegro.money/api/balance/"

params = {
  "shop_id": "1913EA935149B1E5D852A",
  "nonce": 1613435880
}

body = json.dumps(params)
sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    "Authorization": f"Bearer {sign}",
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=headers, params=params)
print(response.json())

#//////////////
#Succesful response.json() example:
#{
#  "type": "success",
#  "desc": "",
#  "data": {
#    "user_id": 1,
#    "balance": {
#      "RUB": "1396.68",
#      "USD": "0.00",
#      "EUR": "1.23",
#      "UAH": "0.00"
#    }
#  }
#}
#//////////////

#//////////////
#METHOD: CHECK ORDER
#//////////////

url = 'https://tegro.money/api/order/'

params = {
  "shop_id": "1913EA935149B1E5D852A",
  "nonce": 1613435880,
  "order_id": 755555,
  "payment_id": "test order"
}

body = json.dumps(params)
sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    "Authorization": f"Bearer {sign}",
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=headers, params=params)
print(response.json())

#//////////////
#Succesful response.json() example:
#{
#  "type": "success",
#  "desc": "",
#  "data": {
#    "id": 1232,
#    "date_created": "2020-11-14 23:32:37",
#    "date_payed": "2020-11-14 23:33:39",
#    "status": 1,
#    "payment_system_id": 10,
#    "currency_id": 1,
#    "amount": "64.18000000",
#    "fee": "4.00000000",
#    "email": "user@site.ru",
#    "test_order": 0,
#    "payment_id": "Order #17854"
#  }
#}
#//////////////

#//////////////
#METHOD: ORDERS LIST
#//////////////

url = 'https://tegro.money/api/orders/'

params = {
  "shop_id": "1913EA935149B1E5D852A",
  "nonce": 1613435880,
  "page": 1
}

body = json.dumps(params)
sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    "Authorization": f"Bearer {sign}",
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=headers, params=params)
print(response.json())

#//////////////
#Succesful response.json() example:
#{
#  "type": "success",
#  "desc": "",
#  "data": [
#    {
#      "id": 123,
#      "date_created": "2020-11-14 23:32:37",
#      "date_payed": "2020-11-14 23:33:39",
#      "status": 1,
#      "payment_system_id": 10,
#      "currency_id": 1,
#      "amount": "64.18000000",
#      "fee": "4.00000000",
#      "email": "user@somesite",
#      "test_order": 0,
#      "payment_id": "Order #4175"
#    },
#    {
#      "id": 124,
#      "date_created": "2020-11-14 23:30:05",
#      "date_payed": null,
#      "status": 0,
#      "payment_system_id": 10,
#      "currency_id": 1,
#      "amount": "64.18000000",
#      "fee": "4.00000000",
#      "email": "user2@somesite",
#      "test_order": 0,
#      "payment_id": "Order #4174"
#    }
#  ]
#}
#//////////////

#//////////////
#METHOD: WITHDRAWAL
#//////////////

url = 'https://tegro.money/api/createWithdrawal/'

params = {
    "shop_id": "1913EA935149B1E5D852A",
    "nonce": 1613435880,
    "currency": "RUB",
    "account": "123",
    "amount": 100,
    "payment_id": 1124235,
    "payment_system": 1
}

body = json.dumps(params)
sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    "Authorization": f"Bearer {sign}",
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=headers, params=params)
print(response.json())

#//////////////
#METHOD: WITHDRAWALS LIST
#//////////////

url = 'https://tegro.money/api/withdrawals/'

params = {
  "shop_id": "1913EA935149B1E5D852A",
  "nonce": 1613435880,
  "page": 1
}

body = json.dumps(params)
sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    "Authorization": f"Bearer {sign}",
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=headers, params=params)
print(response.json())

#//////////////
#METHOD: CHECK WITHDRAWAL
#//////////////

url = 'https://tegro.money/api/withdrawal/'

params = {
  "shop_id": "1913EA935149B1E5D852A",
  "nonce": 1613435880,
  "order_id": 755555,
  "payment_id": "test order"
}

body = json.dumps(params)
sign = hmac.new(config.api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    "Authorization": f"Bearer {sign}",
    "Content-Type": "application/json"
}

response = requests.post(url=url, headers=headers, params=params)
print(response.json())