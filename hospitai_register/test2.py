import requests

cookies = {
    'cmi-user-ticket': 'tsdH5HwFdHYY7ns82U0Kli2s3uv1BXKdYrQdCA..',
}
headers = {
    'Origin': 'https://www.114yygh.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.114yygh.com/hospital/1/2feb85b952a4dcd6dbf832100f6ef595/200004097/source',
    'Connection': 'keep-alive',
    'Request-Source': 'PC',
}
params = (
    ('_time', '1589717746005'),
)
data = '{"firstDeptCode":"2feb85b952a4dcd6dbf832100f6ef595","secondDeptCode":"200004097","hosCode":"1","week":1}'
response = requests.post('https://www.114yygh.com/web/product/list', headers=headers, params=params, cookies=cookies, data=data)
print(response.json())