import requests

print('hello')
res=requests.request(method='GET',url='https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=3296')
print(res.status_code)
