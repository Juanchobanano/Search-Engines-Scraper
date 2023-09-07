import requests
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup

proxy = "brd.superproxy.io:22225"
username = "brd-customer-hl_93b5fa1a-zone-data_center"
password = "ask3gh8zga95"

session = requests.session()
session.proxy = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
session.auth = HTTPProxyAuth(username, password)

print(session.proxy)
print(session.auth)

res = session.get("https://developer.mozilla.org/en-US/docs/Web/CSS/overflow")
print("Status code: ", res.status_code)

#print(BeautifulSoup(res.text).text)