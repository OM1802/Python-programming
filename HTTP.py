import requests

url='https://www.ibm.com/'
r=requests.get(url)
print(r.status_code)
print(r.request.headers)
print("request body:", r.request.body)
print("header: ",r.headers)
print(r.headers['date'])
print(r.headers['Content-Type'])
print(r)