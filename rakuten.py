# coupons API
import requests

url = 'https://api.rakutenmarketing.com/coupon/1.0'
headers = {'Authorization': 'Bearer 60f755a633e64fbd2c9c49af48cdc6'}

req = requests.get(url, headers=headers)

print(req.status_code)
print(req.headers)
print(req.text)

# get approved merchant
import requests

url = 'https://api.rakutenmarketing.com/linklocator/1.0/getMerchByAppStatus/approved'
headers = {'Authorization': 'Bearer 60f755a633e64fbd2c9c49af48cdc6'}

req = requests.get(url, headers=headers)

print(req.status_code)
print(req.headers)
print(req.text)

